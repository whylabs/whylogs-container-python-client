# swagger_client.DebugApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](DebugApi.md#health) | **GET** /health | Tell if the http server is healthy.
[**log_debug_info**](DebugApi.md#log_debug_info) | **POST** /logDebugInfo | Log Debug Info

# **health**
> health()

Tell if the http server is healthy.

Tell if the http server is healthy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()

try:
    # Tell if the http server is healthy.
    api_instance.health()
except ApiException as e:
    print("Exception when calling DebugApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_debug_info**
> log_debug_info(x_api_key=x_api_key)

Log Debug Info

Trigger debugging info to be logged.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
x_api_key = 'x_api_key_example' # str |  (optional)

try:
    # Log Debug Info
    api_instance.log_debug_info(x_api_key=x_api_key)
except ApiException as e:
    print("Exception when calling DebugApi->log_debug_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

