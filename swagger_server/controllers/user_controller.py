import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


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


def get_user_by_token(userToken):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param userToken: 
    :type userToken: str

    :rtype: User
    """
    return 'do some magic!'
