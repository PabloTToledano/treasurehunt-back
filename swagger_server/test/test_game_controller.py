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
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_treasure(self):
        """Test case for create_treasure

        uploads a treasure within a game
        """
        treasure = Treasure()
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game/{gameId}/treasures'.format(gameId=789),
            method='POST',
            data=json.dumps(treasure),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_game(self):
        """Test case for delete_game

        Deletes a game
        """
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game/{gameId}'.format(gameId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_games_by_active(self):
        """Test case for find_games_by_active

        Finds Games by active status
        """
        query_string = [('active', true)]
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game/findByActive',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_game_by_id(self):
        """Test case for get_game_by_id

        Find game by ID
        """
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game/{gameId}'.format(gameId=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_games(self):
        """Test case for get_games

        Get games
        """
        headers = [('userToken', 'userToken_example')]
        response = self.client.open(
            '/v1/game',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_game(self):
        """Test case for update_game

        Update an existing game
        """
        body = Game()
        response = self.client.open(
            '/v1/game',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
