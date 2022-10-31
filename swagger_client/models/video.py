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

class Video(object):
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
        'body': 'str',
        'caption': 'str',
        'embed_url': 'str',
        'image': 'Image',
        'url': 'str',
        'youtube_embed_body': 'str',
        'youtube_embed_url': 'str'
    }

    attribute_map = {
        'body': 'body',
        'caption': 'caption',
        'embed_url': 'embedUrl',
        'image': 'image',
        'url': 'url',
        'youtube_embed_body': 'youtubeEmbedBody',
        'youtube_embed_url': 'youtubeEmbedUrl'
    }

    def __init__(self, body=None, caption=None, embed_url=None, image=None, url=None, youtube_embed_body=None, youtube_embed_url=None):  # noqa: E501
        """Video - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._caption = None
        self._embed_url = None
        self._image = None
        self._url = None
        self._youtube_embed_body = None
        self._youtube_embed_url = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if caption is not None:
            self.caption = caption
        if embed_url is not None:
            self.embed_url = embed_url
        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if youtube_embed_body is not None:
            self.youtube_embed_body = youtube_embed_body
        if youtube_embed_url is not None:
            self.youtube_embed_url = youtube_embed_url

    @property
    def body(self):
        """Gets the body of this Video.  # noqa: E501


        :return: The body of this Video.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Video.


        :param body: The body of this Video.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def caption(self):
        """Gets the caption of this Video.  # noqa: E501


        :return: The caption of this Video.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this Video.


        :param caption: The caption of this Video.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def embed_url(self):
        """Gets the embed_url of this Video.  # noqa: E501


        :return: The embed_url of this Video.  # noqa: E501
        :rtype: str
        """
        return self._embed_url

    @embed_url.setter
    def embed_url(self, embed_url):
        """Sets the embed_url of this Video.


        :param embed_url: The embed_url of this Video.  # noqa: E501
        :type: str
        """

        self._embed_url = embed_url

    @property
    def image(self):
        """Gets the image of this Video.  # noqa: E501


        :return: The image of this Video.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Video.


        :param image: The image of this Video.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def url(self):
        """Gets the url of this Video.  # noqa: E501


        :return: The url of this Video.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Video.


        :param url: The url of this Video.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def youtube_embed_body(self):
        """Gets the youtube_embed_body of this Video.  # noqa: E501


        :return: The youtube_embed_body of this Video.  # noqa: E501
        :rtype: str
        """
        return self._youtube_embed_body

    @youtube_embed_body.setter
    def youtube_embed_body(self, youtube_embed_body):
        """Sets the youtube_embed_body of this Video.


        :param youtube_embed_body: The youtube_embed_body of this Video.  # noqa: E501
        :type: str
        """

        self._youtube_embed_body = youtube_embed_body

    @property
    def youtube_embed_url(self):
        """Gets the youtube_embed_url of this Video.  # noqa: E501


        :return: The youtube_embed_url of this Video.  # noqa: E501
        :rtype: str
        """
        return self._youtube_embed_url

    @youtube_embed_url.setter
    def youtube_embed_url(self, youtube_embed_url):
        """Sets the youtube_embed_url of this Video.


        :param youtube_embed_url: The youtube_embed_url of this Video.  # noqa: E501
        :type: str
        """

        self._youtube_embed_url = youtube_embed_url

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
        if issubclass(Video, dict):
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
        if not isinstance(other, Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other