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

class WirePublishedStory(object):
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
        'id': 'int',
        'metadata': 'WireMetadata',
        'title': 'str',
        'wire_feed_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domainId',
        'id': 'id',
        'metadata': 'metadata',
        'title': 'title',
        'wire_feed_id': 'wireFeedId'
    }

    def __init__(self, domain_id=None, id=None, metadata=None, title=None, wire_feed_id=None):  # noqa: E501
        """WirePublishedStory - a model defined in Swagger"""  # noqa: E501
        self._domain_id = None
        self._id = None
        self._metadata = None
        self._title = None
        self._wire_feed_id = None
        self.discriminator = None
        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata
        if title is not None:
            self.title = title
        if wire_feed_id is not None:
            self.wire_feed_id = wire_feed_id

    @property
    def domain_id(self):
        """Gets the domain_id of this WirePublishedStory.  # noqa: E501


        :return: The domain_id of this WirePublishedStory.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this WirePublishedStory.


        :param domain_id: The domain_id of this WirePublishedStory.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this WirePublishedStory.  # noqa: E501


        :return: The id of this WirePublishedStory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WirePublishedStory.


        :param id: The id of this WirePublishedStory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this WirePublishedStory.  # noqa: E501


        :return: The metadata of this WirePublishedStory.  # noqa: E501
        :rtype: WireMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WirePublishedStory.


        :param metadata: The metadata of this WirePublishedStory.  # noqa: E501
        :type: WireMetadata
        """

        self._metadata = metadata

    @property
    def title(self):
        """Gets the title of this WirePublishedStory.  # noqa: E501


        :return: The title of this WirePublishedStory.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WirePublishedStory.


        :param title: The title of this WirePublishedStory.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def wire_feed_id(self):
        """Gets the wire_feed_id of this WirePublishedStory.  # noqa: E501


        :return: The wire_feed_id of this WirePublishedStory.  # noqa: E501
        :rtype: str
        """
        return self._wire_feed_id

    @wire_feed_id.setter
    def wire_feed_id(self, wire_feed_id):
        """Sets the wire_feed_id of this WirePublishedStory.


        :param wire_feed_id: The wire_feed_id of this WirePublishedStory.  # noqa: E501
        :type: str
        """

        self._wire_feed_id = wire_feed_id

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
        if issubclass(WirePublishedStory, dict):
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
        if not isinstance(other, WirePublishedStory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
