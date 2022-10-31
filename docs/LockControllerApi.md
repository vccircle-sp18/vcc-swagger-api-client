# swagger_client.LockControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_card_lock_using_get**](LockControllerApi.md#acquire_card_lock_using_get) | **GET** /api/cms/lock/acquire/article | acquireCardLock
[**acquire_footer_lock_using_get**](LockControllerApi.md#acquire_footer_lock_using_get) | **GET** /api/cms/lock/acquire/footer/navigation | acquireFooterLock
[**acquire_level_lock_using_get**](LockControllerApi.md#acquire_level_lock_using_get) | **GET** /api/cms/lock/acquire/level/navigation | acquireLevelLock
[**acquire_page_lock_using_get**](LockControllerApi.md#acquire_page_lock_using_get) | **GET** /api/cms/lock/acquire/page | acquirePageLock
[**acquire_section_lock_using_get**](LockControllerApi.md#acquire_section_lock_using_get) | **GET** /api/cms/lock/acquire/section/navigation | acquireSectionLock
[**acquire_topic_lock_using_get**](LockControllerApi.md#acquire_topic_lock_using_get) | **GET** /api/cms/lock/acquire/topic/navigation | acquireTopicLock
[**release_and_acquire_card_lock_using_get**](LockControllerApi.md#release_and_acquire_card_lock_using_get) | **GET** /api/cms/unlock/article | releaseAndAcquireCardLock
[**release_and_acquire_footer_lock_using_get**](LockControllerApi.md#release_and_acquire_footer_lock_using_get) | **GET** /api/cms/unlock/footer/navigation | releaseAndAcquireFooterLock
[**release_and_acquire_level_lock_using_get**](LockControllerApi.md#release_and_acquire_level_lock_using_get) | **GET** /api/cms/unlock/level/navigation | releaseAndAcquireLevelLock
[**release_and_acquire_page_lock_using_get**](LockControllerApi.md#release_and_acquire_page_lock_using_get) | **GET** /api/cms/unlock/page | releaseAndAcquirePageLock
[**release_and_acquire_section_lock_using_get**](LockControllerApi.md#release_and_acquire_section_lock_using_get) | **GET** /api/cms/unlock/section/navigation | releaseAndAcquireSectionLock
[**release_and_acquire_topic_lock_using_get**](LockControllerApi.md#release_and_acquire_topic_lock_using_get) | **GET** /api/cms/unlock/topic/navigation | releaseAndAcquireTopicLock
[**release_card_lock_using_get**](LockControllerApi.md#release_card_lock_using_get) | **GET** /api/cms/lock/release/article | releaseCardLock
[**release_footer_lock_using_get**](LockControllerApi.md#release_footer_lock_using_get) | **GET** /api/cms/lock/release/footer/navigation | releaseFooterLock
[**release_level_lock_using_get**](LockControllerApi.md#release_level_lock_using_get) | **GET** /api/cms/lock/release/level/navigation | releaseLevelLock
[**release_page_lock_using_get**](LockControllerApi.md#release_page_lock_using_get) | **GET** /api/cms/lock/release/page | releasePageLock
[**release_section_lock_using_get**](LockControllerApi.md#release_section_lock_using_get) | **GET** /api/cms/lock/release/section/navigation | releaseSectionLock
[**release_topic_lock_using_get**](LockControllerApi.md#release_topic_lock_using_get) | **GET** /api/cms/lock/release/topic/navigation | releaseTopicLock

# **acquire_card_lock_using_get**
> bool acquire_card_lock_using_get(article_id, domain)

acquireCardLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
article_id = 789 # int | articleId
domain = 'domain_example' # str | Domain

try:
    # acquireCardLock
    api_response = api_instance.acquire_card_lock_using_get(article_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->acquire_card_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| articleId | 
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquire_footer_lock_using_get**
> bool acquire_footer_lock_using_get(domain)

acquireFooterLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # acquireFooterLock
    api_response = api_instance.acquire_footer_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->acquire_footer_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquire_level_lock_using_get**
> bool acquire_level_lock_using_get(domain, nav_type)

acquireLevelLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain
nav_type = 'nav_type_example' # str | navType

try:
    # acquireLevelLock
    api_response = api_instance.acquire_level_lock_using_get(domain, nav_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->acquire_level_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **nav_type** | **str**| navType | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquire_page_lock_using_get**
> bool acquire_page_lock_using_get(page_id, domain)

acquirePageLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain

try:
    # acquirePageLock
    api_response = api_instance.acquire_page_lock_using_get(page_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->acquire_page_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquire_section_lock_using_get**
> bool acquire_section_lock_using_get(domain)

acquireSectionLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # acquireSectionLock
    api_response = api_instance.acquire_section_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->acquire_section_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquire_topic_lock_using_get**
> bool acquire_topic_lock_using_get(domain)

acquireTopicLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # acquireTopicLock
    api_response = api_instance.acquire_topic_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->acquire_topic_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_and_acquire_card_lock_using_get**
> bool release_and_acquire_card_lock_using_get(article_id, domain)

releaseAndAcquireCardLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
article_id = 789 # int | articleId
domain = 'domain_example' # str | Domain

try:
    # releaseAndAcquireCardLock
    api_response = api_instance.release_and_acquire_card_lock_using_get(article_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_and_acquire_card_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| articleId | 
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_and_acquire_footer_lock_using_get**
> bool release_and_acquire_footer_lock_using_get(domain)

releaseAndAcquireFooterLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # releaseAndAcquireFooterLock
    api_response = api_instance.release_and_acquire_footer_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_and_acquire_footer_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_and_acquire_level_lock_using_get**
> bool release_and_acquire_level_lock_using_get(domain, nav_type)

releaseAndAcquireLevelLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain
nav_type = 'nav_type_example' # str | navType

try:
    # releaseAndAcquireLevelLock
    api_response = api_instance.release_and_acquire_level_lock_using_get(domain, nav_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_and_acquire_level_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **nav_type** | **str**| navType | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_and_acquire_page_lock_using_get**
> bool release_and_acquire_page_lock_using_get(page_id, domain)

releaseAndAcquirePageLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain

try:
    # releaseAndAcquirePageLock
    api_response = api_instance.release_and_acquire_page_lock_using_get(page_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_and_acquire_page_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_and_acquire_section_lock_using_get**
> bool release_and_acquire_section_lock_using_get(domain)

releaseAndAcquireSectionLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # releaseAndAcquireSectionLock
    api_response = api_instance.release_and_acquire_section_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_and_acquire_section_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_and_acquire_topic_lock_using_get**
> bool release_and_acquire_topic_lock_using_get(domain)

releaseAndAcquireTopicLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # releaseAndAcquireTopicLock
    api_response = api_instance.release_and_acquire_topic_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_and_acquire_topic_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_card_lock_using_get**
> bool release_card_lock_using_get(article_id, domain)

releaseCardLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
article_id = 789 # int | articleId
domain = 'domain_example' # str | Domain

try:
    # releaseCardLock
    api_response = api_instance.release_card_lock_using_get(article_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_card_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| articleId | 
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_footer_lock_using_get**
> bool release_footer_lock_using_get(domain)

releaseFooterLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # releaseFooterLock
    api_response = api_instance.release_footer_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_footer_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_level_lock_using_get**
> bool release_level_lock_using_get(domain, nav_type)

releaseLevelLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain
nav_type = 'nav_type_example' # str | navType

try:
    # releaseLevelLock
    api_response = api_instance.release_level_lock_using_get(domain, nav_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_level_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **nav_type** | **str**| navType | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_page_lock_using_get**
> bool release_page_lock_using_get(page_id, domain)

releasePageLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain

try:
    # releasePageLock
    api_response = api_instance.release_page_lock_using_get(page_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_page_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_section_lock_using_get**
> bool release_section_lock_using_get(domain)

releaseSectionLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # releaseSectionLock
    api_response = api_instance.release_section_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_section_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_topic_lock_using_get**
> bool release_topic_lock_using_get(domain)

releaseTopicLock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LockControllerApi()
domain = 'domain_example' # str | Domain

try:
    # releaseTopicLock
    api_response = api_instance.release_topic_lock_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockControllerApi->release_topic_lock_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

