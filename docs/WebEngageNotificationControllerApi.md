# swagger_client.WebEngageNotificationControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_analytics_data_using_post1**](WebEngageNotificationControllerApi.md#fetch_analytics_data_using_post1) | **POST** /api/cms/webengage/analytics | fetchAnalyticsData
[**fetch_applications_using_get**](WebEngageNotificationControllerApi.md#fetch_applications_using_get) | **GET** /api/cms/webengage/applications | fetchApplications
[**fetch_notification_type_using_get**](WebEngageNotificationControllerApi.md#fetch_notification_type_using_get) | **GET** /api/cms/webengage/type | fetchNotificationType
[**fetch_segments_using_get**](WebEngageNotificationControllerApi.md#fetch_segments_using_get) | **GET** /api/cms/webengage/segments | fetchSegments
[**fetch_tags_using_get**](WebEngageNotificationControllerApi.md#fetch_tags_using_get) | **GET** /api/cms/webengage/tags | fetchTags
[**send_notification_using_post1**](WebEngageNotificationControllerApi.md#send_notification_using_post1) | **POST** /api/cms/webengage/notify | sendNotification

# **fetch_analytics_data_using_post1**
> object fetch_analytics_data_using_post1(body, authorization, domain)

fetchAnalyticsData

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebEngageNotificationControllerApi()
body = swagger_client.NotificationRequestDto() # NotificationRequestDto | notificationRequestDto
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchAnalyticsData
    api_response = api_instance.fetch_analytics_data_using_post1(body, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebEngageNotificationControllerApi->fetch_analytics_data_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationRequestDto**](NotificationRequestDto.md)| notificationRequestDto | 
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

# **fetch_applications_using_get**
> object fetch_applications_using_get(authorization, domain)

fetchApplications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchApplications
    api_response = api_instance.fetch_applications_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebEngageNotificationControllerApi->fetch_applications_using_get: %s\n" % e)
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

# **fetch_notification_type_using_get**
> object fetch_notification_type_using_get(authorization, domain)

fetchNotificationType

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchNotificationType
    api_response = api_instance.fetch_notification_type_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebEngageNotificationControllerApi->fetch_notification_type_using_get: %s\n" % e)
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

# **fetch_segments_using_get**
> object fetch_segments_using_get(authorization, domain)

fetchSegments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchSegments
    api_response = api_instance.fetch_segments_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebEngageNotificationControllerApi->fetch_segments_using_get: %s\n" % e)
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

# **fetch_tags_using_get**
> object fetch_tags_using_get(authorization, domain)

fetchTags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebEngageNotificationControllerApi()
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # fetchTags
    api_response = api_instance.fetch_tags_using_get(authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebEngageNotificationControllerApi->fetch_tags_using_get: %s\n" % e)
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

# **send_notification_using_post1**
> object send_notification_using_post1(body, authorization, domain, id=id)

sendNotification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebEngageNotificationControllerApi()
body = swagger_client.NotificationRequestDto() # NotificationRequestDto | notificationRequestDto
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
id = 789 # int | id (optional)

try:
    # sendNotification
    api_response = api_instance.send_notification_using_post1(body, authorization, domain, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebEngageNotificationControllerApi->send_notification_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationRequestDto**](NotificationRequestDto.md)| notificationRequestDto | 
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

