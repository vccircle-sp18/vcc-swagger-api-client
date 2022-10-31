# swagger_client.MyUserDetailsControllerApi

All URIs are relative to *//10.136.172.13:6060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_details_using_get**](MyUserDetailsControllerApi.md#get_user_details_using_get) | **GET** /api/cms/user/details | getUserDetails
[**save_user_details_using_post**](MyUserDetailsControllerApi.md#save_user_details_using_post) | **POST** /api/cms/user/details | saveUserDetails
[**update_user_details_using_put**](MyUserDetailsControllerApi.md#update_user_details_using_put) | **PUT** /api/cms/user/details/{id} | updateUserDetails

# **get_user_details_using_get**
> object get_user_details_using_get(domain)

getUserDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MyUserDetailsControllerApi()
domain = 'domain_example' # str | Domain

try:
    # getUserDetails
    api_response = api_instance.get_user_details_using_get(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyUserDetailsControllerApi->get_user_details_using_get: %s\n" % e)
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

# **save_user_details_using_post**
> MyUserDetails save_user_details_using_post(body, domain)

saveUserDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MyUserDetailsControllerApi()
body = swagger_client.MyUserDetails() # MyUserDetails | userDetails
domain = 'domain_example' # str | Domain

try:
    # saveUserDetails
    api_response = api_instance.save_user_details_using_post(body, domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyUserDetailsControllerApi->save_user_details_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MyUserDetails**](MyUserDetails.md)| userDetails | 
 **domain** | **str**| Domain | 

### Return type

[**MyUserDetails**](MyUserDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_details_using_put**
> MyUserDetails update_user_details_using_put(body, domain, id)

updateUserDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MyUserDetailsControllerApi()
body = swagger_client.MyUserDetails() # MyUserDetails | userDetails
domain = 'domain_example' # str | Domain
id = 789 # int | id

try:
    # updateUserDetails
    api_response = api_instance.update_user_details_using_put(body, domain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyUserDetailsControllerApi->update_user_details_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MyUserDetails**](MyUserDetails.md)| userDetails | 
 **domain** | **str**| Domain | 
 **id** | **int**| id | 

### Return type

[**MyUserDetails**](MyUserDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

