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

class Listicle(object):
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
        'inline_element_id': 'int',
        'product': 'Product',
        'title': 'str'
    }

    attribute_map = {
        'body': 'body',
        'inline_element_id': 'inlineElementId',
        'product': 'product',
        'title': 'title'
    }

    def __init__(self, body=None, inline_element_id=None, product=None, title=None):  # noqa: E501
        """Listicle - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._inline_element_id = None
        self._product = None
        self._title = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if inline_element_id is not None:
            self.inline_element_id = inline_element_id
        if product is not None:
            self.product = product
        if title is not None:
            self.title = title

    @property
    def body(self):
        """Gets the body of this Listicle.  # noqa: E501


        :return: The body of this Listicle.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Listicle.


        :param body: The body of this Listicle.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def inline_element_id(self):
        """Gets the inline_element_id of this Listicle.  # noqa: E501


        :return: The inline_element_id of this Listicle.  # noqa: E501
        :rtype: int
        """
        return self._inline_element_id

    @inline_element_id.setter
    def inline_element_id(self, inline_element_id):
        """Sets the inline_element_id of this Listicle.


        :param inline_element_id: The inline_element_id of this Listicle.  # noqa: E501
        :type: int
        """

        self._inline_element_id = inline_element_id

    @property
    def product(self):
        """Gets the product of this Listicle.  # noqa: E501


        :return: The product of this Listicle.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Listicle.


        :param product: The product of this Listicle.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def title(self):
        """Gets the title of this Listicle.  # noqa: E501


        :return: The title of this Listicle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Listicle.


        :param title: The title of this Listicle.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(Listicle, dict):
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
        if not isinstance(other, Listicle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
