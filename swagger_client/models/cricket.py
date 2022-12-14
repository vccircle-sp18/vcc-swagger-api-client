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

class Cricket(object):
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
        'match_file': 'str',
        'match_id': 'int',
        'match_name_with_date': 'str',
        'series_id': 'int',
        'series_name': 'str',
        'team_a': 'str',
        'team_a_id': 'str',
        'team_b': 'str',
        'team_b_id': 'str'
    }

    attribute_map = {
        'match_file': 'matchFile',
        'match_id': 'matchId',
        'match_name_with_date': 'matchNameWithDate',
        'series_id': 'seriesId',
        'series_name': 'seriesName',
        'team_a': 'teamA',
        'team_a_id': 'teamAId',
        'team_b': 'teamB',
        'team_b_id': 'teamBId'
    }

    def __init__(self, match_file=None, match_id=None, match_name_with_date=None, series_id=None, series_name=None, team_a=None, team_a_id=None, team_b=None, team_b_id=None):  # noqa: E501
        """Cricket - a model defined in Swagger"""  # noqa: E501
        self._match_file = None
        self._match_id = None
        self._match_name_with_date = None
        self._series_id = None
        self._series_name = None
        self._team_a = None
        self._team_a_id = None
        self._team_b = None
        self._team_b_id = None
        self.discriminator = None
        if match_file is not None:
            self.match_file = match_file
        if match_id is not None:
            self.match_id = match_id
        if match_name_with_date is not None:
            self.match_name_with_date = match_name_with_date
        if series_id is not None:
            self.series_id = series_id
        if series_name is not None:
            self.series_name = series_name
        if team_a is not None:
            self.team_a = team_a
        if team_a_id is not None:
            self.team_a_id = team_a_id
        if team_b is not None:
            self.team_b = team_b
        if team_b_id is not None:
            self.team_b_id = team_b_id

    @property
    def match_file(self):
        """Gets the match_file of this Cricket.  # noqa: E501


        :return: The match_file of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._match_file

    @match_file.setter
    def match_file(self, match_file):
        """Sets the match_file of this Cricket.


        :param match_file: The match_file of this Cricket.  # noqa: E501
        :type: str
        """

        self._match_file = match_file

    @property
    def match_id(self):
        """Gets the match_id of this Cricket.  # noqa: E501


        :return: The match_id of this Cricket.  # noqa: E501
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this Cricket.


        :param match_id: The match_id of this Cricket.  # noqa: E501
        :type: int
        """

        self._match_id = match_id

    @property
    def match_name_with_date(self):
        """Gets the match_name_with_date of this Cricket.  # noqa: E501


        :return: The match_name_with_date of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._match_name_with_date

    @match_name_with_date.setter
    def match_name_with_date(self, match_name_with_date):
        """Sets the match_name_with_date of this Cricket.


        :param match_name_with_date: The match_name_with_date of this Cricket.  # noqa: E501
        :type: str
        """

        self._match_name_with_date = match_name_with_date

    @property
    def series_id(self):
        """Gets the series_id of this Cricket.  # noqa: E501


        :return: The series_id of this Cricket.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this Cricket.


        :param series_id: The series_id of this Cricket.  # noqa: E501
        :type: int
        """

        self._series_id = series_id

    @property
    def series_name(self):
        """Gets the series_name of this Cricket.  # noqa: E501


        :return: The series_name of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._series_name

    @series_name.setter
    def series_name(self, series_name):
        """Sets the series_name of this Cricket.


        :param series_name: The series_name of this Cricket.  # noqa: E501
        :type: str
        """

        self._series_name = series_name

    @property
    def team_a(self):
        """Gets the team_a of this Cricket.  # noqa: E501


        :return: The team_a of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._team_a

    @team_a.setter
    def team_a(self, team_a):
        """Sets the team_a of this Cricket.


        :param team_a: The team_a of this Cricket.  # noqa: E501
        :type: str
        """

        self._team_a = team_a

    @property
    def team_a_id(self):
        """Gets the team_a_id of this Cricket.  # noqa: E501


        :return: The team_a_id of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._team_a_id

    @team_a_id.setter
    def team_a_id(self, team_a_id):
        """Sets the team_a_id of this Cricket.


        :param team_a_id: The team_a_id of this Cricket.  # noqa: E501
        :type: str
        """

        self._team_a_id = team_a_id

    @property
    def team_b(self):
        """Gets the team_b of this Cricket.  # noqa: E501


        :return: The team_b of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._team_b

    @team_b.setter
    def team_b(self, team_b):
        """Sets the team_b of this Cricket.


        :param team_b: The team_b of this Cricket.  # noqa: E501
        :type: str
        """

        self._team_b = team_b

    @property
    def team_b_id(self):
        """Gets the team_b_id of this Cricket.  # noqa: E501


        :return: The team_b_id of this Cricket.  # noqa: E501
        :rtype: str
        """
        return self._team_b_id

    @team_b_id.setter
    def team_b_id(self, team_b_id):
        """Sets the team_b_id of this Cricket.


        :param team_b_id: The team_b_id of this Cricket.  # noqa: E501
        :type: str
        """

        self._team_b_id = team_b_id

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
        if issubclass(Cricket, dict):
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
        if not isinstance(other, Cricket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
