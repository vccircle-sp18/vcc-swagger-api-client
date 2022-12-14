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

class ArticleCompact(object):
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
        'article_type': 'str',
        'headline': 'str',
        'id': 'int',
        'last_modified_by': 'str',
        'last_modified_by_user_name': 'str',
        'last_modified_date': 'str',
        'locked_by_user_id': 'str',
        'locked_by_user_name': 'str',
        'metadata': 'MetadataCompact',
        'related': 'list[int]',
        'show_related': 'bool',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'article_type': 'articleType',
        'headline': 'headline',
        'id': 'id',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_by_user_name': 'lastModifiedByUserName',
        'last_modified_date': 'lastModifiedDate',
        'locked_by_user_id': 'lockedByUserId',
        'locked_by_user_name': 'lockedByUserName',
        'metadata': 'metadata',
        'related': 'related',
        'show_related': 'showRelated',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, article_type=None, headline=None, id=None, last_modified_by=None, last_modified_by_user_name=None, last_modified_date=None, locked_by_user_id=None, locked_by_user_name=None, metadata=None, related=None, show_related=None, title=None, type=None):  # noqa: E501
        """ArticleCompact - a model defined in Swagger"""  # noqa: E501
        self._article_type = None
        self._headline = None
        self._id = None
        self._last_modified_by = None
        self._last_modified_by_user_name = None
        self._last_modified_date = None
        self._locked_by_user_id = None
        self._locked_by_user_name = None
        self._metadata = None
        self._related = None
        self._show_related = None
        self._title = None
        self._type = None
        self.discriminator = None
        if article_type is not None:
            self.article_type = article_type
        if headline is not None:
            self.headline = headline
        if id is not None:
            self.id = id
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_by_user_name is not None:
            self.last_modified_by_user_name = last_modified_by_user_name
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if locked_by_user_id is not None:
            self.locked_by_user_id = locked_by_user_id
        if locked_by_user_name is not None:
            self.locked_by_user_name = locked_by_user_name
        if metadata is not None:
            self.metadata = metadata
        if related is not None:
            self.related = related
        if show_related is not None:
            self.show_related = show_related
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def article_type(self):
        """Gets the article_type of this ArticleCompact.  # noqa: E501


        :return: The article_type of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._article_type

    @article_type.setter
    def article_type(self, article_type):
        """Sets the article_type of this ArticleCompact.


        :param article_type: The article_type of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._article_type = article_type

    @property
    def headline(self):
        """Gets the headline of this ArticleCompact.  # noqa: E501


        :return: The headline of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this ArticleCompact.


        :param headline: The headline of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def id(self):
        """Gets the id of this ArticleCompact.  # noqa: E501


        :return: The id of this ArticleCompact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArticleCompact.


        :param id: The id of this ArticleCompact.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ArticleCompact.  # noqa: E501


        :return: The last_modified_by of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ArticleCompact.


        :param last_modified_by: The last_modified_by of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_by_user_name(self):
        """Gets the last_modified_by_user_name of this ArticleCompact.  # noqa: E501


        :return: The last_modified_by_user_name of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by_user_name

    @last_modified_by_user_name.setter
    def last_modified_by_user_name(self, last_modified_by_user_name):
        """Sets the last_modified_by_user_name of this ArticleCompact.


        :param last_modified_by_user_name: The last_modified_by_user_name of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._last_modified_by_user_name = last_modified_by_user_name

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this ArticleCompact.  # noqa: E501


        :return: The last_modified_date of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this ArticleCompact.


        :param last_modified_date: The last_modified_date of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._last_modified_date = last_modified_date

    @property
    def locked_by_user_id(self):
        """Gets the locked_by_user_id of this ArticleCompact.  # noqa: E501


        :return: The locked_by_user_id of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._locked_by_user_id

    @locked_by_user_id.setter
    def locked_by_user_id(self, locked_by_user_id):
        """Sets the locked_by_user_id of this ArticleCompact.


        :param locked_by_user_id: The locked_by_user_id of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._locked_by_user_id = locked_by_user_id

    @property
    def locked_by_user_name(self):
        """Gets the locked_by_user_name of this ArticleCompact.  # noqa: E501


        :return: The locked_by_user_name of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._locked_by_user_name

    @locked_by_user_name.setter
    def locked_by_user_name(self, locked_by_user_name):
        """Sets the locked_by_user_name of this ArticleCompact.


        :param locked_by_user_name: The locked_by_user_name of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._locked_by_user_name = locked_by_user_name

    @property
    def metadata(self):
        """Gets the metadata of this ArticleCompact.  # noqa: E501


        :return: The metadata of this ArticleCompact.  # noqa: E501
        :rtype: MetadataCompact
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ArticleCompact.


        :param metadata: The metadata of this ArticleCompact.  # noqa: E501
        :type: MetadataCompact
        """

        self._metadata = metadata

    @property
    def related(self):
        """Gets the related of this ArticleCompact.  # noqa: E501


        :return: The related of this ArticleCompact.  # noqa: E501
        :rtype: list[int]
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this ArticleCompact.


        :param related: The related of this ArticleCompact.  # noqa: E501
        :type: list[int]
        """

        self._related = related

    @property
    def show_related(self):
        """Gets the show_related of this ArticleCompact.  # noqa: E501


        :return: The show_related of this ArticleCompact.  # noqa: E501
        :rtype: bool
        """
        return self._show_related

    @show_related.setter
    def show_related(self, show_related):
        """Sets the show_related of this ArticleCompact.


        :param show_related: The show_related of this ArticleCompact.  # noqa: E501
        :type: bool
        """

        self._show_related = show_related

    @property
    def title(self):
        """Gets the title of this ArticleCompact.  # noqa: E501


        :return: The title of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ArticleCompact.


        :param title: The title of this ArticleCompact.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this ArticleCompact.  # noqa: E501


        :return: The type of this ArticleCompact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ArticleCompact.


        :param type: The type of this ArticleCompact.  # noqa: E501
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
        if issubclass(ArticleCompact, dict):
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
        if not isinstance(other, ArticleCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
