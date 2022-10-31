# coding: utf-8

"""
    CMS-Backend API

    This is API documentation of CMS-Backend  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: htdevteam@hindustantimes.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NotificationGeoLocations(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'geo_locations': 'dict(str, list[str])'
    }

    attribute_map = {
        'geo_locations': 'geoLocations'
    }

    def __init__(self, geo_locations=None):  # noqa: E501
        """NotificationGeoLocations - a model defined in Swagger"""  # noqa: E501
        self._geo_locations = None
        self.discriminator = None
        if geo_locations is not None:
            self.geo_locations = geo_locations

    @property
    def geo_locations(self):
        """Gets the geo_locations of this NotificationGeoLocations.  # noqa: E501


        :return: The geo_locations of this NotificationGeoLocations.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._geo_locations

    @geo_locations.setter
    def geo_locations(self, geo_locations):
        """Sets the geo_locations of this NotificationGeoLocations.


        :param geo_locations: The geo_locations of this NotificationGeoLocations.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._geo_locations = geo_locations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NotificationGeoLocations, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationGeoLocations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
