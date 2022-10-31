# swagger_client.DashboardControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_using_get**](DashboardControllerApi.md#find_all_using_get) | **GET** /api/cms/search/{type} | cards
[**get_dashboard_meta_search_using_get**](DashboardControllerApi.md#get_dashboard_meta_search_using_get) | **GET** /api/cms/dashboard/meta/search | getDashboardMetaSearch
[**get_dashboard_using_get**](DashboardControllerApi.md#get_dashboard_using_get) | **GET** /api/cms/dashboard/meta | getDashboard
[**get_element_dashboard_using_get**](DashboardControllerApi.md#get_element_dashboard_using_get) | **GET** /api/cms/element/meta | getElementDashboard
[**get_workspace_metadata_search_using_get**](DashboardControllerApi.md#get_workspace_metadata_search_using_get) | **GET** /api/cms/workspace/meta/search | getWorkspaceMetadataSearch
[**get_workspace_metadata_using_get**](DashboardControllerApi.md#get_workspace_metadata_using_get) | **GET** /api/cms/workspace/meta | getWorkspaceMetadata

# **find_all_using_get**
> object find_all_using_get(params, type, domain)

cards

This endpoint can be used for searching, filtering and sorting of the stories.It recognises four parameters by default(page, size, sort, search). You can have as many sort parameters as you want but there must be only one page, size and search paramater each.The page and size parameter must be an integer.The sort parameter must be the fieldname and comma-seprated sort order(asc, desc). If no sort order is mentioned then it takes asc by default.The search parameter must have comma-separated value such as (fieldName):(fieldValue).The allowed operations are equals(:), less than, greater than, prefix-matching(~) and not(!).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardControllerApi()
params = NULL # object | params
type = 'type_example' # str | type
domain = 'domain_example' # str | Domain

try:
    # cards
    api_response = api_instance.find_all_using_get(params, type, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->find_all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**object**](.md)| params | 
 **type** | **str**| type | 
 **domain** | **str**| Domain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_meta_search_using_get**
> object get_dashboard_meta_search_using_get(field, domain, text=text)

getDashboardMetaSearch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardControllerApi()
field = 'field_example' # str | field
domain = 'domain_example' # str | Domain
text = 'text_example' # str | text (optional)

try:
    # getDashboardMetaSearch
    api_response = api_instance.get_dashboard_meta_search_using_get(field, domain, text=text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboard_meta_search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| field | 
 **domain** | **str**| Domain | 
 **text** | **str**| text | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_using_get**
> object get_dashboard_using_get(domain)

getDashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getDashboard
    api_response = api_instance.get_dashboard_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboard_using_get: %s\n" % e)
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

# **get_element_dashboard_using_get**
> object get_element_dashboard_using_get(domain)

getElementDashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getElementDashboard
    api_response = api_instance.get_element_dashboard_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_element_dashboard_using_get: %s\n" % e)
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

# **get_workspace_metadata_search_using_get**
> object get_workspace_metadata_search_using_get(field, domain, text=text)

getWorkspaceMetadataSearch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardControllerApi()
field = 'field_example' # str | field
domain = 'domain_example' # str | Domain
text = 'text_example' # str | text (optional)

try:
    # getWorkspaceMetadataSearch
    api_response = api_instance.get_workspace_metadata_search_using_get(field, domain, text=text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_workspace_metadata_search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| field | 
 **domain** | **str**| Domain | 
 **text** | **str**| text | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_metadata_using_get**
> object get_workspace_metadata_using_get(domain)

getWorkspaceMetadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getWorkspaceMetadata
    api_response = api_instance.get_workspace_metadata_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_workspace_metadata_using_get: %s\n" % e)
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

