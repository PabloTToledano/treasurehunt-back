import connexion
import six

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.treasure import Treasure  # noqa: E501
from swagger_server import util


def add_game(userToken, body):  # noqa: E501
    """Add a game

     # noqa: E501

    :param userToken: 
    :type userToken: str
    :param body: Game that needs to be created
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Game.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_treasure(gameId, userToken, treasure):  # noqa: E501
    """uploads a treasure within a game

     # noqa: E501

    :param gameId: ID of game to update
    :type gameId: int
    :param userToken: 
    :type userToken: str
    :param treasure: The treasure to be uploaded
    :type treasure: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        treasure = Treasure.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_game(userToken, gameId):  # noqa: E501
    """Deletes a game

     # noqa: E501

    :param userToken: 
    :type userToken: str
    :param gameId: Game id to delete
    :type gameId: int

    :rtype: None
    """
    return 'do some magic!'


def find_games_by_active(userToken, active):  # noqa: E501
    """Finds Games by active status

     # noqa: E501

    :param userToken: 
    :type userToken: str
    :param active: Active value that need to be considered for filter
    :type active: bool

    :rtype: List[Game]
    """
    return 'do some magic!'


def get_game_by_id(userToken, gameId):  # noqa: E501
    """Find game by ID

    Returns a single game # noqa: E501

    :param userToken: 
    :type userToken: str
    :param gameId: ID of game to return
    :type gameId: int

    :rtype: Game
    """
    return 'do some magic!'


def get_games(userToken):  # noqa: E501
    """Get games

    Returns all games # noqa: E501

    :param userToken: 
    :type userToken: str

    :rtype: Game
    """
    return 'do some magic!'


def update_game(body):  # noqa: E501
    """Update an existing game

     # noqa: E501

    :param body: Game that need to be put in the treasure hunt game
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Game.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
