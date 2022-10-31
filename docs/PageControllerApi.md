# swagger_client.PageControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_section_navigation_using_put**](PageControllerApi.md#add_to_section_navigation_using_put) | **PUT** /api/cms/page/section/navigation | addToSectionNavigation
[**add_to_topic_navigation_using_put**](PageControllerApi.md#add_to_topic_navigation_using_put) | **PUT** /api/cms/page/topic/navigation | addToTopicNavigation
[**add_using_put**](PageControllerApi.md#add_using_put) | **PUT** /api/cms/page/add/article/{pageId} | add
[**create_external_page_using_post**](PageControllerApi.md#create_external_page_using_post) | **POST** /api/cms/page/external | createExternalPage
[**create_page_using_post**](PageControllerApi.md#create_page_using_post) | **POST** /api/cms/page | createPage
[**find_all_articles_by_ids_using_post1**](PageControllerApi.md#find_all_articles_by_ids_using_post1) | **POST** /api/cms/page/get-all-by-ids/ | findAllArticlesByIds
[**get_all_designs_using_get**](PageControllerApi.md#get_all_designs_using_get) | **GET** /api/cms/page/design/all | getAllDesigns
[**get_all_market_topics_using_get**](PageControllerApi.md#get_all_market_topics_using_get) | **GET** /api/cms/page/topic/market/all | getAllMarketTopics
[**get_all_pages_using_get**](PageControllerApi.md#get_all_pages_using_get) | **GET** /api/cms/page/all | getAllPages
[**get_all_topics_using_get**](PageControllerApi.md#get_all_topics_using_get) | **GET** /api/cms/page/topic/all | getAllTopics
[**get_articles_using_get**](PageControllerApi.md#get_articles_using_get) | **GET** /api/cms/page/articles/{pageId} | getArticles
[**get_footer_navigation_using_get**](PageControllerApi.md#get_footer_navigation_using_get) | **GET** /api/cms/page/footer/navigation | getFooterNavigation
[**get_page_meta_using_get**](PageControllerApi.md#get_page_meta_using_get) | **GET** /api/cms/page/meta | getPageMeta
[**get_page_template_using_get**](PageControllerApi.md#get_page_template_using_get) | **GET** /api/cms/page/template/{templateId} | getPageTemplate
[**get_page_using_get**](PageControllerApi.md#get_page_using_get) | **GET** /api/cms/page/{pageId} | getPage
[**get_section_navigation_nav_type_using_get**](PageControllerApi.md#get_section_navigation_nav_type_using_get) | **GET** /api/cms/page/level/navigation | getSectionNavigationNavType
[**get_section_navigation_using_get**](PageControllerApi.md#get_section_navigation_using_get) | **GET** /api/cms/page/section/navigation | getSectionNavigation
[**get_sections_using_get**](PageControllerApi.md#get_sections_using_get) | **GET** /api/cms/page/section/all | getSections
[**get_sub_sections_by_section_using_get**](PageControllerApi.md#get_sub_sections_by_section_using_get) | **GET** /api/cms/page/subsection/all/{sectionId} | getSubSectionsBySection
[**get_topic_navigation_using_get**](PageControllerApi.md#get_topic_navigation_using_get) | **GET** /api/cms/page/topic/navigation | getTopicNavigation
[**page_purge_using_post**](PageControllerApi.md#page_purge_using_post) | **POST** /api/cms/page/purge/{id} | pagePurge
[**remove_article_using_delete**](PageControllerApi.md#remove_article_using_delete) | **DELETE** /api/cms/page/remove/article/{pageId} | removeArticle
[**remove_from_section_navigation_using_delete**](PageControllerApi.md#remove_from_section_navigation_using_delete) | **DELETE** /api/cms/page/section/navigation | removeFromSectionNavigation
[**remove_from_topic_navigation_using_delete**](PageControllerApi.md#remove_from_topic_navigation_using_delete) | **DELETE** /api/cms/page/topic/navigation | removeFromTopicNavigation
[**remove_page_using_delete**](PageControllerApi.md#remove_page_using_delete) | **DELETE** /api/cms/page/{pageId} | removePage
[**save_footer_navigation_using_post**](PageControllerApi.md#save_footer_navigation_using_post) | **POST** /api/cms/page/footer/navigation | saveFooterNavigation
[**save_section_navigation_nav_type_using_post**](PageControllerApi.md#save_section_navigation_nav_type_using_post) | **POST** /api/cms/page/level/navigation | saveSectionNavigationNavType
[**save_section_navigation_using_post**](PageControllerApi.md#save_section_navigation_using_post) | **POST** /api/cms/page/section/navigation | saveSectionNavigation
[**search_page_using_get**](PageControllerApi.md#search_page_using_get) | **GET** /api/cms/page/search | searchPage
[**update_and_save_all_pages_using_post**](PageControllerApi.md#update_and_save_all_pages_using_post) | **POST** /api/cms/page/all/pageapis | updateAndSaveAllPages
[**update_external_page_using_put**](PageControllerApi.md#update_external_page_using_put) | **PUT** /api/cms/page/external/{pageId} | updateExternalPage
[**update_page_using_put**](PageControllerApi.md#update_page_using_put) | **PUT** /api/cms/page/{pageId} | updatePage

# **add_to_section_navigation_using_put**
> add_to_section_navigation_using_put(page_id, position, domain, auto_save=auto_save)

addToSectionNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
position = 56 # int | position
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # addToSectionNavigation
    api_instance.add_to_section_navigation_using_put(page_id, position, domain, auto_save=auto_save)
except ApiException as e:
    print("Exception when calling PageControllerApi->add_to_section_navigation_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **position** | **int**| position | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_to_topic_navigation_using_put**
> add_to_topic_navigation_using_put(page_id, position, domain, auto_save=auto_save)

addToTopicNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
position = 56 # int | position
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # addToTopicNavigation
    api_instance.add_to_topic_navigation_using_put(page_id, position, domain, auto_save=auto_save)
except ApiException as e:
    print("Exception when calling PageControllerApi->add_to_topic_navigation_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **position** | **int**| position | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_using_put**
> add_using_put(article, page_id, domain, after=after, before=before)

add

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
article = 789 # int | article
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain
after = 789 # int | after (optional)
before = 789 # int | before (optional)

try:
    # add
    api_instance.add_using_put(article, page_id, domain, after=after, before=before)
except ApiException as e:
    print("Exception when calling PageControllerApi->add_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article** | **int**| article | 
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 
 **after** | **int**| after | [optional] 
 **before** | **int**| before | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_external_page_using_post**
> object create_external_page_using_post(body, domain)

createExternalPage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.Page() # Page | page
domain = 'domain_example' # str | Domain

try:
    # createExternalPage
    api_response = api_instance.create_external_page_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->create_external_page_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Page**](Page.md)| page | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_page_using_post**
> Page create_page_using_post(body, domain)

createPage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.Page() # Page | page
domain = 'domain_example' # str | Domain

try:
    # createPage
    api_response = api_instance.create_page_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->create_page_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Page**](Page.md)| page | 
 **domain** | **str**| Domain | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_articles_by_ids_using_post1**
> object find_all_articles_by_ids_using_post1(domain, body=body)

findAllArticlesByIds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain
body = swagger_client.OptionalListlong() # OptionalListlong | ids (optional)

try:
    # findAllArticlesByIds
    api_response = api_instance.find_all_articles_by_ids_using_post1(domain, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->find_all_articles_by_ids_using_post1: %s\n" % e)
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

# **get_all_designs_using_get**
> list[str] get_all_designs_using_get(domain)

getAllDesigns

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getAllDesigns
    api_response = api_instance.get_all_designs_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_all_designs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_market_topics_using_get**
> list[MarketTopicUrl] get_all_market_topics_using_get(domain)

getAllMarketTopics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getAllMarketTopics
    api_response = api_instance.get_all_market_topics_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_all_market_topics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**list[MarketTopicUrl]**](MarketTopicUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pages_using_get**
> list[Page] get_all_pages_using_get(domain, page=page, size=size)

getAllPages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain
page = 56 # int | page (optional)
size = 56 # int | size (optional)

try:
    # getAllPages
    api_response = api_instance.get_all_pages_using_get(domain, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_all_pages_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **page** | **int**| page | [optional] 
 **size** | **int**| size | [optional] 

### Return type

[**list[Page]**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_topics_using_get**
> list[Page] get_all_topics_using_get(domain, page=page, size=size)

getAllTopics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain
page = 56 # int | page (optional)
size = 56 # int | size (optional)

try:
    # getAllTopics
    api_response = api_instance.get_all_topics_using_get(domain, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_all_topics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **page** | **int**| page | [optional] 
 **size** | **int**| size | [optional] 

### Return type

[**list[Page]**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_articles_using_get**
> list[Article] get_articles_using_get(page_id, page, size, domain)

getArticles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
page = 56 # int | page
size = 56 # int | size
domain = 'domain_example' # str | Domain

try:
    # getArticles
    api_response = api_instance.get_articles_using_get(page_id, page, size, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_articles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **page** | **int**| page | 
 **size** | **int**| size | 
 **domain** | **str**| Domain | 

### Return type

[**list[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footer_navigation_using_get**
> FooterNavigation get_footer_navigation_using_get(domain)

getFooterNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getFooterNavigation
    api_response = api_instance.get_footer_navigation_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_footer_navigation_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**FooterNavigation**](FooterNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_meta_using_get**
> PageMeta get_page_meta_using_get(domain)

getPageMeta

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getPageMeta
    api_response = api_instance.get_page_meta_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_page_meta_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**PageMeta**](PageMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_template_using_get**
> PageTemplate get_page_template_using_get(template_id, domain)

getPageTemplate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
template_id = 'template_id_example' # str | templateId
domain = 'domain_example' # str | Domain

try:
    # getPageTemplate
    api_response = api_instance.get_page_template_using_get(template_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_page_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| templateId | 
 **domain** | **str**| Domain | 

### Return type

[**PageTemplate**](PageTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_using_get**
> object get_page_using_get(page_id, domain)

getPage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain

try:
    # getPage
    api_response = api_instance.get_page_using_get(page_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_page_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_navigation_nav_type_using_get**
> LevelNavigation get_section_navigation_nav_type_using_get(domain, nav_type)

getSectionNavigationNavType

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain
nav_type = 'nav_type_example' # str | navType

try:
    # getSectionNavigationNavType
    api_response = api_instance.get_section_navigation_nav_type_using_get(domain, nav_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_section_navigation_nav_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **nav_type** | **str**| navType | 

### Return type

[**LevelNavigation**](LevelNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_navigation_using_get**
> SectionNavigation get_section_navigation_using_get(domain)

getSectionNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getSectionNavigation
    api_response = api_instance.get_section_navigation_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_section_navigation_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**SectionNavigation**](SectionNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_using_get**
> list[Page] get_sections_using_get(domain, page=page, size=size)

getSections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain
page = 56 # int | page (optional)
size = 56 # int | size (optional)

try:
    # getSections
    api_response = api_instance.get_sections_using_get(domain, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_sections_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **page** | **int**| page | [optional] 
 **size** | **int**| size | [optional] 

### Return type

[**list[Page]**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_sections_by_section_using_get**
> list[Page] get_sub_sections_by_section_using_get(section_id, domain)

getSubSectionsBySection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
section_id = 789 # int | sectionId
domain = 'domain_example' # str | Domain

try:
    # getSubSectionsBySection
    api_response = api_instance.get_sub_sections_by_section_using_get(section_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_sub_sections_by_section_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **int**| sectionId | 
 **domain** | **str**| Domain | 

### Return type

[**list[Page]**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_navigation_using_get**
> TopicNavigation get_topic_navigation_using_get(domain)

getTopicNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getTopicNavigation
    api_response = api_instance.get_topic_navigation_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->get_topic_navigation_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**TopicNavigation**](TopicNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_purge_using_post**
> object page_purge_using_post(id, domain, authorization)

pagePurge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain
authorization = 'authorization_example' # str | Authorization

try:
    # pagePurge
    api_response = api_instance.page_purge_using_post(id, domain, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->page_purge_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain** | **str**| Domain | 
 **authorization** | **str**| Authorization | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_article_using_delete**
> remove_article_using_delete(article, page_id, domain)

removeArticle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
article = 789 # int | article
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain

try:
    # removeArticle
    api_instance.remove_article_using_delete(article, page_id, domain)
except ApiException as e:
    print("Exception when calling PageControllerApi->remove_article_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article** | **int**| article | 
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_section_navigation_using_delete**
> remove_from_section_navigation_using_delete(page_id, domain, auto_save=auto_save)

removeFromSectionNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # removeFromSectionNavigation
    api_instance.remove_from_section_navigation_using_delete(page_id, domain, auto_save=auto_save)
except ApiException as e:
    print("Exception when calling PageControllerApi->remove_from_section_navigation_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_topic_navigation_using_delete**
> remove_from_topic_navigation_using_delete(page_id, domain, auto_save=auto_save)

removeFromTopicNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # removeFromTopicNavigation
    api_instance.remove_from_topic_navigation_using_delete(page_id, domain, auto_save=auto_save)
except ApiException as e:
    print("Exception when calling PageControllerApi->remove_from_topic_navigation_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_page_using_delete**
> remove_page_using_delete(page_id, domain)

removePage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
page_id = 789 # int | pageId
domain = 'domain_example' # str | Domain

try:
    # removePage
    api_instance.remove_page_using_delete(page_id, domain)
except ApiException as e:
    print("Exception when calling PageControllerApi->remove_page_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**| pageId | 
 **domain** | **str**| Domain | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_footer_navigation_using_post**
> FooterNavigation save_footer_navigation_using_post(body, domain, auto_save=auto_save)

saveFooterNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.FooterNavigation() # FooterNavigation | navigation
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # saveFooterNavigation
    api_response = api_instance.save_footer_navigation_using_post(body, domain, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->save_footer_navigation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FooterNavigation**](FooterNavigation.md)| navigation | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

[**FooterNavigation**](FooterNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_section_navigation_nav_type_using_post**
> LevelNavigation save_section_navigation_nav_type_using_post(body, domain, auto_save=auto_save)

saveSectionNavigationNavType

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.LevelNavigation() # LevelNavigation | navigation
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # saveSectionNavigationNavType
    api_response = api_instance.save_section_navigation_nav_type_using_post(body, domain, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->save_section_navigation_nav_type_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LevelNavigation**](LevelNavigation.md)| navigation | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

[**LevelNavigation**](LevelNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_section_navigation_using_post**
> SectionNavigation save_section_navigation_using_post(body, domain, auto_save=auto_save)

saveSectionNavigation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.SectionNavigation() # SectionNavigation | navigation
domain = 'domain_example' # str | Domain
auto_save = true # bool | autoSave (optional)

try:
    # saveSectionNavigation
    api_response = api_instance.save_section_navigation_using_post(body, domain, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->save_section_navigation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SectionNavigation**](SectionNavigation.md)| navigation | 
 **domain** | **str**| Domain | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

[**SectionNavigation**](SectionNavigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_page_using_get**
> PagePage search_page_using_get(params, domain)

searchPage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # searchPage
    api_response = api_instance.search_page_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->search_page_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

[**PagePage**](PagePage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_and_save_all_pages_using_post**
> list[int] update_and_save_all_pages_using_post(domain)

updateAndSaveAllPages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
domain = 'domain_example' # str | Domain

try:
    # updateAndSaveAllPages
    api_response = api_instance.update_and_save_all_pages_using_post(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->update_and_save_all_pages_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_page_using_put**
> object update_external_page_using_put(body, domain, page_id)

updateExternalPage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.Page() # Page | page
domain = 'domain_example' # str | Domain
page_id = 789 # int | pageId

try:
    # updateExternalPage
    api_response = api_instance.update_external_page_using_put(body, domain, page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->update_external_page_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Page**](Page.md)| page | 
 **domain** | **str**| Domain | 
 **page_id** | **int**| pageId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_page_using_put**
> Page update_page_using_put(body, domain, page_id, auto_save=auto_save)

updatePage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PageControllerApi()
body = swagger_client.Page() # Page | page
domain = 'domain_example' # str | Domain
page_id = 789 # int | pageId
auto_save = true # bool | autoSave (optional)

try:
    # updatePage
    api_response = api_instance.update_page_using_put(body, domain, page_id, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageControllerApi->update_page_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Page**](Page.md)| page | 
 **domain** | **str**| Domain | 
 **page_id** | **int**| pageId | 
 **auto_save** | **bool**| autoSave | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

