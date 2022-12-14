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

class MarketIndices(object):
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
        'code': 'str',
        'domain_ids': 'list[str]',
        'indices_type': 'str',
        'keyword_list': 'list[str]',
        'market_name': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'domain_ids': 'domainIds',
        'indices_type': 'indicesType',
        'keyword_list': 'keywordList',
        'market_name': 'marketName',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, code=None, domain_ids=None, indices_type=None, keyword_list=None, market_name=None, name=None, type=None):  # noqa: E501
        """MarketIndices - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._domain_ids = None
        self._indices_type = None
        self._keyword_list = None
        self._market_name = None
        self._name = None
        self._type = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if indices_type is not None:
            self.indices_type = indices_type
        if keyword_list is not None:
            self.keyword_list = keyword_list
        if market_name is not None:
            self.market_name = market_name
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def code(self):
        """Gets the code of this MarketIndices.  # noqa: E501


        :return: The code of this MarketIndices.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this MarketIndices.


        :param code: The code of this MarketIndices.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def domain_ids(self):
        """Gets the domain_ids of this MarketIndices.  # noqa: E501


        :return: The domain_ids of this MarketIndices.  # noqa: E501
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        """Sets the domain_ids of this MarketIndices.


        :param domain_ids: The domain_ids of this MarketIndices.  # noqa: E501
        :type: list[str]
        """

        self._domain_ids = domain_ids

    @property
    def indices_type(self):
        """Gets the indices_type of this MarketIndices.  # noqa: E501


        :return: The indices_type of this MarketIndices.  # noqa: E501
        :rtype: str
        """
        return self._indices_type

    @indices_type.setter
    def indices_type(self, indices_type):
        """Sets the indices_type of this MarketIndices.


        :param indices_type: The indices_type of this MarketIndices.  # noqa: E501
        :type: str
        """

        self._indices_type = indices_type

    @property
    def keyword_list(self):
        """Gets the keyword_list of this MarketIndices.  # noqa: E501


        :return: The keyword_list of this MarketIndices.  # noqa: E501
        :rtype: list[str]
        """
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, keyword_list):
        """Sets the keyword_list of this MarketIndices.


        :param keyword_list: The keyword_list of this MarketIndices.  # noqa: E501
        :type: list[str]
        """

        self._keyword_list = keyword_list

    @property
    def market_name(self):
        """Gets the market_name of this MarketIndices.  # noqa: E501


        :return: The market_name of this MarketIndices.  # noqa: E501
        :rtype: str
        """
        return self._market_name

    @market_name.setter
    def market_name(self, market_name):
        """Sets the market_name of this MarketIndices.


        :param market_name: The market_name of this MarketIndices.  # noqa: E501
        :type: str
        """

        self._market_name = market_name

    @property
    def name(self):
        """Gets the name of this MarketIndices.  # noqa: E501


        :return: The name of this MarketIndices.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MarketIndices.


        :param name: The name of this MarketIndices.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this MarketIndices.  # noqa: E501


        :return: The type of this MarketIndices.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MarketIndices.


        :param type: The type of this MarketIndices.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(MarketIndices, dict):
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
        if not isinstance(other, MarketIndices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
