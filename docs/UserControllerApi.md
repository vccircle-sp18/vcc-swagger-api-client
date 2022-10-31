# swagger_client.UserControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logout_using_get**](UserControllerApi.md#logout_using_get) | **GET** /api/cms/logout | logout

# **logout_using_get**
> str logout_using_get(authorization, domain)

logout

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # logout
    api_response = api_instance.logout_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->logout_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

