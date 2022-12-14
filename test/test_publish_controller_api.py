# coding: utf-8

"""
    CMS-Backend API

    This is API documentation of CMS-Backend  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: htdevteam@hindustantimes.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.publish_controller_api import PublishControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPublishControllerApi(unittest.TestCase):
    """PublishControllerApi unit test stubs"""

    def setUp(self):
        self.api = PublishControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_twitter_details_using_get(self):
        """Test case for get_twitter_details_using_get

        getTwitterDetails  # noqa: E501
        """
        pass

    def test_post_on_facebook_using_post(self):
        """Test case for post_on_facebook_using_post

        postOnFacebook  # noqa: E501
        """
        pass

    def test_post_on_twitter_handle_using_post(self):
        """Test case for post_on_twitter_handle_using_post

        postOnTwitterHandle  # noqa: E501
        """
        pass

    def test_post_on_twitter_using_post(self):
        """Test case for post_on_twitter_using_post

        postOnTwitter  # noqa: E501
        """
        pass

    def test_send_browser_notification_using_post(self):
        """Test case for send_browser_notification_using_post

        sendBrowserNotification  # noqa: E501
        """
        pass

    def test_send_flash_notification_using_post(self):
        """Test case for send_flash_notification_using_post

        sendFlashNotification  # noqa: E501
        """
        pass

    def test_send_mobile_flash_notification_using_post(self):
        """Test case for send_mobile_flash_notification_using_post

        sendMobileFlashNotification  # noqa: E501
        """
        pass

    def test_send_mobile_notification_using_post(self):
        """Test case for send_mobile_notification_using_post

        sendMobileNotification  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
