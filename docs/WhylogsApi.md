# swagger_client.WhylogsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track**](WhylogsApi.md#track) | **POST** /logs | Log Data
[**track_pub_sub_message**](WhylogsApi.md#track_pub_sub_message) | **POST** /pubsubLogs | Track pub/sub messages
[**write_profiles**](WhylogsApi.md#write_profiles) | **POST** /writeProfiles | Write Profiles

# **track**
> track(body=body, x_api_key=x_api_key)

Log Data

Log a map of feature names and values or an array of data points

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WhylogsApi()
body = swagger_client.LogRequest() # LogRequest | 
Pass the input in single entry format or a multiple entry format.
- Set `single` key if you're passing a single data point with multiple features
- Set `multiple` key if you're passing multiple data at once.
The `multiple` format is is compatible with Pandas JSON output:
```
import pandas as pd
cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000] }
df = pd.DataFrame(cars, columns = ['Brand', 'Price'])
df.to_json(orient="split") # this is the value of `multiple`
```
Here is an example from the output above
```
{
    "datasetId": "demo-model",
    "timestamp": 1648162494947,
    "tags": {
        "tag1": "value1"
    },
    "multiple": {
        "columns": [
            "Brand",
            "Price"
        ],
        "data": [
            [ "Honda Civic", 22000 ],
            [ "Toyota Corolla", 25000 ],
            [ "Ford Focus", 27000 ],
            [ "Audi A4", 35000 ]
        ]
    }
}
```
 (optional)
x_api_key = 'x_api_key_example' # str |  (optional)

try:
    # Log Data
    api_instance.track(body=body, x_api_key=x_api_key)
except ApiException as e:
    print("Exception when calling WhylogsApi->track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogRequest**](LogRequest.md)| 
Pass the input in single entry format or a multiple entry format.
- Set &#x60;single&#x60; key if you&#x27;re passing a single data point with multiple features
- Set &#x60;multiple&#x60; key if you&#x27;re passing multiple data at once.
The &#x60;multiple&#x60; format is is compatible with Pandas JSON output:
&#x60;&#x60;&#x60;
import pandas as pd
cars &#x3D; {&#x27;Brand&#x27;: [&#x27;Honda Civic&#x27;,&#x27;Toyota Corolla&#x27;,&#x27;Ford Focus&#x27;,&#x27;Audi A4&#x27;],
        &#x27;Price&#x27;: [22000,25000,27000,35000] }
df &#x3D; pd.DataFrame(cars, columns &#x3D; [&#x27;Brand&#x27;, &#x27;Price&#x27;])
df.to_json(orient&#x3D;&quot;split&quot;) # this is the value of &#x60;multiple&#x60;
&#x60;&#x60;&#x60;
Here is an example from the output above
&#x60;&#x60;&#x60;
{
    &quot;datasetId&quot;: &quot;demo-model&quot;,
    &quot;timestamp&quot;: 1648162494947,
    &quot;tags&quot;: {
        &quot;tag1&quot;: &quot;value1&quot;
    },
    &quot;multiple&quot;: {
        &quot;columns&quot;: [
            &quot;Brand&quot;,
            &quot;Price&quot;
        ],
        &quot;data&quot;: [
            [ &quot;Honda Civic&quot;, 22000 ],
            [ &quot;Toyota Corolla&quot;, 25000 ],
            [ &quot;Ford Focus&quot;, 27000 ],
            [ &quot;Audi A4&quot;, 35000 ]
        ]
    }
}
&#x60;&#x60;&#x60;
 | [optional] 
 **x_api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_pub_sub_message**
> track_pub_sub_message(body=body, x_api_key=x_api_key)

Track pub/sub messages

Decode base64 encoded pub/sub message and track them

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WhylogsApi()
body = swagger_client.PubSubEnvelope() # PubSubEnvelope | 
                A Google Pub\Sub interface to tracking data. Does the same thing as /track except
                it consumes a message in the format that Pub\Sub uses.
 (optional)
x_api_key = 'x_api_key_example' # str |  (optional)

try:
    # Track pub/sub messages
    api_instance.track_pub_sub_message(body=body, x_api_key=x_api_key)
except ApiException as e:
    print("Exception when calling WhylogsApi->track_pub_sub_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PubSubEnvelope**](PubSubEnvelope.md)| 
                A Google Pub\Sub interface to tracking data. Does the same thing as /track except
                it consumes a message in the format that Pub\Sub uses.
 | [optional] 
 **x_api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_profiles**
> WriteProfilesResponse write_profiles(x_api_key=x_api_key)

Write Profiles

Force the container to write out the pending profiles via whatever method it's configured for.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WhylogsApi()
x_api_key = 'x_api_key_example' # str |  (optional)

try:
    # Write Profiles
    api_response = api_instance.write_profiles(x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhylogsApi->write_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 

### Return type

[**WriteProfilesResponse**](WriteProfilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

