# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        body = User()
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        userId = User()
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/user',
            method='DELETE',
            data=json.dumps(userId),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by user name
        """
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/user',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
