# swagger_client.ReportControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_report_using_post**](ReportControllerApi.md#generate_report_using_post) | **POST** /api/cms/report | generateReport
[**get_report_subscription_using_get**](ReportControllerApi.md#get_report_subscription_using_get) | **GET** /api/cms/report/subscribe | getReportSubscription
[**get_reports_using_get**](ReportControllerApi.md#get_reports_using_get) | **GET** /api/cms/report | getReports
[**save_report_subscription_using_put**](ReportControllerApi.md#save_report_subscription_using_put) | **PUT** /api/cms/report/subscribe | saveReportSubscription

# **generate_report_using_post**
> Report generate_report_using_post(body, domain)

generateReport

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportControllerApi()
body = swagger_client.Report() # Report | report
domain = 'domain_example' # str | Domain

try:
    # generateReport
    api_response = api_instance.generate_report_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportControllerApi->generate_report_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Report**](Report.md)| report | 
 **domain** | **str**| Domain | 

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_subscription_using_get**
> ReportSubscription get_report_subscription_using_get(id, domain)

getReportSubscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportControllerApi()
id = 'id_example' # str | id
domain = 'domain_example' # str | Domain

try:
    # getReportSubscription
    api_response = api_instance.get_report_subscription_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportControllerApi->get_report_subscription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **domain** | **str**| Domain | 

### Return type

[**ReportSubscription**](ReportSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_using_get**
> PageReport get_reports_using_get(domain)

getReports

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getReports
    api_response = api_instance.get_reports_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportControllerApi->get_reports_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**PageReport**](PageReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_report_subscription_using_put**
> ReportSubscription save_report_subscription_using_put(body, domain)

saveReportSubscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportControllerApi()
body = swagger_client.ReportSubscription() # ReportSubscription | reportSubscription
domain = 'domain_example' # str | Domain

try:
    # saveReportSubscription
    api_response = api_instance.save_report_subscription_using_put(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportControllerApi->save_report_subscription_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportSubscription**](ReportSubscription.md)| reportSubscription | 
 **domain** | **str**| Domain | 

### Return type

[**ReportSubscription**](ReportSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

