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

class SectionNavigation(object):
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
        'links': 'list[PageCompact]',
        'locked_by_user_id': 'str',
        'locked_by_user_name': 'str',
        'locked_date': 'datetime',
        'modification_history': 'dict(str, str)',
        'status': 'str'
    }

    attribute_map = {
        'domain_id': 'domainId',
        'id': 'id',
        'links': 'links',
        'locked_by_user_id': 'lockedByUserId',
        'locked_by_user_name': 'lockedByUserName',
        'locked_date': 'lockedDate',
        'modification_history': 'modificationHistory',
        'status': 'status'
    }

    def __init__(self, domain_id=None, id=None, links=None, locked_by_user_id=None, locked_by_user_name=None, locked_date=None, modification_history=None, status=None):  # noqa: E501
        """SectionNavigation - a model defined in Swagger"""  # noqa: E501
        self._domain_id = None
        self._id = None
        self._links = None
        self._locked_by_user_id = None
        self._locked_by_user_name = None
        self._locked_date = None
        self._modification_history = None
        self._status = None
        self.discriminator = None
        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if locked_by_user_id is not None:
            self.locked_by_user_id = locked_by_user_id
        if locked_by_user_name is not None:
            self.locked_by_user_name = locked_by_user_name
        if locked_date is not None:
            self.locked_date = locked_date
        if modification_history is not None:
            self.modification_history = modification_history
        if status is not None:
            self.status = status

    @property
    def domain_id(self):
        """Gets the domain_id of this SectionNavigation.  # noqa: E501


        :return: The domain_id of this SectionNavigation.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SectionNavigation.


        :param domain_id: The domain_id of this SectionNavigation.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this SectionNavigation.  # noqa: E501


        :return: The id of this SectionNavigation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SectionNavigation.


        :param id: The id of this SectionNavigation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this SectionNavigation.  # noqa: E501


        :return: The links of this SectionNavigation.  # noqa: E501
        :rtype: list[PageCompact]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SectionNavigation.


        :param links: The links of this SectionNavigation.  # noqa: E501
        :type: list[PageCompact]
        """

        self._links = links

    @property
    def locked_by_user_id(self):
        """Gets the locked_by_user_id of this SectionNavigation.  # noqa: E501


        :return: The locked_by_user_id of this SectionNavigation.  # noqa: E501
        :rtype: str
        """
        return self._locked_by_user_id

    @locked_by_user_id.setter
    def locked_by_user_id(self, locked_by_user_id):
        """Sets the locked_by_user_id of this SectionNavigation.


        :param locked_by_user_id: The locked_by_user_id of this SectionNavigation.  # noqa: E501
        :type: str
        """

        self._locked_by_user_id = locked_by_user_id

    @property
    def locked_by_user_name(self):
        """Gets the locked_by_user_name of this SectionNavigation.  # noqa: E501


        :return: The locked_by_user_name of this SectionNavigation.  # noqa: E501
        :rtype: str
        """
        return self._locked_by_user_name

    @locked_by_user_name.setter
    def locked_by_user_name(self, locked_by_user_name):
        """Sets the locked_by_user_name of this SectionNavigation.


        :param locked_by_user_name: The locked_by_user_name of this SectionNavigation.  # noqa: E501
        :type: str
        """

        self._locked_by_user_name = locked_by_user_name

    @property
    def locked_date(self):
        """Gets the locked_date of this SectionNavigation.  # noqa: E501


        :return: The locked_date of this SectionNavigation.  # noqa: E501
        :rtype: datetime
        """
        return self._locked_date

    @locked_date.setter
    def locked_date(self, locked_date):
        """Sets the locked_date of this SectionNavigation.


        :param locked_date: The locked_date of this SectionNavigation.  # noqa: E501
        :type: datetime
        """

        self._locked_date = locked_date

    @property
    def modification_history(self):
        """Gets the modification_history of this SectionNavigation.  # noqa: E501


        :return: The modification_history of this SectionNavigation.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._modification_history

    @modification_history.setter
    def modification_history(self, modification_history):
        """Sets the modification_history of this SectionNavigation.


        :param modification_history: The modification_history of this SectionNavigation.  # noqa: E501
        :type: dict(str, str)
        """

        self._modification_history = modification_history

    @property
    def status(self):
        """Gets the status of this SectionNavigation.  # noqa: E501


        :return: The status of this SectionNavigation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SectionNavigation.


        :param status: The status of this SectionNavigation.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "PUBLISHED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(SectionNavigation, dict):
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
        if not isinstance(other, SectionNavigation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other