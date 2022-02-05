import connexion
import pymongo
import os
import six

from bson import json_util, ObjectId
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from swagger_server.controllers.token_controller import verifyToken,getUser

uri = os.environ['MONGODB_URI'] 
client = pymongo.MongoClient(uri)
db = client.get_default_database()
usersDB = db.users 

def create_user(userToken, body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param userToken: 
    :type userToken: str
    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(userToken, userId):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param userToken: 
    :type userToken: str
    :param userId: The name that needs to be deleted
    :type userId: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        userId = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user(userToken, id=None):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param userToken: 
    :type userToken: str

    :rtype: User
    """
    if id is None:
        user = getUser(userToken)
        if user is None:
            return 'User not valid' ,404
            
        # verify if user already exists
        try:
            userFromDB = usersDB.find({'email': user.email})[0]
            user.rol = userFromDB['rol']
        except IndexError:
            # user doesn't exist
            user.rol = 'user'
            userjson = {"_id": user.id, "username": user.username, "email": user.email, "rol": user.rol}
            usersDB.insert_one(userjson)
        return user
    else:
        try:
            userFromDB = usersDB.find({'_id': id})[0]
            return userFromDB['username']
        except IndexError:
            # user doesn't exist
            return 'Not found', 404
