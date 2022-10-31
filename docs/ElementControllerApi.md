# swagger_client.ElementControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_article_using_post**](ElementControllerApi.md#create_article_using_post) | **POST** /api/cms/element | createArticle
[**create_elements_copy_using_get**](ElementControllerApi.md#create_elements_copy_using_get) | **GET** /api/cms/copy/elements/story/{id} | createElementsCopy
[**delete_article_using_delete**](ElementControllerApi.md#delete_article_using_delete) | **DELETE** /api/cms/element/{id} | deleteArticle
[**find_all_articles_by_ids_using_post**](ElementControllerApi.md#find_all_articles_by_ids_using_post) | **POST** /api/cms/element/get-all-by-ids/ | findAllArticlesByIds
[**find_all_articles_using_get**](ElementControllerApi.md#find_all_articles_using_get) | **GET** /api/cms/element/all | findAllArticles
[**find_all_elements_using_get**](ElementControllerApi.md#find_all_elements_using_get) | **GET** /api/cms/elements | Articles
[**get_article_using_get**](ElementControllerApi.md#get_article_using_get) | **GET** /api/cms/element/{id} | getArticle
[**get_cricket_fixtures_using_get**](ElementControllerApi.md#get_cricket_fixtures_using_get) | **GET** /api/cms/element/cricket/fixtures | getCricketFixtures
[**get_element_collection_types_by_type_using_get**](ElementControllerApi.md#get_element_collection_types_by_type_using_get) | **GET** /api/cms/element/collectiontype/all/{type} | getElementCollectionTypesByType
[**get_element_designs_by_type_using_get**](ElementControllerApi.md#get_element_designs_by_type_using_get) | **GET** /api/cms/element/design/all/{type} | getElementDesignsByType
[**get_elements_copy_using_get**](ElementControllerApi.md#get_elements_copy_using_get) | **GET** /api/cms/elements/story/{id} | getElementsCopy
[**get_lead_media_copy_using_get**](ElementControllerApi.md#get_lead_media_copy_using_get) | **GET** /api/cms/elements/story/leadmedia/{id} | getLeadMediaCopy
[**get_photo_gallery_element_using_post**](ElementControllerApi.md#get_photo_gallery_element_using_post) | **POST** /api/cms/elements/photoStory | getPhotoGalleryElement
[**search_article_using_get**](ElementControllerApi.md#search_article_using_get) | **GET** /api/cms/search/element/{tags} | searchArticle
[**update_article_using_put**](ElementControllerApi.md#update_article_using_put) | **PUT** /api/cms/element/{id} | updateArticle
[**update_parent_using_put**](ElementControllerApi.md#update_parent_using_put) | **PUT** /api/cms/element/parent/{id} | updateParent

# **create_article_using_post**
> Article create_article_using_post(body, domain)

createArticle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
body = swagger_client.Element() # Element | article
domain = 'domain_example' # str | Domain

try:
    # createArticle
    api_response = api_instance.create_article_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->create_article_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Element**](Element.md)| article | 
 **domain** | **str**| Domain | 

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_elements_copy_using_get**
> object create_elements_copy_using_get(id, domain_from, domain)

createElementsCopy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
id = 789 # int | id
domain_from = 'domain_from_example' # str | domainFrom
domain = 'domain_example' # str | Domain

try:
    # createElementsCopy
    api_response = api_instance.create_elements_copy_using_get(id, domain_from, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->create_elements_copy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain_from** | **str**| domainFrom | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_article_using_delete**
> object delete_article_using_delete(id, authorization, domain, discard=discard)

deleteArticle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
id = 789 # int | id
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
discard = true # bool | discard (optional)

try:
    # deleteArticle
    api_response = api_instance.delete_article_using_delete(id, authorization, domain, discard=discard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->delete_article_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **discard** | **bool**| discard | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_articles_by_ids_using_post**
> object find_all_articles_by_ids_using_post(domain, body=body)

findAllArticlesByIds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
domain = 'domain_example' # str | Domain
body = swagger_client.OptionalListlong() # OptionalListlong | ids (optional)

try:
    # findAllArticlesByIds
    api_response = api_instance.find_all_articles_by_ids_using_post(domain, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->find_all_articles_by_ids_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **body** | [**OptionalListlong**](OptionalListlong.md)| ids | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_articles_using_get**
> PageArticle find_all_articles_using_get(domain)

findAllArticles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
domain = 'domain_example' # str | Domain

try:
    # findAllArticles
    api_response = api_instance.find_all_articles_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->find_all_articles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**PageArticle**](PageArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_elements_using_get**
> object find_all_elements_using_get(params, domain)

Articles

This endpoint can be used for searching, filtering and sorting of the Articles.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # Articles
    api_response = api_instance.find_all_elements_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->find_all_elements_using_get: %s\n" % e)
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

# **get_article_using_get**
> object get_article_using_get(id, domain)

getArticle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain

try:
    # getArticle
    api_response = api_instance.get_article_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_article_using_get: %s\n" % e)
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

# **get_cricket_fixtures_using_get**
> object get_cricket_fixtures_using_get(params, authorization, domain)

getCricketFixtures

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
params = NULL # object | params
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # getCricketFixtures
    api_response = api_instance.get_cricket_fixtures_using_get(params, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_cricket_fixtures_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
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

# **get_element_collection_types_by_type_using_get**
> list[str] get_element_collection_types_by_type_using_get(domain, type)

getElementCollectionTypesByType

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
domain = 'domain_example' # str | Domain
type = 'type_example' # str | type

try:
    # getElementCollectionTypesByType
    api_response = api_instance.get_element_collection_types_by_type_using_get(domain, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_element_collection_types_by_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **type** | **str**| type | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_designs_by_type_using_get**
> list[str] get_element_designs_by_type_using_get(domain, type)

getElementDesignsByType

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
domain = 'domain_example' # str | Domain
type = 'type_example' # str | type

try:
    # getElementDesignsByType
    api_response = api_instance.get_element_designs_by_type_using_get(domain, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_element_designs_by_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **type** | **str**| type | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements_copy_using_get**
> object get_elements_copy_using_get(id, domain_from, domain)

getElementsCopy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
id = 789 # int | id
domain_from = 'domain_from_example' # str | domainFrom
domain = 'domain_example' # str | Domain

try:
    # getElementsCopy
    api_response = api_instance.get_elements_copy_using_get(id, domain_from, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_elements_copy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain_from** | **str**| domainFrom | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_media_copy_using_get**
> object get_lead_media_copy_using_get(id, domain_from, domain)

getLeadMediaCopy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
id = 789 # int | id
domain_from = 'domain_from_example' # str | domainFrom
domain = 'domain_example' # str | Domain

try:
    # getLeadMediaCopy
    api_response = api_instance.get_lead_media_copy_using_get(id, domain_from, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_lead_media_copy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain_from** | **str**| domainFrom | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo_gallery_element_using_post**
> object get_photo_gallery_element_using_post(body, domain)

getPhotoGalleryElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
body = swagger_client.PhotoGalleryResponse() # PhotoGalleryResponse | article
domain = 'domain_example' # str | Domain

try:
    # getPhotoGalleryElement
    api_response = api_instance.get_photo_gallery_element_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->get_photo_gallery_element_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhotoGalleryResponse**](PhotoGalleryResponse.md)| article | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_article_using_get**
> object search_article_using_get(tags, domain)

searchArticle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
tags = 'tags_example' # str | tags
domain = 'domain_example' # str | Domain

try:
    # searchArticle
    api_response = api_instance.search_article_using_get(tags, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->search_article_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| tags | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_article_using_put**
> object update_article_using_put(body, authorization, domain, id, auto_save=auto_save)

updateArticle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
body = swagger_client.Element() # Element | article
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
id = 789 # int | id
auto_save = true # bool | autoSave (optional)

try:
    # updateArticle
    api_response = api_instance.update_article_using_put(body, authorization, domain, id, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->update_article_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Element**](Element.md)| article | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **id** | **int**| id | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parent_using_put**
> object update_parent_using_put(id, authorization, domain)

updateParent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElementControllerApi()
id = 789 # int | id
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # updateParent
    api_response = api_instance.update_parent_using_put(id, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementControllerApi->update_parent_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
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

