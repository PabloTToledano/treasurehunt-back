# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.area import Area
from swagger_server.models.treasure import Treasure
from swagger_server import util


class Game(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, winner: str=None, description: str=None, organizer_id: float=None, area: Area=None, treasures: List[Treasure]=None, active: bool=None):  # noqa: E501
        """Game - a model defined in Swagger

        :param id: The id of this Game.  # noqa: E501
        :type id: str
        :param name: The name of this Game.  # noqa: E501
        :type name: str
        :param winner: The winner of this Game.  # noqa: E501
        :type winner: str
        :param description: The description of this Game.  # noqa: E501
        :type description: str
        :param organizer_id: The organizer_id of this Game.  # noqa: E501
        :type organizer_id: float
        :param area: The area of this Game.  # noqa: E501
        :type area: Area
        :param treasures: The treasures of this Game.  # noqa: E501
        :type treasures: List[Treasure]
        :param active: The active of this Game.  # noqa: E501
        :type active: bool
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'winner': str,
            'description': str,
            'organizer_id': float,
            'area': Area,
            'treasures': List[Treasure],
            'active': bool
        }

        self.attribute_map = {
            'id': '_id',
            'name': 'name',
            'winner': 'winner',
            'description': 'description',
            'organizer_id': 'organizerId',
            'area': 'area',
            'treasures': 'treasures',
            'active': 'active'
        }

        self._id = id
        self._name = name
        self._winner = winner
        self._description = description
        self._organizer_id = organizer_id
        self._area = area
        self._treasures = treasures
        self._active = active

    @classmethod
    def from_dict(cls, dikt) -> 'Game':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Game of this Game.  # noqa: E501
        :rtype: Game
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Game.


        :return: The id of this Game.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Game.


        :param id: The id of this Game.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Game.


        :return: The name of this Game.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Game.


        :param name: The name of this Game.
        :type name: str
        """

        self._name = name

    @property
    def winner(self) -> str:
        """Gets the winner of this Game.


        :return: The winner of this Game.
        :rtype: str
        """
        return self._winner

    @winner.setter
    def winner(self, winner: str):
        """Sets the winner of this Game.


        :param winner: The winner of this Game.
        :type winner: str
        """

        self._winner = winner

    @property
    def description(self) -> str:
        """Gets the description of this Game.


        :return: The description of this Game.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Game.


        :param description: The description of this Game.
        :type description: str
        """

        self._description = description

    @property
    def organizer_id(self) -> float:
        """Gets the organizer_id of this Game.


        :return: The organizer_id of this Game.
        :rtype: float
        """
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, organizer_id: float):
        """Sets the organizer_id of this Game.


        :param organizer_id: The organizer_id of this Game.
        :type organizer_id: float
        """

        self._organizer_id = organizer_id

    @property
    def area(self) -> Area:
        """Gets the area of this Game.


        :return: The area of this Game.
        :rtype: Area
        """
        return self._area

    @area.setter
    def area(self, area: Area):
        """Sets the area of this Game.


        :param area: The area of this Game.
        :type area: Area
        """
        if area is None:
            raise ValueError("Invalid value for `area`, must not be `None`")  # noqa: E501

        self._area = area

    @property
    def treasures(self) -> List[Treasure]:
        """Gets the treasures of this Game.


        :return: The treasures of this Game.
        :rtype: List[Treasure]
        """
        return self._treasures

    @treasures.setter
    def treasures(self, treasures: List[Treasure]):
        """Sets the treasures of this Game.


        :param treasures: The treasures of this Game.
        :type treasures: List[Treasure]
        """
        if treasures is None:
            raise ValueError("Invalid value for `treasures`, must not be `None`")  # noqa: E501

        self._treasures = treasures

    @property
    def active(self) -> bool:
        """Gets the active of this Game.

        game status  # noqa: E501

        :return: The active of this Game.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this Game.

        game status  # noqa: E501

        :param active: The active of this Game.
        :type active: bool
        """

        self._active = active
