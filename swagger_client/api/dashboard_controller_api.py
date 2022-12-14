# coding: utf-8

"""
    CMS-Backend API

    This is API documentation of CMS-Backend  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: htdevteam@hindustantimes.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DashboardControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_all_using_get(self, params, type, domain, **kwargs):  # noqa: E501
        """cards  # noqa: E501

        This endpoint can be used for searching, filtering and sorting of the stories.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~) and not(!).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all_using_get(params, type, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object params: params (required)
        :param str type: type (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_all_using_get_with_http_info(params, type, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.find_all_using_get_with_http_info(params, type, domain, **kwargs)  # noqa: E501
            return data

    def find_all_using_get_with_http_info(self, params, type, domain, **kwargs):  # noqa: E501
        """cards  # noqa: E501

        This endpoint can be used for searching, filtering and sorting of the stories.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~) and not(!).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all_using_get_with_http_info(params, type, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object params: params (required)
        :param str type: type (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['params', 'type', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_all_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'params' is set
        if ('params' not in params or
                params['params'] is None):
            raise ValueError("Missing the required parameter `params` when calling `find_all_using_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `find_all_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `find_all_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []
        if 'params' in params:
            query_params.append(('params', params['params']))  # noqa: E501

        header_params = {}
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/search/{type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboard_meta_search_using_get(self, field, domain, **kwargs):  # noqa: E501
        """getDashboardMetaSearch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_meta_search_using_get(field, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: field (required)
        :param str domain: Domain (required)
        :param str text: text
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboard_meta_search_using_get_with_http_info(field, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboard_meta_search_using_get_with_http_info(field, domain, **kwargs)  # noqa: E501
            return data

    def get_dashboard_meta_search_using_get_with_http_info(self, field, domain, **kwargs):  # noqa: E501
        """getDashboardMetaSearch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_meta_search_using_get_with_http_info(field, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: field (required)
        :param str domain: Domain (required)
        :param str text: text
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field', 'domain', 'text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboard_meta_search_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `get_dashboard_meta_search_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_dashboard_meta_search_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'field' in params:
            query_params.append(('field', params['field']))  # noqa: E501
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501

        header_params = {}
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/dashboard/meta/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboard_using_get(self, domain, **kwargs):  # noqa: E501
        """getDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_using_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboard_using_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboard_using_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def get_dashboard_using_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """getDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_using_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboard_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_dashboard_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/dashboard/meta', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_element_dashboard_using_get(self, domain, **kwargs):  # noqa: E501
        """getElementDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_element_dashboard_using_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_element_dashboard_using_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_element_dashboard_using_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def get_element_dashboard_using_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """getElementDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_element_dashboard_using_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_element_dashboard_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_element_dashboard_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/element/meta', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspace_metadata_search_using_get(self, field, domain, **kwargs):  # noqa: E501
        """getWorkspaceMetadataSearch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_metadata_search_using_get(field, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: field (required)
        :param str domain: Domain (required)
        :param str text: text
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workspace_metadata_search_using_get_with_http_info(field, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_metadata_search_using_get_with_http_info(field, domain, **kwargs)  # noqa: E501
            return data

    def get_workspace_metadata_search_using_get_with_http_info(self, field, domain, **kwargs):  # noqa: E501
        """getWorkspaceMetadataSearch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_metadata_search_using_get_with_http_info(field, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: field (required)
        :param str domain: Domain (required)
        :param str text: text
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field', 'domain', 'text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspace_metadata_search_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `get_workspace_metadata_search_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_workspace_metadata_search_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'field' in params:
            query_params.append(('field', params['field']))  # noqa: E501
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501

        header_params = {}
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/workspace/meta/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspace_metadata_using_get(self, domain, **kwargs):  # noqa: E501
        """getWorkspaceMetadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_metadata_using_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workspace_metadata_using_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_metadata_using_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def get_workspace_metadata_using_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """getWorkspaceMetadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_metadata_using_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspace_metadata_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_workspace_metadata_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/workspace/meta', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
