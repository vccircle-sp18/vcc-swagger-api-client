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


class BreakingNewsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_breaking_news_using_get(self, domain, **kwargs):  # noqa: E501
        """getBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_breaking_news_using_get(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: PageBreakingNews
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_breaking_news_using_get_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_breaking_news_using_get_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def get_breaking_news_using_get_with_http_info(self, domain, **kwargs):  # noqa: E501
        """getBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_breaking_news_using_get_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain (required)
        :return: PageBreakingNews
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
                    " to method get_breaking_news_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_breaking_news_using_get`")  # noqa: E501

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
            '/api/cms/breakingnews/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageBreakingNews',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_breaking_news_using_get1(self, params, domain, **kwargs):  # noqa: E501
        """getBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_breaking_news_using_get1(params, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object params: params (required)
        :param str domain: Domain (required)
        :return: PageBreakingNews
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_breaking_news_using_get1_with_http_info(params, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.get_breaking_news_using_get1_with_http_info(params, domain, **kwargs)  # noqa: E501
            return data

    def get_breaking_news_using_get1_with_http_info(self, params, domain, **kwargs):  # noqa: E501
        """getBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_breaking_news_using_get1_with_http_info(params, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object params: params (required)
        :param str domain: Domain (required)
        :return: PageBreakingNews
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['params', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_breaking_news_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'params' is set
        if ('params' not in params or
                params['params'] is None):
            raise ValueError("Missing the required parameter `params` when calling `get_breaking_news_using_get1`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `get_breaking_news_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/cms/breakingnews', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageBreakingNews',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_breaking_news_using_post(self, body, domain, **kwargs):  # noqa: E501
        """sendBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_breaking_news_using_post(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BreakingNews body: breakingNews (required)
        :param str domain: Domain (required)
        :return: BreakingNews
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_breaking_news_using_post_with_http_info(body, domain, **kwargs)  # noqa: E501
        else:
            (data) = self.send_breaking_news_using_post_with_http_info(body, domain, **kwargs)  # noqa: E501
            return data

    def send_breaking_news_using_post_with_http_info(self, body, domain, **kwargs):  # noqa: E501
        """sendBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_breaking_news_using_post_with_http_info(body, domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BreakingNews body: breakingNews (required)
        :param str domain: Domain (required)
        :return: BreakingNews
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_breaking_news_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_breaking_news_using_post`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `send_breaking_news_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
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
            '/api/cms/breakingnews', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BreakingNews',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_breaking_news_using_put(self, body, domain, id, **kwargs):  # noqa: E501
        """updateBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_breaking_news_using_put(body, domain, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BreakingNews body: breakingNews (required)
        :param str domain: Domain (required)
        :param str id: id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_breaking_news_using_put_with_http_info(body, domain, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_breaking_news_using_put_with_http_info(body, domain, id, **kwargs)  # noqa: E501
            return data

    def update_breaking_news_using_put_with_http_info(self, body, domain, id, **kwargs):  # noqa: E501
        """updateBreakingNews  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_breaking_news_using_put_with_http_info(body, domain, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BreakingNews body: breakingNews (required)
        :param str domain: Domain (required)
        :param str id: id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_breaking_news_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_breaking_news_using_put`")  # noqa: E501
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `update_breaking_news_using_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_breaking_news_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
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
            '/api/cms/breakingnews/{id}', 'PUT',
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