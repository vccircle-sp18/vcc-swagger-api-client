# swagger_client.PodcastControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_publisher_list_using_get**](PodcastControllerApi.md#get_publisher_list_using_get) | **GET** /api/cms/podcast/publishers | getPublisherList

# **get_publisher_list_using_get**
> object get_publisher_list_using_get(domain)

getPublisherList

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PodcastControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getPublisherList
    api_response = api_instance.get_publisher_list_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PodcastControllerApi->get_publisher_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

