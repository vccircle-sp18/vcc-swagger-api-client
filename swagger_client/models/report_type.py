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

class ReportType(object):
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
        'notifications': 'list[str]',
        'plagiarism': 'list[str]',
        'quick_reads': 'list[str]'
    }

    attribute_map = {
        'notifications': 'notifications',
        'plagiarism': 'plagiarism',
        'quick_reads': 'quickReads'
    }

    def __init__(self, notifications=None, plagiarism=None, quick_reads=None):  # noqa: E501
        """ReportType - a model defined in Swagger"""  # noqa: E501
        self._notifications = None
        self._plagiarism = None
        self._quick_reads = None
        self.discriminator = None
        if notifications is not None:
            self.notifications = notifications
        if plagiarism is not None:
            self.plagiarism = plagiarism
        if quick_reads is not None:
            self.quick_reads = quick_reads

    @property
    def notifications(self):
        """Gets the notifications of this ReportType.  # noqa: E501


        :return: The notifications of this ReportType.  # noqa: E501
        :rtype: list[str]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this ReportType.


        :param notifications: The notifications of this ReportType.  # noqa: E501
        :type: list[str]
        """

        self._notifications = notifications

    @property
    def plagiarism(self):
        """Gets the plagiarism of this ReportType.  # noqa: E501


        :return: The plagiarism of this ReportType.  # noqa: E501
        :rtype: list[str]
        """
        return self._plagiarism

    @plagiarism.setter
    def plagiarism(self, plagiarism):
        """Sets the plagiarism of this ReportType.


        :param plagiarism: The plagiarism of this ReportType.  # noqa: E501
        :type: list[str]
        """

        self._plagiarism = plagiarism

    @property
    def quick_reads(self):
        """Gets the quick_reads of this ReportType.  # noqa: E501


        :return: The quick_reads of this ReportType.  # noqa: E501
        :rtype: list[str]
        """
        return self._quick_reads

    @quick_reads.setter
    def quick_reads(self, quick_reads):
        """Sets the quick_reads of this ReportType.


        :param quick_reads: The quick_reads of this ReportType.  # noqa: E501
        :type: list[str]
        """

        self._quick_reads = quick_reads

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
        if issubclass(ReportType, dict):
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
        if not isinstance(other, ReportType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
