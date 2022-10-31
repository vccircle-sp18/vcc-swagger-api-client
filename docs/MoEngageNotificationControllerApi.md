# swagger_client.MoEngageNotificationControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_segment_using_post**](MoEngageNotificationControllerApi.md#add_segment_using_post) | **POST** /api/cms/moengage/segment | addSegment
[**fetch_all_segment_using_get**](MoEngageNotificationControllerApi.md#fetch_all_segment_using_get) | **GET** /api/cms/moengage/segment/all | fetchAllSegment
[**fetch_analytics_data_using_post**](MoEngageNotificationControllerApi.md#fetch_analytics_data_using_post) | **POST** /api/cms/moengage/analytics | fetchAnalyticsData
[**fetch_cross_domains_using_get**](MoEngageNotificationControllerApi.md#fetch_cross_domains_using_get) | **GET** /api/cms/moengage/crossDomain/all | fetchCrossDomains
[**fetch_notification_list_using_get**](MoEngageNotificationControllerApi.md#fetch_notification_list_using_get) | **GET** /api/cms/moengage/notification/list | fetchNotificationList
[**fetch_slug_names_using_get**](MoEngageNotificationControllerApi.md#fetch_slug_names_using_get) | **GET** /api/cms/moengage/slug/all | fetchSlugNames
[**send_notification_using_post**](MoEngageNotificationControllerApi.md#send_notification_using_post) | **POST** /api/cms/moengage/notify | sendNotification

# **add_segment_using_post**
> object add_segment_using_post(body, authorization, domain)

addSegment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
body = swagger_client.MoEngageSegmentRequestDto() # MoEngageSegmentRequestDto | request
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # addSegment
    api_response = api_instance.add_segment_using_post(body, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->add_segment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoEngageSegmentRequestDto**](MoEngageSegmentRequestDto.md)| request | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_segment_using_get**
> object fetch_all_segment_using_get(authorization, domain)

fetchAllSegment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchAllSegment
    api_response = api_instance.fetch_all_segment_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->fetch_all_segment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_analytics_data_using_post**
> object fetch_analytics_data_using_post(body, authorization, domain)

fetchAnalyticsData

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
body = swagger_client.MoEngageNotificationRequestDto() # MoEngageNotificationRequestDto | notificationRequestDto
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchAnalyticsData
    api_response = api_instance.fetch_analytics_data_using_post(body, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->fetch_analytics_data_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoEngageNotificationRequestDto**](MoEngageNotificationRequestDto.md)| notificationRequestDto | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_cross_domains_using_get**
> list[str] fetch_cross_domains_using_get(authorization, domain)

fetchCrossDomains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchCrossDomains
    api_response = api_instance.fetch_cross_domains_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->fetch_cross_domains_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_notification_list_using_get**
> list[object] fetch_notification_list_using_get(authorization, domain)

fetchNotificationList

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchNotificationList
    api_response = api_instance.fetch_notification_list_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->fetch_notification_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_slug_names_using_get**
> object fetch_slug_names_using_get(authorization, domain)

fetchSlugNames

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchSlugNames
    api_response = api_instance.fetch_slug_names_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->fetch_slug_names_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_notification_using_post**
> object send_notification_using_post(body, authorization, domain, id=id)

sendNotification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MoEngageNotificationControllerApi()
body = swagger_client.MoEngageNotificationRequestDto() # MoEngageNotificationRequestDto | moEngageNotificationRequestDto
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
id = 789 # int | id (optional)

try:
    # sendNotification
    api_response = api_instance.send_notification_using_post(body, authorization, domain, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoEngageNotificationControllerApi->send_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoEngageNotificationRequestDto**](MoEngageNotificationRequestDto.md)| moEngageNotificationRequestDto | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **id** | **int**| id | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

