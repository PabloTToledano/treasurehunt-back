import os

from google.oauth2 import id_token
from google.auth.transport import requests
from swagger_server.models.user import User 

def verifyToken(userToken):
    try:
        idinfo = id_token.verify_oauth2_token(userToken, requests.Request(), os.environ['CLIENT_ID'])
        # ID token is valid. Get the user's Google Account ID from the decoded token.
        return True
    except ValueError:
        # Invalid token
        return False

def getUser(userToken):
    try:

        idinfo = id_token.verify_oauth2_token(userToken, requests.Request(), os.environ['CLIENT_ID'])

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        user = User(id = idinfo['sub'],username=idinfo['name'],email=idinfo['email'])
        return user
    except ValueError:
        # Invalid token
        return None
        