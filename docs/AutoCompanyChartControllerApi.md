# swagger_client.AutoCompanyChartControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company_chart_using_get**](AutoCompanyChartControllerApi.md#add_company_chart_using_get) | **GET** /api/cms/automated/company-chart/{id} | addCompanyChart

# **add_company_chart_using_get**
> object add_company_chart_using_get(id, domain)

addCompanyChart

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AutoCompanyChartControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain

try:
    # addCompanyChart
    api_response = api_instance.add_company_chart_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoCompanyChartControllerApi->add_company_chart_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

