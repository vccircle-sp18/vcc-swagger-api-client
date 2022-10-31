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

class Embed(object):
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
        'background_color': 'str',
        'body': 'str',
        'body2': 'str',
        'font_color': 'str',
        'label': 'EmbedLabel',
        'label_enabled': 'bool',
        'option': 'dict(str, str)',
        'title': 'str',
        'url': 'str'
    }

    attribute_map = {
        'background_color': 'backgroundColor',
        'body': 'body',
        'body2': 'body2',
        'font_color': 'fontColor',
        'label': 'label',
        'label_enabled': 'labelEnabled',
        'option': 'option',
        'title': 'title',
        'url': 'url'
    }

    def __init__(self, background_color=None, body=None, body2=None, font_color=None, label=None, label_enabled=None, option=None, title=None, url=None):  # noqa: E501
        """Embed - a model defined in Swagger"""  # noqa: E501
        self._background_color = None
        self._body = None
        self._body2 = None
        self._font_color = None
        self._label = None
        self._label_enabled = None
        self._option = None
        self._title = None
        self._url = None
        self.discriminator = None
        if background_color is not None:
            self.background_color = background_color
        if body is not None:
            self.body = body
        if body2 is not None:
            self.body2 = body2
        if font_color is not None:
            self.font_color = font_color
        if label is not None:
            self.label = label
        if label_enabled is not None:
            self.label_enabled = label_enabled
        if option is not None:
            self.option = option
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url

    @property
    def background_color(self):
        """Gets the background_color of this Embed.  # noqa: E501


        :return: The background_color of this Embed.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this Embed.


        :param background_color: The background_color of this Embed.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def body(self):
        """Gets the body of this Embed.  # noqa: E501


        :return: The body of this Embed.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Embed.


        :param body: The body of this Embed.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def body2(self):
        """Gets the body2 of this Embed.  # noqa: E501


        :return: The body2 of this Embed.  # noqa: E501
        :rtype: str
        """
        return self._body2

    @body2.setter
    def body2(self, body2):
        """Sets the body2 of this Embed.


        :param body2: The body2 of this Embed.  # noqa: E501
        :type: str
        """

        self._body2 = body2

    @property
    def font_color(self):
        """Gets the font_color of this Embed.  # noqa: E501


        :return: The font_color of this Embed.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this Embed.


        :param font_color: The font_color of this Embed.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def label(self):
        """Gets the label of this Embed.  # noqa: E501


        :return: The label of this Embed.  # noqa: E501
        :rtype: EmbedLabel
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Embed.


        :param label: The label of this Embed.  # noqa: E501
        :type: EmbedLabel
        """

        self._label = label

    @property
    def label_enabled(self):
        """Gets the label_enabled of this Embed.  # noqa: E501


        :return: The label_enabled of this Embed.  # noqa: E501
        :rtype: bool
        """
        return self._label_enabled

    @label_enabled.setter
    def label_enabled(self, label_enabled):
        """Sets the label_enabled of this Embed.


        :param label_enabled: The label_enabled of this Embed.  # noqa: E501
        :type: bool
        """

        self._label_enabled = label_enabled

    @property
    def option(self):
        """Gets the option of this Embed.  # noqa: E501


        :return: The option of this Embed.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this Embed.


        :param option: The option of this Embed.  # noqa: E501
        :type: dict(str, str)
        """

        self._option = option

    @property
    def title(self):
        """Gets the title of this Embed.  # noqa: E501


        :return: The title of this Embed.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Embed.


        :param title: The title of this Embed.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this Embed.  # noqa: E501


        :return: The url of this Embed.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Embed.


        :param url: The url of this Embed.  # noqa: E501
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
        if issubclass(Embed, dict):
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
        if not isinstance(other, Embed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other