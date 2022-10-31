# swagger_client.AdminControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_domain_using_post**](AdminControllerApi.md#enable_domain_using_post) | **POST** /api/cms/admin/enable/domain | enableDomain
[**get_all_domain_configs_using_get**](AdminControllerApi.md#get_all_domain_configs_using_get) | **GET** /api/cms/admin/config/all | getAllDomainConfigs

# **enable_domain_using_post**
> object enable_domain_using_post(domain_id)

enableDomain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminControllerApi()
domain_id = 'domain_id_example' # str | domainId

try:
    # enableDomain
    api_response = api_instance.enable_domain_using_post(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->enable_domain_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| domainId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_domain_configs_using_get**
> list[FrontendConfiguration] get_all_domain_configs_using_get()

getAllDomainConfigs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminControllerApi()

try:
    # getAllDomainConfigs
    api_response = api_instance.get_all_domain_configs_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->get_all_domain_configs_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FrontendConfiguration]**](FrontendConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

