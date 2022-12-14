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

class StoryAutoSuggestions(object):
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
        'agency_names': 'list[str]',
        'attribution': 'list[str]',
        'authors': 'list[str]',
        'brand_and_models': 'dict(str, list[str])',
        'breaking_news_image_caption': 'str',
        'breaking_news_image_url': 'dict(str, str)',
        'columns': 'list[str]',
        'delete_modes': 'list[str]',
        'preview_urls': 'dict(str, str)',
        'sections': 'dict(str, list[str])',
        'sponsored_titles': 'list[str]',
        'states': 'dict(str, list[str])',
        'sub_sections': 'dict(str, list[str])',
        'topics': 'list[str]',
        'wire_disclaimers': 'list[str]'
    }

    attribute_map = {
        'agency_names': 'agencyNames',
        'attribution': 'attribution',
        'authors': 'authors',
        'brand_and_models': 'brandAndModels',
        'breaking_news_image_caption': 'breakingNewsImageCaption',
        'breaking_news_image_url': 'breakingNewsImageUrl',
        'columns': 'columns',
        'delete_modes': 'deleteModes',
        'preview_urls': 'previewUrls',
        'sections': 'sections',
        'sponsored_titles': 'sponsoredTitles',
        'states': 'states',
        'sub_sections': 'subSections',
        'topics': 'topics',
        'wire_disclaimers': 'wireDisclaimers'
    }

    def __init__(self, agency_names=None, attribution=None, authors=None, brand_and_models=None, breaking_news_image_caption=None, breaking_news_image_url=None, columns=None, delete_modes=None, preview_urls=None, sections=None, sponsored_titles=None, states=None, sub_sections=None, topics=None, wire_disclaimers=None):  # noqa: E501
        """StoryAutoSuggestions - a model defined in Swagger"""  # noqa: E501
        self._agency_names = None
        self._attribution = None
        self._authors = None
        self._brand_and_models = None
        self._breaking_news_image_caption = None
        self._breaking_news_image_url = None
        self._columns = None
        self._delete_modes = None
        self._preview_urls = None
        self._sections = None
        self._sponsored_titles = None
        self._states = None
        self._sub_sections = None
        self._topics = None
        self._wire_disclaimers = None
        self.discriminator = None
        if agency_names is not None:
            self.agency_names = agency_names
        if attribution is not None:
            self.attribution = attribution
        if authors is not None:
            self.authors = authors
        if brand_and_models is not None:
            self.brand_and_models = brand_and_models
        if breaking_news_image_caption is not None:
            self.breaking_news_image_caption = breaking_news_image_caption
        if breaking_news_image_url is not None:
            self.breaking_news_image_url = breaking_news_image_url
        if columns is not None:
            self.columns = columns
        if delete_modes is not None:
            self.delete_modes = delete_modes
        if preview_urls is not None:
            self.preview_urls = preview_urls
        if sections is not None:
            self.sections = sections
        if sponsored_titles is not None:
            self.sponsored_titles = sponsored_titles
        if states is not None:
            self.states = states
        if sub_sections is not None:
            self.sub_sections = sub_sections
        if topics is not None:
            self.topics = topics
        if wire_disclaimers is not None:
            self.wire_disclaimers = wire_disclaimers

    @property
    def agency_names(self):
        """Gets the agency_names of this StoryAutoSuggestions.  # noqa: E501


        :return: The agency_names of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._agency_names

    @agency_names.setter
    def agency_names(self, agency_names):
        """Sets the agency_names of this StoryAutoSuggestions.


        :param agency_names: The agency_names of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._agency_names = agency_names

    @property
    def attribution(self):
        """Gets the attribution of this StoryAutoSuggestions.  # noqa: E501


        :return: The attribution of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this StoryAutoSuggestions.


        :param attribution: The attribution of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._attribution = attribution

    @property
    def authors(self):
        """Gets the authors of this StoryAutoSuggestions.  # noqa: E501


        :return: The authors of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this StoryAutoSuggestions.


        :param authors: The authors of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._authors = authors

    @property
    def brand_and_models(self):
        """Gets the brand_and_models of this StoryAutoSuggestions.  # noqa: E501


        :return: The brand_and_models of this StoryAutoSuggestions.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._brand_and_models

    @brand_and_models.setter
    def brand_and_models(self, brand_and_models):
        """Sets the brand_and_models of this StoryAutoSuggestions.


        :param brand_and_models: The brand_and_models of this StoryAutoSuggestions.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._brand_and_models = brand_and_models

    @property
    def breaking_news_image_caption(self):
        """Gets the breaking_news_image_caption of this StoryAutoSuggestions.  # noqa: E501


        :return: The breaking_news_image_caption of this StoryAutoSuggestions.  # noqa: E501
        :rtype: str
        """
        return self._breaking_news_image_caption

    @breaking_news_image_caption.setter
    def breaking_news_image_caption(self, breaking_news_image_caption):
        """Sets the breaking_news_image_caption of this StoryAutoSuggestions.


        :param breaking_news_image_caption: The breaking_news_image_caption of this StoryAutoSuggestions.  # noqa: E501
        :type: str
        """

        self._breaking_news_image_caption = breaking_news_image_caption

    @property
    def breaking_news_image_url(self):
        """Gets the breaking_news_image_url of this StoryAutoSuggestions.  # noqa: E501


        :return: The breaking_news_image_url of this StoryAutoSuggestions.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._breaking_news_image_url

    @breaking_news_image_url.setter
    def breaking_news_image_url(self, breaking_news_image_url):
        """Sets the breaking_news_image_url of this StoryAutoSuggestions.


        :param breaking_news_image_url: The breaking_news_image_url of this StoryAutoSuggestions.  # noqa: E501
        :type: dict(str, str)
        """

        self._breaking_news_image_url = breaking_news_image_url

    @property
    def columns(self):
        """Gets the columns of this StoryAutoSuggestions.  # noqa: E501


        :return: The columns of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this StoryAutoSuggestions.


        :param columns: The columns of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    @property
    def delete_modes(self):
        """Gets the delete_modes of this StoryAutoSuggestions.  # noqa: E501


        :return: The delete_modes of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._delete_modes

    @delete_modes.setter
    def delete_modes(self, delete_modes):
        """Sets the delete_modes of this StoryAutoSuggestions.


        :param delete_modes: The delete_modes of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["TEMPORARY_REDIRECT", "PERMANENT_REDIRECT"]  # noqa: E501
        if not set(delete_modes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `delete_modes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(delete_modes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._delete_modes = delete_modes

    @property
    def preview_urls(self):
        """Gets the preview_urls of this StoryAutoSuggestions.  # noqa: E501


        :return: The preview_urls of this StoryAutoSuggestions.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._preview_urls

    @preview_urls.setter
    def preview_urls(self, preview_urls):
        """Sets the preview_urls of this StoryAutoSuggestions.


        :param preview_urls: The preview_urls of this StoryAutoSuggestions.  # noqa: E501
        :type: dict(str, str)
        """

        self._preview_urls = preview_urls

    @property
    def sections(self):
        """Gets the sections of this StoryAutoSuggestions.  # noqa: E501


        :return: The sections of this StoryAutoSuggestions.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this StoryAutoSuggestions.


        :param sections: The sections of this StoryAutoSuggestions.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._sections = sections

    @property
    def sponsored_titles(self):
        """Gets the sponsored_titles of this StoryAutoSuggestions.  # noqa: E501


        :return: The sponsored_titles of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._sponsored_titles

    @sponsored_titles.setter
    def sponsored_titles(self, sponsored_titles):
        """Sets the sponsored_titles of this StoryAutoSuggestions.


        :param sponsored_titles: The sponsored_titles of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._sponsored_titles = sponsored_titles

    @property
    def states(self):
        """Gets the states of this StoryAutoSuggestions.  # noqa: E501


        :return: The states of this StoryAutoSuggestions.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this StoryAutoSuggestions.


        :param states: The states of this StoryAutoSuggestions.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._states = states

    @property
    def sub_sections(self):
        """Gets the sub_sections of this StoryAutoSuggestions.  # noqa: E501


        :return: The sub_sections of this StoryAutoSuggestions.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._sub_sections

    @sub_sections.setter
    def sub_sections(self, sub_sections):
        """Sets the sub_sections of this StoryAutoSuggestions.


        :param sub_sections: The sub_sections of this StoryAutoSuggestions.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._sub_sections = sub_sections

    @property
    def topics(self):
        """Gets the topics of this StoryAutoSuggestions.  # noqa: E501


        :return: The topics of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this StoryAutoSuggestions.


        :param topics: The topics of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._topics = topics

    @property
    def wire_disclaimers(self):
        """Gets the wire_disclaimers of this StoryAutoSuggestions.  # noqa: E501


        :return: The wire_disclaimers of this StoryAutoSuggestions.  # noqa: E501
        :rtype: list[str]
        """
        return self._wire_disclaimers

    @wire_disclaimers.setter
    def wire_disclaimers(self, wire_disclaimers):
        """Sets the wire_disclaimers of this StoryAutoSuggestions.


        :param wire_disclaimers: The wire_disclaimers of this StoryAutoSuggestions.  # noqa: E501
        :type: list[str]
        """

        self._wire_disclaimers = wire_disclaimers

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
        if issubclass(StoryAutoSuggestions, dict):
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
        if not isinstance(other, StoryAutoSuggestions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
