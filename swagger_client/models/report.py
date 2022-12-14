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

class Report(object):
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
        'created_by': 'str',
        'created_date': 'str',
        'date_from': 'str',
        'date_to': 'str',
        'domain_id': 'str',
        'id': 'int',
        'report_generation_type': 'str',
        'report_type': 'str',
        'report_url': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_date': 'createdDate',
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'domain_id': 'domainId',
        'id': 'id',
        'report_generation_type': 'reportGenerationType',
        'report_type': 'reportType',
        'report_url': 'reportUrl'
    }

    def __init__(self, created_by=None, created_date=None, date_from=None, date_to=None, domain_id=None, id=None, report_generation_type=None, report_type=None, report_url=None):  # noqa: E501
        """Report - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_date = None
        self._date_from = None
        self._date_to = None
        self._domain_id = None
        self._id = None
        self._report_generation_type = None
        self._report_type = None
        self._report_url = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if report_generation_type is not None:
            self.report_generation_type = report_generation_type
        if report_type is not None:
            self.report_type = report_type
        if report_url is not None:
            self.report_url = report_url

    @property
    def created_by(self):
        """Gets the created_by of this Report.  # noqa: E501


        :return: The created_by of this Report.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Report.


        :param created_by: The created_by of this Report.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_date(self):
        """Gets the created_date of this Report.  # noqa: E501


        :return: The created_date of this Report.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Report.


        :param created_date: The created_date of this Report.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def date_from(self):
        """Gets the date_from of this Report.  # noqa: E501


        :return: The date_from of this Report.  # noqa: E501
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this Report.


        :param date_from: The date_from of this Report.  # noqa: E501
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this Report.  # noqa: E501


        :return: The date_to of this Report.  # noqa: E501
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this Report.


        :param date_to: The date_to of this Report.  # noqa: E501
        :type: str
        """

        self._date_to = date_to

    @property
    def domain_id(self):
        """Gets the domain_id of this Report.  # noqa: E501


        :return: The domain_id of this Report.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Report.


        :param domain_id: The domain_id of this Report.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this Report.  # noqa: E501


        :return: The id of this Report.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Report.


        :param id: The id of this Report.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def report_generation_type(self):
        """Gets the report_generation_type of this Report.  # noqa: E501


        :return: The report_generation_type of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_generation_type

    @report_generation_type.setter
    def report_generation_type(self, report_generation_type):
        """Sets the report_generation_type of this Report.


        :param report_generation_type: The report_generation_type of this Report.  # noqa: E501
        :type: str
        """

        self._report_generation_type = report_generation_type

    @property
    def report_type(self):
        """Gets the report_type of this Report.  # noqa: E501


        :return: The report_type of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this Report.


        :param report_type: The report_type of this Report.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def report_url(self):
        """Gets the report_url of this Report.  # noqa: E501


        :return: The report_url of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this Report.


        :param report_url: The report_url of this Report.  # noqa: E501
        :type: str
        """

        self._report_url = report_url

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
        if issubclass(Report, dict):
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
        if not isinstance(other, Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
