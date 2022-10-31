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

class WebStoriesTextboxOrButton(object):
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
        'border': 'bool',
        'border_bottom': 'bool',
        'border_color': 'str',
        'border_left': 'bool',
        'border_right': 'bool',
        'border_style': 'str',
        'border_top': 'bool',
        'bottom': 'bool',
        'bottom_alignment': 'bool',
        'bottom_margin': 'str',
        'bottom_padding': 'str',
        'corner_radius': 'str',
        'font_color': 'str',
        'font_family': 'str',
        'font_size': 'str',
        'font_style': 'str',
        'left': 'bool',
        'left_alignment': 'bool',
        'left_margin': 'str',
        'left_right_center': 'bool',
        'position': 'str',
        'right': 'bool',
        'right_alignment': 'bool',
        'right_margin': 'str',
        'text': 'str',
        'text_alignment': 'str',
        'text_transform': 'str',
        'textbox_css': 'object',
        'top': 'bool',
        'top_alignment': 'bool',
        'top_bottom_center': 'bool',
        'top_margin': 'str',
        'top_padding': 'str',
        'type': 'str',
        'url': 'str',
        'width': 'str'
    }

    attribute_map = {
        'background_color': 'backgroundColor',
        'border': 'border',
        'border_bottom': 'borderBottom',
        'border_color': 'borderColor',
        'border_left': 'borderLeft',
        'border_right': 'borderRight',
        'border_style': 'borderStyle',
        'border_top': 'borderTop',
        'bottom': 'bottom',
        'bottom_alignment': 'bottomAlignment',
        'bottom_margin': 'bottomMargin',
        'bottom_padding': 'bottomPadding',
        'corner_radius': 'cornerRadius',
        'font_color': 'fontColor',
        'font_family': 'fontFamily',
        'font_size': 'fontSize',
        'font_style': 'fontStyle',
        'left': 'left',
        'left_alignment': 'leftAlignment',
        'left_margin': 'leftMargin',
        'left_right_center': 'leftRightCenter',
        'position': 'position',
        'right': 'right',
        'right_alignment': 'rightAlignment',
        'right_margin': 'rightMargin',
        'text': 'text',
        'text_alignment': 'textAlignment',
        'text_transform': 'textTransform',
        'textbox_css': 'textboxCSS',
        'top': 'top',
        'top_alignment': 'topAlignment',
        'top_bottom_center': 'topBottomCenter',
        'top_margin': 'topMargin',
        'top_padding': 'topPadding',
        'type': 'type',
        'url': 'url',
        'width': 'width'
    }

    def __init__(self, background_color=None, border=None, border_bottom=None, border_color=None, border_left=None, border_right=None, border_style=None, border_top=None, bottom=None, bottom_alignment=None, bottom_margin=None, bottom_padding=None, corner_radius=None, font_color=None, font_family=None, font_size=None, font_style=None, left=None, left_alignment=None, left_margin=None, left_right_center=None, position=None, right=None, right_alignment=None, right_margin=None, text=None, text_alignment=None, text_transform=None, textbox_css=None, top=None, top_alignment=None, top_bottom_center=None, top_margin=None, top_padding=None, type=None, url=None, width=None):  # noqa: E501
        """WebStoriesTextboxOrButton - a model defined in Swagger"""  # noqa: E501
        self._background_color = None
        self._border = None
        self._border_bottom = None
        self._border_color = None
        self._border_left = None
        self._border_right = None
        self._border_style = None
        self._border_top = None
        self._bottom = None
        self._bottom_alignment = None
        self._bottom_margin = None
        self._bottom_padding = None
        self._corner_radius = None
        self._font_color = None
        self._font_family = None
        self._font_size = None
        self._font_style = None
        self._left = None
        self._left_alignment = None
        self._left_margin = None
        self._left_right_center = None
        self._position = None
        self._right = None
        self._right_alignment = None
        self._right_margin = None
        self._text = None
        self._text_alignment = None
        self._text_transform = None
        self._textbox_css = None
        self._top = None
        self._top_alignment = None
        self._top_bottom_center = None
        self._top_margin = None
        self._top_padding = None
        self._type = None
        self._url = None
        self._width = None
        self.discriminator = None
        if background_color is not None:
            self.background_color = background_color
        if border is not None:
            self.border = border
        if border_bottom is not None:
            self.border_bottom = border_bottom
        if border_color is not None:
            self.border_color = border_color
        if border_left is not None:
            self.border_left = border_left
        if border_right is not None:
            self.border_right = border_right
        if border_style is not None:
            self.border_style = border_style
        if border_top is not None:
            self.border_top = border_top
        if bottom is not None:
            self.bottom = bottom
        if bottom_alignment is not None:
            self.bottom_alignment = bottom_alignment
        if bottom_margin is not None:
            self.bottom_margin = bottom_margin
        if bottom_padding is not None:
            self.bottom_padding = bottom_padding
        if corner_radius is not None:
            self.corner_radius = corner_radius
        if font_color is not None:
            self.font_color = font_color
        if font_family is not None:
            self.font_family = font_family
        if font_size is not None:
            self.font_size = font_size
        if font_style is not None:
            self.font_style = font_style
        if left is not None:
            self.left = left
        if left_alignment is not None:
            self.left_alignment = left_alignment
        if left_margin is not None:
            self.left_margin = left_margin
        if left_right_center is not None:
            self.left_right_center = left_right_center
        if position is not None:
            self.position = position
        if right is not None:
            self.right = right
        if right_alignment is not None:
            self.right_alignment = right_alignment
        if right_margin is not None:
            self.right_margin = right_margin
        if text is not None:
            self.text = text
        if text_alignment is not None:
            self.text_alignment = text_alignment
        if text_transform is not None:
            self.text_transform = text_transform
        if textbox_css is not None:
            self.textbox_css = textbox_css
        if top is not None:
            self.top = top
        if top_alignment is not None:
            self.top_alignment = top_alignment
        if top_bottom_center is not None:
            self.top_bottom_center = top_bottom_center
        if top_margin is not None:
            self.top_margin = top_margin
        if top_padding is not None:
            self.top_padding = top_padding
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if width is not None:
            self.width = width

    @property
    def background_color(self):
        """Gets the background_color of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The background_color of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this WebStoriesTextboxOrButton.


        :param background_color: The background_color of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def border(self):
        """Gets the border of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._border

    @border.setter
    def border(self, border):
        """Sets the border of this WebStoriesTextboxOrButton.


        :param border: The border of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._border = border

    @property
    def border_bottom(self):
        """Gets the border_bottom of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border_bottom of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._border_bottom

    @border_bottom.setter
    def border_bottom(self, border_bottom):
        """Sets the border_bottom of this WebStoriesTextboxOrButton.


        :param border_bottom: The border_bottom of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._border_bottom = border_bottom

    @property
    def border_color(self):
        """Gets the border_color of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border_color of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._border_color

    @border_color.setter
    def border_color(self, border_color):
        """Sets the border_color of this WebStoriesTextboxOrButton.


        :param border_color: The border_color of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._border_color = border_color

    @property
    def border_left(self):
        """Gets the border_left of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border_left of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._border_left

    @border_left.setter
    def border_left(self, border_left):
        """Sets the border_left of this WebStoriesTextboxOrButton.


        :param border_left: The border_left of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._border_left = border_left

    @property
    def border_right(self):
        """Gets the border_right of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border_right of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._border_right

    @border_right.setter
    def border_right(self, border_right):
        """Sets the border_right of this WebStoriesTextboxOrButton.


        :param border_right: The border_right of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._border_right = border_right

    @property
    def border_style(self):
        """Gets the border_style of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border_style of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._border_style

    @border_style.setter
    def border_style(self, border_style):
        """Sets the border_style of this WebStoriesTextboxOrButton.


        :param border_style: The border_style of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._border_style = border_style

    @property
    def border_top(self):
        """Gets the border_top of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The border_top of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._border_top

    @border_top.setter
    def border_top(self, border_top):
        """Sets the border_top of this WebStoriesTextboxOrButton.


        :param border_top: The border_top of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._border_top = border_top

    @property
    def bottom(self):
        """Gets the bottom of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The bottom of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """Sets the bottom of this WebStoriesTextboxOrButton.


        :param bottom: The bottom of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._bottom = bottom

    @property
    def bottom_alignment(self):
        """Gets the bottom_alignment of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The bottom_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._bottom_alignment

    @bottom_alignment.setter
    def bottom_alignment(self, bottom_alignment):
        """Sets the bottom_alignment of this WebStoriesTextboxOrButton.


        :param bottom_alignment: The bottom_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._bottom_alignment = bottom_alignment

    @property
    def bottom_margin(self):
        """Gets the bottom_margin of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The bottom_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._bottom_margin

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """Sets the bottom_margin of this WebStoriesTextboxOrButton.


        :param bottom_margin: The bottom_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._bottom_margin = bottom_margin

    @property
    def bottom_padding(self):
        """Gets the bottom_padding of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The bottom_padding of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._bottom_padding

    @bottom_padding.setter
    def bottom_padding(self, bottom_padding):
        """Sets the bottom_padding of this WebStoriesTextboxOrButton.


        :param bottom_padding: The bottom_padding of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._bottom_padding = bottom_padding

    @property
    def corner_radius(self):
        """Gets the corner_radius of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The corner_radius of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._corner_radius

    @corner_radius.setter
    def corner_radius(self, corner_radius):
        """Sets the corner_radius of this WebStoriesTextboxOrButton.


        :param corner_radius: The corner_radius of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._corner_radius = corner_radius

    @property
    def font_color(self):
        """Gets the font_color of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The font_color of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this WebStoriesTextboxOrButton.


        :param font_color: The font_color of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def font_family(self):
        """Gets the font_family of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The font_family of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this WebStoriesTextboxOrButton.


        :param font_family: The font_family of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._font_family = font_family

    @property
    def font_size(self):
        """Gets the font_size of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The font_size of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this WebStoriesTextboxOrButton.


        :param font_size: The font_size of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def font_style(self):
        """Gets the font_style of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The font_style of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._font_style

    @font_style.setter
    def font_style(self, font_style):
        """Sets the font_style of this WebStoriesTextboxOrButton.


        :param font_style: The font_style of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._font_style = font_style

    @property
    def left(self):
        """Gets the left of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The left of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this WebStoriesTextboxOrButton.


        :param left: The left of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._left = left

    @property
    def left_alignment(self):
        """Gets the left_alignment of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The left_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._left_alignment

    @left_alignment.setter
    def left_alignment(self, left_alignment):
        """Sets the left_alignment of this WebStoriesTextboxOrButton.


        :param left_alignment: The left_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._left_alignment = left_alignment

    @property
    def left_margin(self):
        """Gets the left_margin of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The left_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._left_margin

    @left_margin.setter
    def left_margin(self, left_margin):
        """Sets the left_margin of this WebStoriesTextboxOrButton.


        :param left_margin: The left_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._left_margin = left_margin

    @property
    def left_right_center(self):
        """Gets the left_right_center of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The left_right_center of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._left_right_center

    @left_right_center.setter
    def left_right_center(self, left_right_center):
        """Sets the left_right_center of this WebStoriesTextboxOrButton.


        :param left_right_center: The left_right_center of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._left_right_center = left_right_center

    @property
    def position(self):
        """Gets the position of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The position of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this WebStoriesTextboxOrButton.


        :param position: The position of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def right(self):
        """Gets the right of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The right of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this WebStoriesTextboxOrButton.


        :param right: The right of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._right = right

    @property
    def right_alignment(self):
        """Gets the right_alignment of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The right_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._right_alignment

    @right_alignment.setter
    def right_alignment(self, right_alignment):
        """Sets the right_alignment of this WebStoriesTextboxOrButton.


        :param right_alignment: The right_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._right_alignment = right_alignment

    @property
    def right_margin(self):
        """Gets the right_margin of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The right_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._right_margin

    @right_margin.setter
    def right_margin(self, right_margin):
        """Sets the right_margin of this WebStoriesTextboxOrButton.


        :param right_margin: The right_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._right_margin = right_margin

    @property
    def text(self):
        """Gets the text of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The text of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WebStoriesTextboxOrButton.


        :param text: The text of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def text_alignment(self):
        """Gets the text_alignment of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The text_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._text_alignment

    @text_alignment.setter
    def text_alignment(self, text_alignment):
        """Sets the text_alignment of this WebStoriesTextboxOrButton.


        :param text_alignment: The text_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._text_alignment = text_alignment

    @property
    def text_transform(self):
        """Gets the text_transform of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The text_transform of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._text_transform

    @text_transform.setter
    def text_transform(self, text_transform):
        """Sets the text_transform of this WebStoriesTextboxOrButton.


        :param text_transform: The text_transform of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._text_transform = text_transform

    @property
    def textbox_css(self):
        """Gets the textbox_css of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The textbox_css of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: object
        """
        return self._textbox_css

    @textbox_css.setter
    def textbox_css(self, textbox_css):
        """Sets the textbox_css of this WebStoriesTextboxOrButton.


        :param textbox_css: The textbox_css of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: object
        """

        self._textbox_css = textbox_css

    @property
    def top(self):
        """Gets the top of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The top of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this WebStoriesTextboxOrButton.


        :param top: The top of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._top = top

    @property
    def top_alignment(self):
        """Gets the top_alignment of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The top_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._top_alignment

    @top_alignment.setter
    def top_alignment(self, top_alignment):
        """Sets the top_alignment of this WebStoriesTextboxOrButton.


        :param top_alignment: The top_alignment of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._top_alignment = top_alignment

    @property
    def top_bottom_center(self):
        """Gets the top_bottom_center of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The top_bottom_center of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: bool
        """
        return self._top_bottom_center

    @top_bottom_center.setter
    def top_bottom_center(self, top_bottom_center):
        """Sets the top_bottom_center of this WebStoriesTextboxOrButton.


        :param top_bottom_center: The top_bottom_center of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: bool
        """

        self._top_bottom_center = top_bottom_center

    @property
    def top_margin(self):
        """Gets the top_margin of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The top_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._top_margin

    @top_margin.setter
    def top_margin(self, top_margin):
        """Sets the top_margin of this WebStoriesTextboxOrButton.


        :param top_margin: The top_margin of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._top_margin = top_margin

    @property
    def top_padding(self):
        """Gets the top_padding of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The top_padding of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._top_padding

    @top_padding.setter
    def top_padding(self, top_padding):
        """Sets the top_padding of this WebStoriesTextboxOrButton.


        :param top_padding: The top_padding of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._top_padding = top_padding

    @property
    def type(self):
        """Gets the type of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The type of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebStoriesTextboxOrButton.


        :param type: The type of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The url of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebStoriesTextboxOrButton.


        :param url: The url of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """Gets the width of this WebStoriesTextboxOrButton.  # noqa: E501


        :return: The width of this WebStoriesTextboxOrButton.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this WebStoriesTextboxOrButton.


        :param width: The width of this WebStoriesTextboxOrButton.  # noqa: E501
        :type: str
        """

        self._width = width

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
        if issubclass(WebStoriesTextboxOrButton, dict):
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
        if not isinstance(other, WebStoriesTextboxOrButton):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
