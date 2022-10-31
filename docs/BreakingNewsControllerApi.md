# swagger_client.BreakingNewsControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_breaking_news_using_get**](BreakingNewsControllerApi.md#get_breaking_news_using_get) | **GET** /api/cms/breakingnews/all | getBreakingNews
[**get_breaking_news_using_get1**](BreakingNewsControllerApi.md#get_breaking_news_using_get1) | **GET** /api/cms/breakingnews | getBreakingNews
[**send_breaking_news_using_post**](BreakingNewsControllerApi.md#send_breaking_news_using_post) | **POST** /api/cms/breakingnews | sendBreakingNews
[**update_breaking_news_using_put**](BreakingNewsControllerApi.md#update_breaking_news_using_put) | **PUT** /api/cms/breakingnews/{id} | updateBreakingNews

# **get_breaking_news_using_get**
> PageBreakingNews get_breaking_news_using_get(domain)

getBreakingNews

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BreakingNewsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getBreakingNews
    api_response = api_instance.get_breaking_news_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BreakingNewsControllerApi->get_breaking_news_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**PageBreakingNews**](PageBreakingNews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_breaking_news_using_get1**
> PageBreakingNews get_breaking_news_using_get1(params, domain)

getBreakingNews

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BreakingNewsControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # getBreakingNews
    api_response = api_instance.get_breaking_news_using_get1(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BreakingNewsControllerApi->get_breaking_news_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

[**PageBreakingNews**](PageBreakingNews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_breaking_news_using_post**
> BreakingNews send_breaking_news_using_post(body, domain)

sendBreakingNews

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BreakingNewsControllerApi()
body = swagger_client.BreakingNews() # BreakingNews | breakingNews
domain = 'domain_example' # str | Domain

try:
    # sendBreakingNews
    api_response = api_instance.send_breaking_news_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BreakingNewsControllerApi->send_breaking_news_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BreakingNews**](BreakingNews.md)| breakingNews | 
 **domain** | **str**| Domain | 

### Return type

[**BreakingNews**](BreakingNews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_breaking_news_using_put**
> object update_breaking_news_using_put(body, domain, id)

updateBreakingNews

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BreakingNewsControllerApi()
body = swagger_client.BreakingNews() # BreakingNews | breakingNews
domain = 'domain_example' # str | Domain
id = 'id_example' # str | id

try:
    # updateBreakingNews
    api_response = api_instance.update_breaking_news_using_put(body, domain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BreakingNewsControllerApi->update_breaking_news_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BreakingNews**](BreakingNews.md)| breakingNews | 
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

