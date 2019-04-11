# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LanguageGenerationEndpointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_language_generation_endpoint(self, endpoint_definition, **kwargs):  # noqa: E501
        """Creates a new language generation endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_language_generation_endpoint(endpoint_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndpointDefinition endpoint_definition: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_language_generation_endpoint_with_http_info(endpoint_definition, **kwargs)  # noqa: E501
        else:
            (data) = self.create_language_generation_endpoint_with_http_info(endpoint_definition, **kwargs)  # noqa: E501
            return data

    def create_language_generation_endpoint_with_http_info(self, endpoint_definition, **kwargs):  # noqa: E501
        """Creates a new language generation endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_language_generation_endpoint_with_http_info(endpoint_definition, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndpointDefinition endpoint_definition: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_definition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_language_generation_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_definition' is set
        if ('endpoint_definition' not in params or
                params['endpoint_definition'] is None):
            raise ValueError("Missing the required parameter `endpoint_definition` when calling `create_language_generation_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'endpoint_definition' in params:
            body_params = params['endpoint_definition']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/languagegeneration/v2.0/Endpoints', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_language_generation_endpoint(self, id, **kwargs):  # noqa: E501
        """Deletes the language generation model endpoint with the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_language_generation_endpoint(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the language generation model endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_language_generation_endpoint_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_language_generation_endpoint_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_language_generation_endpoint_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes the language generation model endpoint with the given id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_language_generation_endpoint_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the language generation model endpoint. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_language_generation_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_language_generation_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/languagegeneration/v2.0/Endpoints/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_language_generation_endpoint(self, id, **kwargs):  # noqa: E501
        """Gets the specified deployed language generation endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_generation_endpoint(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Endpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_language_generation_endpoint_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_language_generation_endpoint_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_language_generation_endpoint_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the specified deployed language generation endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_generation_endpoint_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Endpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_language_generation_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_language_generation_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/languagegeneration/v2.0/Endpoints/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Endpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_language_generation_endpoints(self, **kwargs):  # noqa: E501
        """Gets all language generation endpoint of a subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_generation_endpoints(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Endpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_language_generation_endpoints_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_language_generation_endpoints_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_language_generation_endpoints_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all language generation endpoint of a subscription.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_generation_endpoints_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Endpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_language_generation_endpoints" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/languagegeneration/v2.0/Endpoints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Endpoint]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_supported_locales_for_language_generation_endpoints(self, **kwargs):  # noqa: E501
        """Gets a list of supported locales for language generation endpoint creation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_locales_for_language_generation_endpoints(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_supported_locales_for_language_generation_endpoints_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_supported_locales_for_language_generation_endpoints_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_supported_locales_for_language_generation_endpoints_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of supported locales for language generation endpoint creation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_supported_locales_for_language_generation_endpoints_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supported_locales_for_language_generation_endpoints" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/languagegeneration/v2.0/Endpoints/locales', 'GET',
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

    def update_language_generation_endpoint(self, id, endpoint_update, **kwargs):  # noqa: E501
        """Updates the mutable details of the language generation endpoint identified by its id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_language_generation_endpoint(id, endpoint_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the language generation model endpoint. (required)
        :param EndpointUpdate endpoint_update: The object contains the updated fields of the endpoint. (required)
        :return: Endpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_language_generation_endpoint_with_http_info(id, endpoint_update, **kwargs)  # noqa: E501
        else:
            (data) = self.update_language_generation_endpoint_with_http_info(id, endpoint_update, **kwargs)  # noqa: E501
            return data

    def update_language_generation_endpoint_with_http_info(self, id, endpoint_update, **kwargs):  # noqa: E501
        """Updates the mutable details of the language generation endpoint identified by its id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_language_generation_endpoint_with_http_info(id, endpoint_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the language generation model endpoint. (required)
        :param EndpointUpdate endpoint_update: The object contains the updated fields of the endpoint. (required)
        :return: Endpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'endpoint_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_language_generation_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_language_generation_endpoint`")  # noqa: E501
        # verify the required parameter 'endpoint_update' is set
        if ('endpoint_update' not in params or
                params['endpoint_update'] is None):
            raise ValueError("Missing the required parameter `endpoint_update` when calling `update_language_generation_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'endpoint_update' in params:
            body_params = params['endpoint_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['subscription_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/languagegeneration/v2.0/Endpoints/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Endpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
