# swagger_client.PublishControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_twitter_details_using_get**](PublishControllerApi.md#get_twitter_details_using_get) | **GET** /api/cms/notify/twitter/details | getTwitterDetails
[**post_on_facebook_using_post**](PublishControllerApi.md#post_on_facebook_using_post) | **POST** /api/cms/notify/facebook/{articleId} | postOnFacebook
[**post_on_twitter_handle_using_post**](PublishControllerApi.md#post_on_twitter_handle_using_post) | **POST** /api/cms/notify/twitter/handle/{articleId}/{twitterHandleId} | postOnTwitterHandle
[**post_on_twitter_using_post**](PublishControllerApi.md#post_on_twitter_using_post) | **POST** /api/cms/notify/twitter/{articleId} | postOnTwitter
[**send_browser_notification_using_post**](PublishControllerApi.md#send_browser_notification_using_post) | **POST** /api/cms/notify/browser/{articleId} | sendBrowserNotification
[**send_flash_notification_using_post**](PublishControllerApi.md#send_flash_notification_using_post) | **POST** /api/cms/notify/browser/flash | sendFlashNotification
[**send_mobile_flash_notification_using_post**](PublishControllerApi.md#send_mobile_flash_notification_using_post) | **POST** /api/cms/notify/mobile/flash | sendMobileFlashNotification
[**send_mobile_notification_using_post**](PublishControllerApi.md#send_mobile_notification_using_post) | **POST** /api/cms/notify/mobile/{articleId} | sendMobileNotification

# **get_twitter_details_using_get**
> list[DomainTwitterConfigurationData] get_twitter_details_using_get(domain)

getTwitterDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getTwitterDetails
    api_response = api_instance.get_twitter_details_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->get_twitter_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**list[DomainTwitterConfigurationData]**](DomainTwitterConfigurationData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_on_facebook_using_post**
> ApiResponse post_on_facebook_using_post(article_id, authorization, domain)

postOnFacebook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
article_id = 789 # int | articleId
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # postOnFacebook
    api_response = api_instance.post_on_facebook_using_post(article_id, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->post_on_facebook_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| articleId | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_on_twitter_handle_using_post**
> ApiResponse post_on_twitter_handle_using_post(article_id, authorization, domain, twitter_handle_id)

postOnTwitterHandle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
article_id = 789 # int | articleId
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
twitter_handle_id = 'twitter_handle_id_example' # str | twitterHandleId

try:
    # postOnTwitterHandle
    api_response = api_instance.post_on_twitter_handle_using_post(article_id, authorization, domain, twitter_handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->post_on_twitter_handle_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| articleId | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **twitter_handle_id** | **str**| twitterHandleId | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_on_twitter_using_post**
> ApiResponse post_on_twitter_using_post(article_id, authorization, domain)

postOnTwitter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
article_id = 789 # int | articleId
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # postOnTwitter
    api_response = api_instance.post_on_twitter_using_post(article_id, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->post_on_twitter_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| articleId | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_browser_notification_using_post**
> ApiResponse send_browser_notification_using_post(body, authorization, domain, article_id)

sendBrowserNotification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
body = swagger_client.NotificationGeoLocations() # NotificationGeoLocations | notificationGeoLocations
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
article_id = 789 # int | articleId

try:
    # sendBrowserNotification
    api_response = api_instance.send_browser_notification_using_post(body, authorization, domain, article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->send_browser_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationGeoLocations**](NotificationGeoLocations.md)| notificationGeoLocations | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **article_id** | **int**| articleId | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_flash_notification_using_post**
> ApiResponse send_flash_notification_using_post(body, authorization, domain)

sendFlashNotification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
body = swagger_client.Story() # Story | article
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # sendFlashNotification
    api_response = api_instance.send_flash_notification_using_post(body, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->send_flash_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| article | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mobile_flash_notification_using_post**
> ApiResponse send_mobile_flash_notification_using_post(body, authorization, domain)

sendMobileFlashNotification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
body = swagger_client.Story() # Story | article
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # sendMobileFlashNotification
    api_response = api_instance.send_mobile_flash_notification_using_post(body, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->send_mobile_flash_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| article | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mobile_notification_using_post**
> ApiResponse send_mobile_notification_using_post(body, authorization, domain, article_id)

sendMobileNotification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishControllerApi()
body = swagger_client.NotificationGeoLocations() # NotificationGeoLocations | notificationGeoLocations
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
article_id = 789 # int | articleId

try:
    # sendMobileNotification
    api_response = api_instance.send_mobile_notification_using_post(body, authorization, domain, article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishControllerApi->send_mobile_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationGeoLocations**](NotificationGeoLocations.md)| notificationGeoLocations | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **article_id** | **int**| articleId | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

