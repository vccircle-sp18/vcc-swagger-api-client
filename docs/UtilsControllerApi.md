# swagger_client.UtilsControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_all_locks_using_get**](UtilsControllerApi.md#remove_all_locks_using_get) | **GET** /api/cms/utils/removeAllLocks | removeAllLocks

# **remove_all_locks_using_get**
> ResponseEntity remove_all_locks_using_get(domain)

removeAllLocks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # removeAllLocks
    api_response = api_instance.remove_all_locks_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsControllerApi->remove_all_locks_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

