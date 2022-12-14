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

class MetadataCompact(object):
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
        'methode_file_name': 'str',
        'section': 'str',
        'section_id': 'int',
        'sub_section': 'str',
        'sub_section_id': 'int',
        'sub_section_l2': 'str',
        'sub_section_l2_id': 'int',
        'topic': 'list[str]',
        'topic_ids': 'list[int]',
        'url': 'str'
    }

    attribute_map = {
        'methode_file_name': 'methodeFileName',
        'section': 'section',
        'section_id': 'sectionId',
        'sub_section': 'subSection',
        'sub_section_id': 'subSectionId',
        'sub_section_l2': 'subSectionL2',
        'sub_section_l2_id': 'subSectionL2Id',
        'topic': 'topic',
        'topic_ids': 'topicIds',
        'url': 'url'
    }

    def __init__(self, methode_file_name=None, section=None, section_id=None, sub_section=None, sub_section_id=None, sub_section_l2=None, sub_section_l2_id=None, topic=None, topic_ids=None, url=None):  # noqa: E501
        """MetadataCompact - a model defined in Swagger"""  # noqa: E501
        self._methode_file_name = None
        self._section = None
        self._section_id = None
        self._sub_section = None
        self._sub_section_id = None
        self._sub_section_l2 = None
        self._sub_section_l2_id = None
        self._topic = None
        self._topic_ids = None
        self._url = None
        self.discriminator = None
        if methode_file_name is not None:
            self.methode_file_name = methode_file_name
        if section is not None:
            self.section = section
        if section_id is not None:
            self.section_id = section_id
        if sub_section is not None:
            self.sub_section = sub_section
        if sub_section_id is not None:
            self.sub_section_id = sub_section_id
        if sub_section_l2 is not None:
            self.sub_section_l2 = sub_section_l2
        if sub_section_l2_id is not None:
            self.sub_section_l2_id = sub_section_l2_id
        if topic is not None:
            self.topic = topic
        if topic_ids is not None:
            self.topic_ids = topic_ids
        if url is not None:
            self.url = url

    @property
    def methode_file_name(self):
        """Gets the methode_file_name of this MetadataCompact.  # noqa: E501


        :return: The methode_file_name of this MetadataCompact.  # noqa: E501
        :rtype: str
        """
        return self._methode_file_name

    @methode_file_name.setter
    def methode_file_name(self, methode_file_name):
        """Sets the methode_file_name of this MetadataCompact.


        :param methode_file_name: The methode_file_name of this MetadataCompact.  # noqa: E501
        :type: str
        """

        self._methode_file_name = methode_file_name

    @property
    def section(self):
        """Gets the section of this MetadataCompact.  # noqa: E501


        :return: The section of this MetadataCompact.  # noqa: E501
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this MetadataCompact.


        :param section: The section of this MetadataCompact.  # noqa: E501
        :type: str
        """

        self._section = section

    @property
    def section_id(self):
        """Gets the section_id of this MetadataCompact.  # noqa: E501


        :return: The section_id of this MetadataCompact.  # noqa: E501
        :rtype: int
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        """Sets the section_id of this MetadataCompact.


        :param section_id: The section_id of this MetadataCompact.  # noqa: E501
        :type: int
        """

        self._section_id = section_id

    @property
    def sub_section(self):
        """Gets the sub_section of this MetadataCompact.  # noqa: E501


        :return: The sub_section of this MetadataCompact.  # noqa: E501
        :rtype: str
        """
        return self._sub_section

    @sub_section.setter
    def sub_section(self, sub_section):
        """Sets the sub_section of this MetadataCompact.


        :param sub_section: The sub_section of this MetadataCompact.  # noqa: E501
        :type: str
        """

        self._sub_section = sub_section

    @property
    def sub_section_id(self):
        """Gets the sub_section_id of this MetadataCompact.  # noqa: E501


        :return: The sub_section_id of this MetadataCompact.  # noqa: E501
        :rtype: int
        """
        return self._sub_section_id

    @sub_section_id.setter
    def sub_section_id(self, sub_section_id):
        """Sets the sub_section_id of this MetadataCompact.


        :param sub_section_id: The sub_section_id of this MetadataCompact.  # noqa: E501
        :type: int
        """

        self._sub_section_id = sub_section_id

    @property
    def sub_section_l2(self):
        """Gets the sub_section_l2 of this MetadataCompact.  # noqa: E501


        :return: The sub_section_l2 of this MetadataCompact.  # noqa: E501
        :rtype: str
        """
        return self._sub_section_l2

    @sub_section_l2.setter
    def sub_section_l2(self, sub_section_l2):
        """Sets the sub_section_l2 of this MetadataCompact.


        :param sub_section_l2: The sub_section_l2 of this MetadataCompact.  # noqa: E501
        :type: str
        """

        self._sub_section_l2 = sub_section_l2

    @property
    def sub_section_l2_id(self):
        """Gets the sub_section_l2_id of this MetadataCompact.  # noqa: E501


        :return: The sub_section_l2_id of this MetadataCompact.  # noqa: E501
        :rtype: int
        """
        return self._sub_section_l2_id

    @sub_section_l2_id.setter
    def sub_section_l2_id(self, sub_section_l2_id):
        """Sets the sub_section_l2_id of this MetadataCompact.


        :param sub_section_l2_id: The sub_section_l2_id of this MetadataCompact.  # noqa: E501
        :type: int
        """

        self._sub_section_l2_id = sub_section_l2_id

    @property
    def topic(self):
        """Gets the topic of this MetadataCompact.  # noqa: E501


        :return: The topic of this MetadataCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this MetadataCompact.


        :param topic: The topic of this MetadataCompact.  # noqa: E501
        :type: list[str]
        """

        self._topic = topic

    @property
    def topic_ids(self):
        """Gets the topic_ids of this MetadataCompact.  # noqa: E501


        :return: The topic_ids of this MetadataCompact.  # noqa: E501
        :rtype: list[int]
        """
        return self._topic_ids

    @topic_ids.setter
    def topic_ids(self, topic_ids):
        """Sets the topic_ids of this MetadataCompact.


        :param topic_ids: The topic_ids of this MetadataCompact.  # noqa: E501
        :type: list[int]
        """

        self._topic_ids = topic_ids

    @property
    def url(self):
        """Gets the url of this MetadataCompact.  # noqa: E501


        :return: The url of this MetadataCompact.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MetadataCompact.


        :param url: The url of this MetadataCompact.  # noqa: E501
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
        if issubclass(MetadataCompact, dict):
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
        if not isinstance(other, MetadataCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
