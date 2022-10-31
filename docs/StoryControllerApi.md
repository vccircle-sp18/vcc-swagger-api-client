# swagger_client.StoryControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_all_new_indices_using_post**](StoryControllerApi.md#add_all_new_indices_using_post) | **POST** /api/cms/story/market/add | addAllNewIndices
[**create_dead_link_story_using_post**](StoryControllerApi.md#create_dead_link_story_using_post) | **POST** /api/cms/story/deadlink | createDeadLinkStory
[**create_story_using_post**](StoryControllerApi.md#create_story_using_post) | **POST** /api/cms/story | createStory
[**delete_story_using_delete**](StoryControllerApi.md#delete_story_using_delete) | **DELETE** /api/cms/story/{id} | deleteStory
[**find_all_articles_by_ids_using_post2**](StoryControllerApi.md#find_all_articles_by_ids_using_post2) | **POST** /api/cms/story/get-all-by-ids/ | findAllArticlesByIds
[**find_all_stories_using_get**](StoryControllerApi.md#find_all_stories_using_get) | **GET** /api/cms/stories | stories
[**find_all_stories_using_get1**](StoryControllerApi.md#find_all_stories_using_get1) | **GET** /api/cms/story/all | findAllStories
[**find_web_story_templates_using_get**](StoryControllerApi.md#find_web_story_templates_using_get) | **GET** /api/cms/web-story/templates | findWebStoryTemplates
[**generate_url_using_post**](StoryControllerApi.md#generate_url_using_post) | **POST** /api/cms/story/url/generate | generateUrl
[**get_brand_products_list_using_get**](StoryControllerApi.md#get_brand_products_list_using_get) | **GET** /api/cms/story/brandproduct/{category} | getBrandProductsList
[**get_country_wise_states_using_get**](StoryControllerApi.md#get_country_wise_states_using_get) | **GET** /api/cms/story/editor/country | getCountryWiseStates
[**get_embed_code_using_get**](StoryControllerApi.md#get_embed_code_using_get) | **GET** /api/cms/story/embedcode | getEmbedCode
[**get_market_indices_using_get**](StoryControllerApi.md#get_market_indices_using_get) | **GET** /api/cms/story/market/indices | getMarketIndices
[**get_photo_gallery_using_get**](StoryControllerApi.md#get_photo_gallery_using_get) | **GET** /api/cms/photoGallery | getPhotoGallery
[**get_products_category_list_using_get**](StoryControllerApi.md#get_products_category_list_using_get) | **GET** /api/cms/story/productcategories | getProductsCategoryList
[**get_story_dashboard_search_suggestions_using_get**](StoryControllerApi.md#get_story_dashboard_search_suggestions_using_get) | **GET** /api/cms/story/suggestions | getStoryDashboardSearchSuggestions
[**get_story_editor_author_suggestions_using_get**](StoryControllerApi.md#get_story_editor_author_suggestions_using_get) | **GET** /api/cms/story/editor/authorsuggestions | getStoryEditorAuthorSuggestions
[**get_story_editor_cities_using_get**](StoryControllerApi.md#get_story_editor_cities_using_get) | **GET** /api/cms/story/editor/cities | getStoryEditorCities
[**get_story_editor_suggestions_using_get**](StoryControllerApi.md#get_story_editor_suggestions_using_get) | **GET** /api/cms/story/editor/suggestions | getStoryEditorSuggestions
[**get_story_status_using_get**](StoryControllerApi.md#get_story_status_using_get) | **GET** /api/cms/story/status/{id} | getStoryStatus
[**get_story_translation_using_post**](StoryControllerApi.md#get_story_translation_using_post) | **POST** /api/cms/story/translate/{id} | getStoryTranslation
[**get_story_using_get**](StoryControllerApi.md#get_story_using_get) | **GET** /api/cms/story/{id} | getStory
[**get_story_versions_using_get**](StoryControllerApi.md#get_story_versions_using_get) | **GET** /api/cms/story/versions/{storyId} | getStoryVersions
[**get_tags_topics_suggestions_using_get**](StoryControllerApi.md#get_tags_topics_suggestions_using_get) | **GET** /api/cms/story/topics/suggestions | getTagsTopicsSuggestions
[**get_topic_map_pages_using_get**](StoryControllerApi.md#get_topic_map_pages_using_get) | **GET** /api/cms/story/editor/topicmap | getTopicMapPages
[**get_topic_pages_using_get**](StoryControllerApi.md#get_topic_pages_using_get) | **GET** /api/cms/story/editor/topics | getTopicPages
[**market_indices_keyword_mapping_using_post**](StoryControllerApi.md#market_indices_keyword_mapping_using_post) | **POST** /api/cms/story/market/indices/keywordmapping | marketIndicesKeywordMapping
[**search_story_using_get**](StoryControllerApi.md#search_story_using_get) | **GET** /api/cms/search/story/{tags} | searchStory
[**show_related_using_put**](StoryControllerApi.md#show_related_using_put) | **PUT** /api/cms/story/update/{id} | showRelated
[**story_purge_using_post**](StoryControllerApi.md#story_purge_using_post) | **POST** /api/cms/purge/story/{id} | storyPurge
[**update_dead_link_story_using_put**](StoryControllerApi.md#update_dead_link_story_using_put) | **PUT** /api/cms/story/deadlink/{id} | updateDeadLinkStory
[**update_story_using_put**](StoryControllerApi.md#update_story_using_put) | **PUT** /api/cms/story/{id} | updateStory

# **add_all_new_indices_using_post**
> list[MarketIndices] add_all_new_indices_using_post(domain)

addAllNewIndices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # addAllNewIndices
    api_response = api_instance.add_all_new_indices_using_post(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->add_all_new_indices_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**list[MarketIndices]**](MarketIndices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dead_link_story_using_post**
> Article create_dead_link_story_using_post(body, domain)

createDeadLinkStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = swagger_client.Story() # Story | article
domain = 'domain_example' # str | Domain

try:
    # createDeadLinkStory
    api_response = api_instance.create_dead_link_story_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->create_dead_link_story_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| article | 
 **domain** | **str**| Domain | 

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_story_using_post**
> Article create_story_using_post(body, domain)

createStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = swagger_client.Story() # Story | article
domain = 'domain_example' # str | Domain

try:
    # createStory
    api_response = api_instance.create_story_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->create_story_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| article | 
 **domain** | **str**| Domain | 

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story_using_delete**
> object delete_story_using_delete(body, authorization, domain, id)

deleteStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = swagger_client.Story() # Story | story
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
id = 789 # int | id

try:
    # deleteStory
    api_response = api_instance.delete_story_using_delete(body, authorization, domain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->delete_story_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| story | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 
 **id** | **int**| id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_articles_by_ids_using_post2**
> object find_all_articles_by_ids_using_post2(domain, body=body)

findAllArticlesByIds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain
body = swagger_client.OptionalListlong() # OptionalListlong | ids (optional)

try:
    # findAllArticlesByIds
    api_response = api_instance.find_all_articles_by_ids_using_post2(domain, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->find_all_articles_by_ids_using_post2: %s\n" % e)
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

# **find_all_stories_using_get**
> object find_all_stories_using_get(params, domain)

stories

This endpoint can be used for searching, filtering and sorting of the stories.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # stories
    api_response = api_instance.find_all_stories_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->find_all_stories_using_get: %s\n" % e)
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

# **find_all_stories_using_get1**
> PageArticle find_all_stories_using_get1(domain)

findAllStories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # findAllStories
    api_response = api_instance.find_all_stories_using_get1(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->find_all_stories_using_get1: %s\n" % e)
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

# **find_web_story_templates_using_get**
> object find_web_story_templates_using_get(domain)

findWebStoryTemplates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # findWebStoryTemplates
    api_response = api_instance.find_web_story_templates_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->find_web_story_templates_using_get: %s\n" % e)
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

# **generate_url_using_post**
> str generate_url_using_post(body, domain)

generateUrl

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = swagger_client.UrlBodyDTO() # UrlBodyDTO | urlBody
domain = 'domain_example' # str | Domain

try:
    # generateUrl
    api_response = api_instance.generate_url_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->generate_url_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlBodyDTO**](UrlBodyDTO.md)| urlBody | 
 **domain** | **str**| Domain | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_products_list_using_get**
> dict(str, dict(str, list[str])) get_brand_products_list_using_get(category, domain, search_chars=search_chars)

getBrandProductsList

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
category = 'category_example' # str | category
domain = 'domain_example' # str | Domain
search_chars = 'search_chars_example' # str | searchChars (optional)

try:
    # getBrandProductsList
    api_response = api_instance.get_brand_products_list_using_get(category, domain, search_chars=search_chars)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_brand_products_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| category | 
 **domain** | **str**| Domain | 
 **search_chars** | **str**| searchChars | [optional] 

### Return type

**dict(str, dict(str, list[str]))**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_wise_states_using_get**
> dict(str, list[str]) get_country_wise_states_using_get(domain)

getCountryWiseStates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getCountryWiseStates
    api_response = api_instance.get_country_wise_states_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_country_wise_states_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

**dict(str, list[str])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embed_code_using_get**
> str get_embed_code_using_get(url_to_embed, domain)

getEmbedCode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
url_to_embed = 'url_to_embed_example' # str | urlToEmbed
domain = 'domain_example' # str | Domain

try:
    # getEmbedCode
    api_response = api_instance.get_embed_code_using_get(url_to_embed, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_embed_code_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_to_embed** | **str**| urlToEmbed | 
 **domain** | **str**| Domain | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_indices_using_get**
> list[MarketIndices] get_market_indices_using_get(domain, type, size=size)

getMarketIndices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain
type = 'type_example' # str | type
size = 200 # int | size (optional) (default to 200)

try:
    # getMarketIndices
    api_response = api_instance.get_market_indices_using_get(domain, type, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_market_indices_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **type** | **str**| type | 
 **size** | **int**| size | [optional] [default to 200]

### Return type

[**list[MarketIndices]**](MarketIndices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo_gallery_using_get**
> object get_photo_gallery_using_get(domain)

getPhotoGallery

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getPhotoGallery
    api_response = api_instance.get_photo_gallery_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_photo_gallery_using_get: %s\n" % e)
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

# **get_products_category_list_using_get**
> list[CategoryMaster] get_products_category_list_using_get(domain)

getProductsCategoryList

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getProductsCategoryList
    api_response = api_instance.get_products_category_list_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_products_category_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**list[CategoryMaster]**](CategoryMaster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_dashboard_search_suggestions_using_get**
> object get_story_dashboard_search_suggestions_using_get(text, domain)

getStoryDashboardSearchSuggestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
text = 'text_example' # str | text
domain = 'domain_example' # str | Domain

try:
    # getStoryDashboardSearchSuggestions
    api_response = api_instance.get_story_dashboard_search_suggestions_using_get(text, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_dashboard_search_suggestions_using_get: %s\n" % e)
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

# **get_story_editor_author_suggestions_using_get**
> StoryAutoAuthorSuggestions get_story_editor_author_suggestions_using_get(domain)

getStoryEditorAuthorSuggestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getStoryEditorAuthorSuggestions
    api_response = api_instance.get_story_editor_author_suggestions_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_editor_author_suggestions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**StoryAutoAuthorSuggestions**](StoryAutoAuthorSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_editor_cities_using_get**
> list[str] get_story_editor_cities_using_get(domain=domain)

getStoryEditorCities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain (optional)

try:
    # getStoryEditorCities
    api_response = api_instance.get_story_editor_cities_using_get(domain=domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_editor_cities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_editor_suggestions_using_get**
> StoryAutoSuggestions get_story_editor_suggestions_using_get(domain)

getStoryEditorSuggestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getStoryEditorSuggestions
    api_response = api_instance.get_story_editor_suggestions_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_editor_suggestions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 

### Return type

[**StoryAutoSuggestions**](StoryAutoSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_status_using_get**
> object get_story_status_using_get(id, domain)

getStoryStatus

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain

try:
    # getStoryStatus
    api_response = api_instance.get_story_status_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_status_using_get: %s\n" % e)
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

# **get_story_translation_using_post**
> TranslationWrapper get_story_translation_using_post(id, domain)

getStoryTranslation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain

try:
    # getStoryTranslation
    api_response = api_instance.get_story_translation_using_post(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_translation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain** | **str**| Domain | 

### Return type

[**TranslationWrapper**](TranslationWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_using_get**
> object get_story_using_get(id, domain)

getStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain

try:
    # getStory
    api_response = api_instance.get_story_using_get(id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_using_get: %s\n" % e)
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

# **get_story_versions_using_get**
> object get_story_versions_using_get(story_id, domain)

getStoryVersions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
story_id = 789 # int | storyId
domain = 'domain_example' # str | Domain

try:
    # getStoryVersions
    api_response = api_instance.get_story_versions_using_get(story_id, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_story_versions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_id** | **int**| storyId | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_topics_suggestions_using_get**
> list[object] get_tags_topics_suggestions_using_get(params, domain)

getTagsTopicsSuggestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # getTagsTopicsSuggestions
    api_response = api_instance.get_tags_topics_suggestions_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_tags_topics_suggestions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_map_pages_using_get**
> dict(str, str) get_topic_map_pages_using_get(params, domain)

getTopicMapPages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # getTopicMapPages
    api_response = api_instance.get_topic_map_pages_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_topic_map_pages_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_pages_using_get**
> list[str] get_topic_pages_using_get(params, domain)

getTopicPages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
params = NULL # object | params
domain = 'domain_example' # str | Domain

try:
    # getTopicPages
    api_response = api_instance.get_topic_pages_using_get(params, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->get_topic_pages_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **domain** | **str**| Domain | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_indices_keyword_mapping_using_post**
> list[MarketIndices] market_indices_keyword_mapping_using_post(body, authorization, domain)

marketIndicesKeywordMapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = [swagger_client.MarketIndicesKeywordNameMappingDTO()] # list[MarketIndicesKeywordNameMappingDTO] | marketIndiceskeywordNameList
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain

try:
    # marketIndicesKeywordMapping
    api_response = api_instance.market_indices_keyword_mapping_using_post(body, authorization, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->market_indices_keyword_mapping_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MarketIndicesKeywordNameMappingDTO]**](MarketIndicesKeywordNameMappingDTO.md)| marketIndiceskeywordNameList | 
 **authorization** | **str**| Authorization | 
 **domain** | **str**| Domain | 

### Return type

[**list[MarketIndices]**](MarketIndices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_story_using_get**
> object search_story_using_get(tags, domain)

searchStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
tags = 'tags_example' # str | tags
domain = 'domain_example' # str | Domain

try:
    # searchStory
    api_response = api_instance.search_story_using_get(tags, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->search_story_using_get: %s\n" % e)
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

# **show_related_using_put**
> Article show_related_using_put(id, domain, show_related)

showRelated

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain
show_related = true # bool | showRelated

try:
    # showRelated
    api_response = api_instance.show_related_using_put(id, domain, show_related)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->show_related_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **domain** | **str**| Domain | 
 **show_related** | **bool**| showRelated | 

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **story_purge_using_post**
> object story_purge_using_post(id, domain, authorization)

storyPurge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
id = 789 # int | id
domain = 'domain_example' # str | Domain
authorization = 'authorization_example' # str | Authorization

try:
    # storyPurge
    api_response = api_instance.story_purge_using_post(id, domain, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->story_purge_using_post: %s\n" % e)
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

# **update_dead_link_story_using_put**
> object update_dead_link_story_using_put(body, authorization, domain, id, auto_save=auto_save)

updateDeadLinkStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = swagger_client.Story() # Story | story
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
id = 789 # int | id
auto_save = true # bool | autoSave (optional)

try:
    # updateDeadLinkStory
    api_response = api_instance.update_dead_link_story_using_put(body, authorization, domain, id, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->update_dead_link_story_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| story | 
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

# **update_story_using_put**
> object update_story_using_put(body, authorization, domain, id, auto_save=auto_save)

updateStory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoryControllerApi()
body = swagger_client.Story() # Story | story
authorization = 'authorization_example' # str | Authorization
domain = 'domain_example' # str | Domain
id = 789 # int | id
auto_save = true # bool | autoSave (optional)

try:
    # updateStory
    api_response = api_instance.update_story_using_put(body, authorization, domain, id, auto_save=auto_save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoryControllerApi->update_story_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Story**](Story.md)| story | 
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

