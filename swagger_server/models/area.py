# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Area(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, center_coordinates: List[float]=None, dimensions: List[float]=None):  # noqa: E501
        """Area - a model defined in Swagger

        :param center_coordinates: The center_coordinates of this Area.  # noqa: E501
        :type center_coordinates: List[float]
        :param dimensions: The dimensions of this Area.  # noqa: E501
        :type dimensions: List[float]
        """
        self.swagger_types = {
            'center_coordinates': List[float],
            'dimensions': List[float]
        }

        self.attribute_map = {
            'center_coordinates': 'centerCoordinates',
            'dimensions': 'dimensions'
        }

        self._center_coordinates = center_coordinates
        self._dimensions = dimensions

    @classmethod
    def from_dict(cls, dikt) -> 'Area':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Area of this Area.  # noqa: E501
        :rtype: Area
        """
        return util.deserialize_model(dikt, cls)

    @property
    def center_coordinates(self) -> List[float]:
        """Gets the center_coordinates of this Area.


        :return: The center_coordinates of this Area.
        :rtype: List[float]
        """
        return self._center_coordinates

    @center_coordinates.setter
    def center_coordinates(self, center_coordinates: List[float]):
        """Sets the center_coordinates of this Area.


        :param center_coordinates: The center_coordinates of this Area.
        :type center_coordinates: List[float]
        """

        self._center_coordinates = center_coordinates

    @property
    def dimensions(self) -> List[float]:
        """Gets the dimensions of this Area.


        :return: The dimensions of this Area.
        :rtype: List[float]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions: List[float]):
        """Sets the dimensions of this Area.


        :param dimensions: The dimensions of this Area.
        :type dimensions: List[float]
        """

        self._dimensions = dimensions
