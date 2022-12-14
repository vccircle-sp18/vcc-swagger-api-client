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

class BreakingNews(object):
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
        'domain_id': 'str',
        'headline': 'str',
        'id': 'str',
        'image': 'Image',
        'last_updated_by': 'str',
        'last_updated_date': 'str',
        'notification_send': 'bool',
        'status': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_date': 'createdDate',
        'domain_id': 'domainId',
        'headline': 'headline',
        'id': 'id',
        'image': 'image',
        'last_updated_by': 'lastUpdatedBy',
        'last_updated_date': 'lastUpdatedDate',
        'notification_send': 'notificationSend',
        'status': 'status',
        'url': 'url'
    }

    def __init__(self, created_by=None, created_date=None, domain_id=None, headline=None, id=None, image=None, last_updated_by=None, last_updated_date=None, notification_send=None, status=None, url=None):  # noqa: E501
        """BreakingNews - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_date = None
        self._domain_id = None
        self._headline = None
        self._id = None
        self._image = None
        self._last_updated_by = None
        self._last_updated_date = None
        self._notification_send = None
        self._status = None
        self._url = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if domain_id is not None:
            self.domain_id = domain_id
        if headline is not None:
            self.headline = headline
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if notification_send is not None:
            self.notification_send = notification_send
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url

    @property
    def created_by(self):
        """Gets the created_by of this BreakingNews.  # noqa: E501


        :return: The created_by of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BreakingNews.


        :param created_by: The created_by of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_date(self):
        """Gets the created_date of this BreakingNews.  # noqa: E501


        :return: The created_date of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this BreakingNews.


        :param created_date: The created_date of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def domain_id(self):
        """Gets the domain_id of this BreakingNews.  # noqa: E501


        :return: The domain_id of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this BreakingNews.


        :param domain_id: The domain_id of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def headline(self):
        """Gets the headline of this BreakingNews.  # noqa: E501


        :return: The headline of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this BreakingNews.


        :param headline: The headline of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def id(self):
        """Gets the id of this BreakingNews.  # noqa: E501


        :return: The id of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BreakingNews.


        :param id: The id of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this BreakingNews.  # noqa: E501


        :return: The image of this BreakingNews.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this BreakingNews.


        :param image: The image of this BreakingNews.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this BreakingNews.  # noqa: E501


        :return: The last_updated_by of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this BreakingNews.


        :param last_updated_by: The last_updated_by of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this BreakingNews.  # noqa: E501


        :return: The last_updated_date of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this BreakingNews.


        :param last_updated_date: The last_updated_date of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._last_updated_date = last_updated_date

    @property
    def notification_send(self):
        """Gets the notification_send of this BreakingNews.  # noqa: E501


        :return: The notification_send of this BreakingNews.  # noqa: E501
        :rtype: bool
        """
        return self._notification_send

    @notification_send.setter
    def notification_send(self, notification_send):
        """Sets the notification_send of this BreakingNews.


        :param notification_send: The notification_send of this BreakingNews.  # noqa: E501
        :type: bool
        """

        self._notification_send = notification_send

    @property
    def status(self):
        """Gets the status of this BreakingNews.  # noqa: E501


        :return: The status of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BreakingNews.


        :param status: The status of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def url(self):
        """Gets the url of this BreakingNews.  # noqa: E501


        :return: The url of this BreakingNews.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BreakingNews.


        :param url: The url of this BreakingNews.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(BreakingNews, dict):
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
        if not isinstance(other, BreakingNews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
