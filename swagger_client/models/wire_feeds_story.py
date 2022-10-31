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

class WireFeedsStory(object):
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
        'author': 'str',
        'auto_publish': 'bool',
        'content': 'str',
        'images': 'list[str]',
        'last_modified_date': 'str',
        'last_modified_date_timestamp': 'int',
        'lead_media': 'LeadMedia',
        'list_images': 'list[WireImage]',
        'metadata': 'Metadata',
        'revision_id': 'int',
        'source': 'str',
        'sub_category': 'str',
        'summary': 'str'
    }

    attribute_map = {
        'author': 'author',
        'auto_publish': 'autoPublish',
        'content': 'content',
        'images': 'images',
        'last_modified_date': 'lastModifiedDate',
        'last_modified_date_timestamp': 'lastModifiedDateTimestamp',
        'lead_media': 'leadMedia',
        'list_images': 'listImages',
        'metadata': 'metadata',
        'revision_id': 'revisionId',
        'source': 'source',
        'sub_category': 'subCategory',
        'summary': 'summary'
    }

    def __init__(self, author=None, auto_publish=None, content=None, images=None, last_modified_date=None, last_modified_date_timestamp=None, lead_media=None, list_images=None, metadata=None, revision_id=None, source=None, sub_category=None, summary=None):  # noqa: E501
        """WireFeedsStory - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._auto_publish = None
        self._content = None
        self._images = None
        self._last_modified_date = None
        self._last_modified_date_timestamp = None
        self._lead_media = None
        self._list_images = None
        self._metadata = None
        self._revision_id = None
        self._source = None
        self._sub_category = None
        self._summary = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if auto_publish is not None:
            self.auto_publish = auto_publish
        if content is not None:
            self.content = content
        if images is not None:
            self.images = images
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_date_timestamp is not None:
            self.last_modified_date_timestamp = last_modified_date_timestamp
        if lead_media is not None:
            self.lead_media = lead_media
        if list_images is not None:
            self.list_images = list_images
        if metadata is not None:
            self.metadata = metadata
        if revision_id is not None:
            self.revision_id = revision_id
        if source is not None:
            self.source = source
        if sub_category is not None:
            self.sub_category = sub_category
        if summary is not None:
            self.summary = summary

    @property
    def author(self):
        """Gets the author of this WireFeedsStory.  # noqa: E501


        :return: The author of this WireFeedsStory.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this WireFeedsStory.


        :param author: The author of this WireFeedsStory.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def auto_publish(self):
        """Gets the auto_publish of this WireFeedsStory.  # noqa: E501


        :return: The auto_publish of this WireFeedsStory.  # noqa: E501
        :rtype: bool
        """
        return self._auto_publish

    @auto_publish.setter
    def auto_publish(self, auto_publish):
        """Sets the auto_publish of this WireFeedsStory.


        :param auto_publish: The auto_publish of this WireFeedsStory.  # noqa: E501
        :type: bool
        """

        self._auto_publish = auto_publish

    @property
    def content(self):
        """Gets the content of this WireFeedsStory.  # noqa: E501


        :return: The content of this WireFeedsStory.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this WireFeedsStory.


        :param content: The content of this WireFeedsStory.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def images(self):
        """Gets the images of this WireFeedsStory.  # noqa: E501


        :return: The images of this WireFeedsStory.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this WireFeedsStory.


        :param images: The images of this WireFeedsStory.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this WireFeedsStory.  # noqa: E501


        :return: The last_modified_date of this WireFeedsStory.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this WireFeedsStory.


        :param last_modified_date: The last_modified_date of this WireFeedsStory.  # noqa: E501
        :type: str
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_date_timestamp(self):
        """Gets the last_modified_date_timestamp of this WireFeedsStory.  # noqa: E501


        :return: The last_modified_date_timestamp of this WireFeedsStory.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_date_timestamp

    @last_modified_date_timestamp.setter
    def last_modified_date_timestamp(self, last_modified_date_timestamp):
        """Sets the last_modified_date_timestamp of this WireFeedsStory.


        :param last_modified_date_timestamp: The last_modified_date_timestamp of this WireFeedsStory.  # noqa: E501
        :type: int
        """

        self._last_modified_date_timestamp = last_modified_date_timestamp

    @property
    def lead_media(self):
        """Gets the lead_media of this WireFeedsStory.  # noqa: E501


        :return: The lead_media of this WireFeedsStory.  # noqa: E501
        :rtype: LeadMedia
        """
        return self._lead_media

    @lead_media.setter
    def lead_media(self, lead_media):
        """Sets the lead_media of this WireFeedsStory.


        :param lead_media: The lead_media of this WireFeedsStory.  # noqa: E501
        :type: LeadMedia
        """

        self._lead_media = lead_media

    @property
    def list_images(self):
        """Gets the list_images of this WireFeedsStory.  # noqa: E501


        :return: The list_images of this WireFeedsStory.  # noqa: E501
        :rtype: list[WireImage]
        """
        return self._list_images

    @list_images.setter
    def list_images(self, list_images):
        """Sets the list_images of this WireFeedsStory.


        :param list_images: The list_images of this WireFeedsStory.  # noqa: E501
        :type: list[WireImage]
        """

        self._list_images = list_images

    @property
    def metadata(self):
        """Gets the metadata of this WireFeedsStory.  # noqa: E501


        :return: The metadata of this WireFeedsStory.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WireFeedsStory.


        :param metadata: The metadata of this WireFeedsStory.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def revision_id(self):
        """Gets the revision_id of this WireFeedsStory.  # noqa: E501


        :return: The revision_id of this WireFeedsStory.  # noqa: E501
        :rtype: int
        """
        return self._revision_id

    @revision_id.setter
    def revision_id(self, revision_id):
        """Sets the revision_id of this WireFeedsStory.


        :param revision_id: The revision_id of this WireFeedsStory.  # noqa: E501
        :type: int
        """

        self._revision_id = revision_id

    @property
    def source(self):
        """Gets the source of this WireFeedsStory.  # noqa: E501


        :return: The source of this WireFeedsStory.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this WireFeedsStory.


        :param source: The source of this WireFeedsStory.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def sub_category(self):
        """Gets the sub_category of this WireFeedsStory.  # noqa: E501


        :return: The sub_category of this WireFeedsStory.  # noqa: E501
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this WireFeedsStory.


        :param sub_category: The sub_category of this WireFeedsStory.  # noqa: E501
        :type: str
        """

        self._sub_category = sub_category

    @property
    def summary(self):
        """Gets the summary of this WireFeedsStory.  # noqa: E501


        :return: The summary of this WireFeedsStory.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this WireFeedsStory.


        :param summary: The summary of this WireFeedsStory.  # noqa: E501
        :type: str
        """

        self._summary = summary

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
        if issubclass(WireFeedsStory, dict):
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
        if not isinstance(other, WireFeedsStory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other