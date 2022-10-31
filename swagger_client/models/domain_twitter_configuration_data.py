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

class DomainTwitterConfigurationData(object):
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
        'domain_id': 'str',
        'id': 'str',
        'name': 'str',
        'twitter_handle': 'str'
    }

    attribute_map = {
        'domain_id': 'domainId',
        'id': 'id',
        'name': 'name',
        'twitter_handle': 'twitterHandle'
    }

    def __init__(self, domain_id=None, id=None, name=None, twitter_handle=None):  # noqa: E501
        """DomainTwitterConfigurationData - a model defined in Swagger"""  # noqa: E501
        self._domain_id = None
        self._id = None
        self._name = None
        self._twitter_handle = None
        self.discriminator = None
        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if twitter_handle is not None:
            self.twitter_handle = twitter_handle

    @property
    def domain_id(self):
        """Gets the domain_id of this DomainTwitterConfigurationData.  # noqa: E501


        :return: The domain_id of this DomainTwitterConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DomainTwitterConfigurationData.


        :param domain_id: The domain_id of this DomainTwitterConfigurationData.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this DomainTwitterConfigurationData.  # noqa: E501


        :return: The id of this DomainTwitterConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainTwitterConfigurationData.


        :param id: The id of this DomainTwitterConfigurationData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DomainTwitterConfigurationData.  # noqa: E501


        :return: The name of this DomainTwitterConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainTwitterConfigurationData.


        :param name: The name of this DomainTwitterConfigurationData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def twitter_handle(self):
        """Gets the twitter_handle of this DomainTwitterConfigurationData.  # noqa: E501


        :return: The twitter_handle of this DomainTwitterConfigurationData.  # noqa: E501
        :rtype: str
        """
        return self._twitter_handle

    @twitter_handle.setter
    def twitter_handle(self, twitter_handle):
        """Sets the twitter_handle of this DomainTwitterConfigurationData.


        :param twitter_handle: The twitter_handle of this DomainTwitterConfigurationData.  # noqa: E501
        :type: str
        """

        self._twitter_handle = twitter_handle

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
        if issubclass(DomainTwitterConfigurationData, dict):
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
        if not isinstance(other, DomainTwitterConfigurationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
