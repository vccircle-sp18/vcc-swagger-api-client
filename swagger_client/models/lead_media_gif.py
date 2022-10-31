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

class LeadMediaGif(object):
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
        'elements': 'list[int]',
        'id': 'int',
        'image': 'Image',
        'media_type': 'str'
    }

    attribute_map = {
        'elements': 'elements',
        'id': 'id',
        'image': 'image',
        'media_type': 'mediaType'
    }

    def __init__(self, elements=None, id=None, image=None, media_type=None):  # noqa: E501
        """LeadMediaGif - a model defined in Swagger"""  # noqa: E501
        self._elements = None
        self._id = None
        self._image = None
        self._media_type = None
        self.discriminator = None
        if elements is not None:
            self.elements = elements
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if media_type is not None:
            self.media_type = media_type

    @property
    def elements(self):
        """Gets the elements of this LeadMediaGif.  # noqa: E501


        :return: The elements of this LeadMediaGif.  # noqa: E501
        :rtype: list[int]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this LeadMediaGif.


        :param elements: The elements of this LeadMediaGif.  # noqa: E501
        :type: list[int]
        """

        self._elements = elements

    @property
    def id(self):
        """Gets the id of this LeadMediaGif.  # noqa: E501


        :return: The id of this LeadMediaGif.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LeadMediaGif.


        :param id: The id of this LeadMediaGif.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this LeadMediaGif.  # noqa: E501


        :return: The image of this LeadMediaGif.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this LeadMediaGif.


        :param image: The image of this LeadMediaGif.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def media_type(self):
        """Gets the media_type of this LeadMediaGif.  # noqa: E501


        :return: The media_type of this LeadMediaGif.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this LeadMediaGif.


        :param media_type: The media_type of this LeadMediaGif.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

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
        if issubclass(LeadMediaGif, dict):
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
        if not isinstance(other, LeadMediaGif):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
