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


class MoEngageNotificationControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_segment_using_post(self, body, authorization, domain, **kwargs):  # noqa: E501
        """addSegment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_segment_using_post(body, authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoEngageSegmentRequestDto body: request (required)
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_segment_using_post_with_http_info(body, authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.add_segment_using_post_with_http_info(body, authorization, domain, **kwargs)  # noqa: E501
            return data

    def add_segment_using_post_with_http_info(self, body, authorization, domain, **kwargs):  # noqa: E501
        """addSegment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_segment_using_post_with_http_info(body, authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoEngageSegmentRequestDto body: request (required)
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_segment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_segment_using_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `add_segment_using_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `add_segment_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/moengage/segment', 'POST',
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

    def fetch_all_segment_using_get(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchAllSegment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_all_segment_using_get(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_all_segment_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_all_segment_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
            return data

    def fetch_all_segment_using_get_with_http_info(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchAllSegment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_all_segment_using_get_with_http_info(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_all_segment_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `fetch_all_segment_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `fetch_all_segment_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/api/cms/moengage/segment/all', 'GET',
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

    def fetch_analytics_data_using_post(self, body, authorization, domain, **kwargs):  # noqa: E501
        """fetchAnalyticsData  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_analytics_data_using_post(body, authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoEngageNotificationRequestDto body: notificationRequestDto (required)
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_analytics_data_using_post_with_http_info(body, authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_analytics_data_using_post_with_http_info(body, authorization, domain, **kwargs)  # noqa: E501
            return data

    def fetch_analytics_data_using_post_with_http_info(self, body, authorization, domain, **kwargs):  # noqa: E501
        """fetchAnalyticsData  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_analytics_data_using_post_with_http_info(body, authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoEngageNotificationRequestDto body: notificationRequestDto (required)
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_analytics_data_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `fetch_analytics_data_using_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `fetch_analytics_data_using_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `fetch_analytics_data_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/moengage/analytics', 'POST',
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

    def fetch_cross_domains_using_get(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchCrossDomains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cross_domains_using_get(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_cross_domains_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_cross_domains_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
            return data

    def fetch_cross_domains_using_get_with_http_info(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchCrossDomains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cross_domains_using_get_with_http_info(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cross_domains_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `fetch_cross_domains_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `fetch_cross_domains_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/api/cms/moengage/crossDomain/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_notification_list_using_get(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchNotificationList  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_notification_list_using_get(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_notification_list_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_notification_list_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
            return data

    def fetch_notification_list_using_get_with_http_info(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchNotificationList  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_notification_list_using_get_with_http_info(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_notification_list_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `fetch_notification_list_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `fetch_notification_list_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/api/cms/moengage/notification/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_slug_names_using_get(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchSlugNames  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_slug_names_using_get(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_slug_names_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_slug_names_using_get_with_http_info(authorization, domain, **kwargs)  # noqa: E501
            return data

    def fetch_slug_names_using_get_with_http_info(self, authorization, domain, **kwargs):  # noqa: E501
        """fetchSlugNames  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_slug_names_using_get_with_http_info(authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_slug_names_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `fetch_slug_names_using_get`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `fetch_slug_names_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/api/cms/moengage/slug/all', 'GET',
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

    def send_notification_using_post(self, body, authorization, domain, **kwargs):  # noqa: E501
        """sendNotification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_notification_using_post(body, authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoEngageNotificationRequestDto body: moEngageNotificationRequestDto (required)
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :param int id: id
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_notification_using_post_with_http_info(body, authorization, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.send_notification_using_post_with_http_info(body, authorization, domain, **kwargs)  # noqa: E501
            return data

    def send_notification_using_post_with_http_info(self, body, authorization, domain, **kwargs):  # noqa: E501
        """sendNotification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_notification_using_post_with_http_info(body, authorization, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoEngageNotificationRequestDto body: moEngageNotificationRequestDto (required)
        :param str authorization: Authorization (required)
        :param str domain: Domain (required)
        :param int id: id
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'domain', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_notification_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_notification_using_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `send_notification_using_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `send_notification_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'domain' in params:
            header_params['Domain'] = params['domain']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/cms/moengage/notify', 'POST',
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
