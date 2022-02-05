# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.treasure import Treasure  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGameController(BaseTestCase):
    """GameController integration test stubs"""

    def test_add_game(self):
        """Test case for add_game

        Add a game
        """
        body = Game()
        query_string = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_treasure(self):
        """Test case for create_treasure

        uploads a treasure within a game
        """
        treasure = Treasure()
        query_string = [('id', 789),
                        ('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game/treasures',
            method='POST',
            data=json.dumps(treasure),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_games_by_active(self):
        """Test case for find_games_by_active

        Finds Games by active status
        """
        query_string = [('userToken', 'userToken_example'),
                        ('active', true)]
        response = self.client.open(
            '/v1/game/findByActive',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_games_by_user(self):
        """Test case for find_games_by_user

        Finds Games by user
        """
        query_string = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game/findByUser',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_games(self):
        """Test case for get_games

        Get games
        """
        query_string = [('userToken', 'userToken_example'),
                        ('id', 'id_example')]
        response = self.client.open(
            '/v1/game',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reset_game_by_id(self):
        """Test case for reset_game_by_id

        Reset game by ID
        """
        query_string = [('userToken', 'userToken_example'),
                        ('id', 789)]
        response = self.client.open(
            '/v1/game/reset',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_game(self):
        """Test case for update_game

        Update an existing game
        """
        body = Game()
        query_string = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
