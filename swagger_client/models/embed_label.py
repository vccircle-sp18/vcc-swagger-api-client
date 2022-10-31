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

class EmbedLabel(object):
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
        'font_color': 'str',
        'text': 'str'
    }

    attribute_map = {
        'background_color': 'backgroundColor',
        'font_color': 'fontColor',
        'text': 'text'
    }

    def __init__(self, background_color=None, font_color=None, text=None):  # noqa: E501
        """EmbedLabel - a model defined in Swagger"""  # noqa: E501
        self._background_color = None
        self._font_color = None
        self._text = None
        self.discriminator = None
        if background_color is not None:
            self.background_color = background_color
        if font_color is not None:
            self.font_color = font_color
        if text is not None:
            self.text = text

    @property
    def background_color(self):
        """Gets the background_color of this EmbedLabel.  # noqa: E501


        :return: The background_color of this EmbedLabel.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this EmbedLabel.


        :param background_color: The background_color of this EmbedLabel.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def font_color(self):
        """Gets the font_color of this EmbedLabel.  # noqa: E501


        :return: The font_color of this EmbedLabel.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this EmbedLabel.


        :param font_color: The font_color of this EmbedLabel.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def text(self):
        """Gets the text of this EmbedLabel.  # noqa: E501


        :return: The text of this EmbedLabel.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EmbedLabel.


        :param text: The text of this EmbedLabel.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(EmbedLabel, dict):
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
        if not isinstance(other, EmbedLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
