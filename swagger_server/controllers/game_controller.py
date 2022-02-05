from xmlrpc.client import Boolean
import connexion
import pymongo
import json
import os
import six

from bson import json_util, ObjectId
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.treasure import Treasure  # noqa: E501
from swagger_server.models.found_treasure import FoundTreasure  # noqa: E501
from swagger_server import util
from swagger_server.controllers.token_controller import verifyToken,getUser
from swagger_server.controllers.user_controller import get_user_by_token

uri = os.environ['MONGODB_URI'] 
client = pymongo.MongoClient(uri)
db = client.get_default_database()
gamesDB = db.games
usersDB = db.users 


def add_game(userToken, body):  # noqa: E501
    """Add a game

     # noqa: E501

    :param userToken: 
    :type userToken: str
    :param body: Game that needs to be created
    :type body: dict | bytes

    :rtype: None
    """
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501
        body['organizerId'] = user.id
        gameid = gamesDB.insert_one(body)
        games = list(gamesDB.find({'_id': ObjectId(gameid.inserted_id)}))
        if len(games) == 0:
            return 'Game could not be created', 404
        games[0]['_id'] = str(games[0]['_id']) #swagger doesn't like ObjectId objects
        game = Game().from_dict(games[0])
        return game
    return 'Invalid json file', 400

def delete_games(userToken, id=None):  # noqa: E501
    """Get games

    Deletes a game # noqa: E501

    :param userToken: 
    :type userToken: str
    :param id: 
    :type id: str

    :rtype: None
    """

    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404

    return 'do some magic!'

def create_treasure(id, userToken, treasure):  # noqa: E501
    """uploads a treasure within a game

     # noqa: E501

    :param id: ID of game to update
    :type id: int
    :param userToken: 
    :type userToken: str
    :param treasure: The treasure to be uploaded
    :type treasure: dict | bytes

    :rtype: None
    """
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404

    if connexion.request.is_json:
        treasure = Treasure.from_dict(connexion.request.get_json())  # noqa: E501
    return treasure


def find_games_by_active(userToken, active):  # noqa: E501
    """Finds Games by active status

     # noqa: E501

    :param userToken: 
    :type userToken: str
    :param active: Active value that need to be considered for filter
    :type active: bool

    :rtype: List[Game]
    """
    if active is not Boolean:
        return 'invalid active value', 400 
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404

    return json_util.dumps(list(gamesDB.find({'active': active},{'treasures.location' : 0})))


def find_games_by_user(userToken):  # noqa: E501
    """Finds Games by user

     # noqa: E501

    :param userToken: 
    :type userToken: str

    :rtype: List[Game]
    """
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404
    games = list(gamesDB.find({'organizerId': user.id},))
    gamesObjList = []
    for gameDic in games:
        gameDic['_id'] = str(gameDic['_id']) #swagger doesn't like ObjectId objects
        gamesObjList.append( Game().from_dict(gameDic))
        
    return gamesObjList



def get_games(userToken, id=None):  # noqa: E501
    """Get games

    Returns all games if no id is given # noqa: E501

    :param userToken: 
    :type userToken: str
    :param id: 
    :type id: str

    :rtype: Game
    """

    #json_util.dumps(list(gamesDB.find({'_id': ObjectId(gameId)},{'treasures.location' : 0})))
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404
    if id is not None:
        games = list(gamesDB.find({'_id': ObjectId(id)}))
        if len(games) == 0:
            return 'Game not found', 404
        games[0]['_id'] = str(games[0]['_id']) #swagger doesn't like ObjectId objects
        game = Game().from_dict(games[0])
        userFromDB = usersDB.find({'email': user.email})[0]
        if user.id != game.organizer_id and userFromDB['rol'] == 'user':
            for treasure in game.treasures:
                treasure.location = []
        return game
    else:
        #return all games
        games = list(gamesDB.find({},{'treasures.location' : 0}))
        gamesObjList = []
        for gameDic in games:
            gameDic['_id'] = str(gameDic['_id']) #swagger doesn't like ObjectId objects
            gamesObjList.append( Game().from_dict(gameDic))
        return gamesObjList

    return 

def reset_game_by_id(userToken, id):  # noqa: E501
    """Reset game by ID

    Returns a reset game # noqa: E501

    :param userToken: 
    :type userToken: str
    :param id: ID of game to return
    :type id: int

    :rtype: Game
    """
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404
    userFromDB = usersDB.find({'email': user.email})[0]
    user.rol = userFromDB['rol']
    games = list(gamesDB.find({'_id': ObjectId(id)}))
    if len(games) == 0:
        return 'Game not found', 404    
    games[0]['_id'] = str(games[0]['_id']) #swagger doesn't like ObjectId objects
    game = Game().from_dict(games[0])

    if user.id != game.organizer_id and userFromDB['rol'] == 'user':
        return 'Not auth', 401
    #we know the user is either the organizer or admin
    games[0]['winner'] = ''
    games[0]['active'] = True
    games[0]['_id'] = ObjectId(games[0]['_id'])
    for treasure in games[0]['treasures']:
        treasure['found'] = []
    
    gamesDB.replace_one({'_id': ObjectId(id)},games[0])
    
    #return updated game
    games = list(gamesDB.find({'_id': ObjectId(id)}))
    games[0]['_id'] = str(games[0]['_id']) #swagger doesn't like ObjectId objects
    game = Game().from_dict(games[0])
    return game


def update_game(userToken, body):  # noqa: E501
    """Update an existing game

     # noqa: E501

    :param body: Game that need to be put in the treasure hunt game
    :type body: dict | bytes

    :rtype: None
    """
    user = getUser(userToken)
    if user is None:
        return 'User not valid' ,404

    if connexion.request.is_json:
        body = Game.from_dict(connexion.request.get_json())  # noqa: E501
    return body


def treasure_found(id, userToken, treasure):  # noqa: E501
    """uploads a treasure within a game

     # noqa: E501

    :param id: ID of game to update
    :type id: int
    :param userToken: 
    :type userToken: str
    :param treasure: The treasure to be uploaded
    :type treasure: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        treasure = FoundTreasure.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'