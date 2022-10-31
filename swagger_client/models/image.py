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

class Image(object):
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
        'alternate_text': 'str',
        'anchor_tag': 'str',
        'caption': 'str',
        'image_credit': 'str',
        'images': 'dict(str, str)',
        'name': 'str',
        'vertical_image': 'bool',
        'watermarked_img': 'bool'
    }

    attribute_map = {
        'alternate_text': 'alternateText',
        'anchor_tag': 'anchorTag',
        'caption': 'caption',
        'image_credit': 'imageCredit',
        'images': 'images',
        'name': 'name',
        'vertical_image': 'verticalImage',
        'watermarked_img': 'watermarkedImg'
    }

    def __init__(self, alternate_text=None, anchor_tag=None, caption=None, image_credit=None, images=None, name=None, vertical_image=None, watermarked_img=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        self._alternate_text = None
        self._anchor_tag = None
        self._caption = None
        self._image_credit = None
        self._images = None
        self._name = None
        self._vertical_image = None
        self._watermarked_img = None
        self.discriminator = None
        if alternate_text is not None:
            self.alternate_text = alternate_text
        if anchor_tag is not None:
            self.anchor_tag = anchor_tag
        if caption is not None:
            self.caption = caption
        if image_credit is not None:
            self.image_credit = image_credit
        if images is not None:
            self.images = images
        if name is not None:
            self.name = name
        if vertical_image is not None:
            self.vertical_image = vertical_image
        if watermarked_img is not None:
            self.watermarked_img = watermarked_img

    @property
    def alternate_text(self):
        """Gets the alternate_text of this Image.  # noqa: E501


        :return: The alternate_text of this Image.  # noqa: E501
        :rtype: str
        """
        return self._alternate_text

    @alternate_text.setter
    def alternate_text(self, alternate_text):
        """Sets the alternate_text of this Image.


        :param alternate_text: The alternate_text of this Image.  # noqa: E501
        :type: str
        """

        self._alternate_text = alternate_text

    @property
    def anchor_tag(self):
        """Gets the anchor_tag of this Image.  # noqa: E501


        :return: The anchor_tag of this Image.  # noqa: E501
        :rtype: str
        """
        return self._anchor_tag

    @anchor_tag.setter
    def anchor_tag(self, anchor_tag):
        """Sets the anchor_tag of this Image.


        :param anchor_tag: The anchor_tag of this Image.  # noqa: E501
        :type: str
        """

        self._anchor_tag = anchor_tag

    @property
    def caption(self):
        """Gets the caption of this Image.  # noqa: E501


        :return: The caption of this Image.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this Image.


        :param caption: The caption of this Image.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def image_credit(self):
        """Gets the image_credit of this Image.  # noqa: E501


        :return: The image_credit of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_credit

    @image_credit.setter
    def image_credit(self, image_credit):
        """Sets the image_credit of this Image.


        :param image_credit: The image_credit of this Image.  # noqa: E501
        :type: str
        """

        self._image_credit = image_credit

    @property
    def images(self):
        """Gets the images of this Image.  # noqa: E501


        :return: The images of this Image.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Image.


        :param images: The images of this Image.  # noqa: E501
        :type: dict(str, str)
        """

        self._images = images

    @property
    def name(self):
        """Gets the name of this Image.  # noqa: E501


        :return: The name of this Image.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Image.


        :param name: The name of this Image.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vertical_image(self):
        """Gets the vertical_image of this Image.  # noqa: E501


        :return: The vertical_image of this Image.  # noqa: E501
        :rtype: bool
        """
        return self._vertical_image

    @vertical_image.setter
    def vertical_image(self, vertical_image):
        """Sets the vertical_image of this Image.


        :param vertical_image: The vertical_image of this Image.  # noqa: E501
        :type: bool
        """

        self._vertical_image = vertical_image

    @property
    def watermarked_img(self):
        """Gets the watermarked_img of this Image.  # noqa: E501


        :return: The watermarked_img of this Image.  # noqa: E501
        :rtype: bool
        """
        return self._watermarked_img

    @watermarked_img.setter
    def watermarked_img(self, watermarked_img):
        """Sets the watermarked_img of this Image.


        :param watermarked_img: The watermarked_img of this Image.  # noqa: E501
        :type: bool
        """

        self._watermarked_img = watermarked_img

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other