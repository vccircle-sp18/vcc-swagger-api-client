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
from swagger_client.api.dashboard_controller_api import DashboardControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDashboardControllerApi(unittest.TestCase):
    """DashboardControllerApi unit test stubs"""

    def setUp(self):
        self.api = DashboardControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_all_using_get(self):
        """Test case for find_all_using_get

        cards  # noqa: E501
        """
        pass

    def test_get_dashboard_meta_search_using_get(self):
        """Test case for get_dashboard_meta_search_using_get

        getDashboardMetaSearch  # noqa: E501
        """
        pass

    def test_get_dashboard_using_get(self):
        """Test case for get_dashboard_using_get

        getDashboard  # noqa: E501
        """
        pass

    def test_get_element_dashboard_using_get(self):
        """Test case for get_element_dashboard_using_get

        getElementDashboard  # noqa: E501
        """
        pass

    def test_get_workspace_metadata_search_using_get(self):
        """Test case for get_workspace_metadata_search_using_get

        getWorkspaceMetadataSearch  # noqa: E501
        """
        pass

    def test_get_workspace_metadata_using_get(self):
        """Test case for get_workspace_metadata_using_get

        getWorkspaceMetadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()