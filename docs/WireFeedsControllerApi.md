# swagger_client.WireFeedsControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_feeds_using_get**](WireFeedsControllerApi.md#find_all_feeds_using_get) | **GET** /api/cms/wires | feeds
[**find_all_images_using_get**](WireFeedsControllerApi.md#find_all_images_using_get) | **GET** /api/cms/wires/images | feeds images
[**find_all_story_using_get**](WireFeedsControllerApi.md#find_all_story_using_get) | **GET** /api/cms/wire/all | findAllStory
[**find_all_tech_images_using_get**](WireFeedsControllerApi.md#find_all_tech_images_using_get) | **GET** /api/cms/tech/images | tech images
[**find_all_wire_images_using_get**](WireFeedsControllerApi.md#find_all_wire_images_using_get) | **GET** /api/cms/wire/image/all | findAllWireImages
[**get_image_using_get**](WireFeedsControllerApi.md#get_image_using_get) | **GET** /api/cms/wire/image/{id} | getImage
[**get_stroy_using_get**](WireFeedsControllerApi.md#get_stroy_using_get) | **GET** /api/cms/wire/{id} | getStroy
[**get_wire_dashboard_search_suggestions_using_get**](WireFeedsControllerApi.md#get_wire_dashboard_search_suggestions_using_get) | **GET** /api/cms/wire/suggestions | getWireDashboardSearchSuggestions
[**get_wire_feeds_using_get**](WireFeedsControllerApi.md#get_wire_feeds_using_get) | **GET** /api/cms/wire/meta | getWireFeeds
[**get_wire_mint_feeds_using_get**](WireFeedsControllerApi.md#get_wire_mint_feeds_using_get) | **GET** /api/cms/wire/mint/meta | getWireMintFeeds
[**update_feed_story_using_put**](WireFeedsControllerApi.md#update_feed_story_using_put) | **PUT** /api/cms/wire/{id} | updateFeedStory

# **find_all_feeds_using_get**
> object find_all_feeds_using_get(params, domain)

feeds

This endpoint can be used for searching, filtering and sorting of the feeds.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # feeds
    api_response = api_instance.find_all_feeds_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->find_all_feeds_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_images_using_get**
> object find_all_images_using_get(params, domain)

feeds images

This endpoint can be used for searching, filtering and sorting of the wire images.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # feeds images
    api_response = api_instance.find_all_images_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->find_all_images_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_story_using_get**
> object find_all_story_using_get(domain)

findAllStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # findAllStory
    api_response = api_instance.find_all_story_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->find_all_story_using_get: %s\n" % e)
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

# **find_all_tech_images_using_get**
> object find_all_tech_images_using_get(params, domain)

tech images

This endpoint can be used for searching, filtering and sorting of the tech images.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # tech images
    api_response = api_instance.find_all_tech_images_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->find_all_tech_images_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_wire_images_using_get**
> object find_all_wire_images_using_get(domain)

findAllWireImages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # findAllWireImages
    api_response = api_instance.find_all_wire_images_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->find_all_wire_images_using_get: %s\n" % e)
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

# **get_image_using_get**
> object get_image_using_get(id, domain)

getImage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
id = 'id_example' # str | id
domain = 'domain_example' # str | Domain

try:
    # getImage
    api_response = api_instance.get_image_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->get_image_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stroy_using_get**
> object get_stroy_using_get(id, domain)

getStroy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
id = 'id_example' # str | id
domain = 'domain_example' # str | Domain

try:
    # getStroy
    api_response = api_instance.get_stroy_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->get_stroy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wire_dashboard_search_suggestions_using_get**
> object get_wire_dashboard_search_suggestions_using_get(text, domain)

getWireDashboardSearchSuggestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
text = 'text_example' # str | text
domain = 'domain_example' # str | Domain

try:
    # getWireDashboardSearchSuggestions
    api_response = api_instance.get_wire_dashboard_search_suggestions_using_get(text, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->get_wire_dashboard_search_suggestions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| text | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wire_feeds_using_get**
> object get_wire_feeds_using_get(domain)

getWireFeeds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getWireFeeds
    api_response = api_instance.get_wire_feeds_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->get_wire_feeds_using_get: %s\n" % e)
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

# **get_wire_mint_feeds_using_get**
> object get_wire_mint_feeds_using_get(domain)

getWireMintFeeds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getWireMintFeeds
    api_response = api_instance.get_wire_mint_feeds_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->get_wire_mint_feeds_using_get: %s\n" % e)
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

# **update_feed_story_using_put**
> object update_feed_story_using_put(body, domain, id)

updateFeedStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WireFeedsControllerApi()
body = swagger_client.WireFeeds() # WireFeeds | story
domain = 'domain_example' # str | Domain
id = 'id_example' # str | id

try:
    # updateFeedStory
    api_response = api_instance.update_feed_story_using_put(body, domain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WireFeedsControllerApi->update_feed_story_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WireFeeds**](WireFeeds.md)| story | 
 **domain** | **str**| Domain | 
 **id** | **str**| id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

