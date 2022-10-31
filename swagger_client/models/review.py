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

class Review(object):
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
        'brand_name': 'str',
        'cons': 'list[str]',
        'price': 'str',
        'product_name': 'str',
        'pros': 'list[str]',
        'rating': 'float',
        'short_verdict': 'str',
        'specification': 'list[DynamicConfiguration]'
    }

    attribute_map = {
        'brand_name': 'brandName',
        'cons': 'cons',
        'price': 'price',
        'product_name': 'productName',
        'pros': 'pros',
        'rating': 'rating',
        'short_verdict': 'shortVerdict',
        'specification': 'specification'
    }

    def __init__(self, brand_name=None, cons=None, price=None, product_name=None, pros=None, rating=None, short_verdict=None, specification=None):  # noqa: E501
        """Review - a model defined in Swagger"""  # noqa: E501
        self._brand_name = None
        self._cons = None
        self._price = None
        self._product_name = None
        self._pros = None
        self._rating = None
        self._short_verdict = None
        self._specification = None
        self.discriminator = None
        if brand_name is not None:
            self.brand_name = brand_name
        if cons is not None:
            self.cons = cons
        if price is not None:
            self.price = price
        if product_name is not None:
            self.product_name = product_name
        if pros is not None:
            self.pros = pros
        if rating is not None:
            self.rating = rating
        if short_verdict is not None:
            self.short_verdict = short_verdict
        if specification is not None:
            self.specification = specification

    @property
    def brand_name(self):
        """Gets the brand_name of this Review.  # noqa: E501


        :return: The brand_name of this Review.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this Review.


        :param brand_name: The brand_name of this Review.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    @property
    def cons(self):
        """Gets the cons of this Review.  # noqa: E501


        :return: The cons of this Review.  # noqa: E501
        :rtype: list[str]
        """
        return self._cons

    @cons.setter
    def cons(self, cons):
        """Sets the cons of this Review.


        :param cons: The cons of this Review.  # noqa: E501
        :type: list[str]
        """

        self._cons = cons

    @property
    def price(self):
        """Gets the price of this Review.  # noqa: E501


        :return: The price of this Review.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Review.


        :param price: The price of this Review.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def product_name(self):
        """Gets the product_name of this Review.  # noqa: E501


        :return: The product_name of this Review.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this Review.


        :param product_name: The product_name of this Review.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def pros(self):
        """Gets the pros of this Review.  # noqa: E501


        :return: The pros of this Review.  # noqa: E501
        :rtype: list[str]
        """
        return self._pros

    @pros.setter
    def pros(self, pros):
        """Sets the pros of this Review.


        :param pros: The pros of this Review.  # noqa: E501
        :type: list[str]
        """

        self._pros = pros

    @property
    def rating(self):
        """Gets the rating of this Review.  # noqa: E501


        :return: The rating of this Review.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Review.


        :param rating: The rating of this Review.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def short_verdict(self):
        """Gets the short_verdict of this Review.  # noqa: E501


        :return: The short_verdict of this Review.  # noqa: E501
        :rtype: str
        """
        return self._short_verdict

    @short_verdict.setter
    def short_verdict(self, short_verdict):
        """Sets the short_verdict of this Review.


        :param short_verdict: The short_verdict of this Review.  # noqa: E501
        :type: str
        """

        self._short_verdict = short_verdict

    @property
    def specification(self):
        """Gets the specification of this Review.  # noqa: E501


        :return: The specification of this Review.  # noqa: E501
        :rtype: list[DynamicConfiguration]
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this Review.


        :param specification: The specification of this Review.  # noqa: E501
        :type: list[DynamicConfiguration]
        """

        self._specification = specification

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
        if issubclass(Review, dict):
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
        if not isinstance(other, Review):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
