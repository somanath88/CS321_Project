# openapi_client.MealPlanningApi

All URIs are relative to *https://api.spoonacular.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_meal_plan_template**](MealPlanningApi.md#add_meal_plan_template) | **POST** /mealplanner/{username}/templates | Add Meal Plan Template
[**add_to_meal_plan**](MealPlanningApi.md#add_to_meal_plan) | **POST** /mealplanner/{username}/items | Add to Meal Plan
[**add_to_shopping_list**](MealPlanningApi.md#add_to_shopping_list) | **POST** /mealplanner/{username}/shopping-list/items | Add to Shopping List
[**clear_meal_plan_day**](MealPlanningApi.md#clear_meal_plan_day) | **DELETE** /mealplanner/{username}/day/{date} | Clear Meal Plan Day
[**connect_user**](MealPlanningApi.md#connect_user) | **POST** /users/connect | Connect User
[**delete_from_meal_plan**](MealPlanningApi.md#delete_from_meal_plan) | **DELETE** /mealplanner/{username}/items/{id} | Delete from Meal Plan
[**delete_from_shopping_list**](MealPlanningApi.md#delete_from_shopping_list) | **DELETE** /mealplanner/{username}/shopping-list/items/{id} | Delete from Shopping List
[**delete_meal_plan_template**](MealPlanningApi.md#delete_meal_plan_template) | **DELETE** /mealplanner/{username}/templates/{id} | Delete Meal Plan Template
[**generate_meal_plan**](MealPlanningApi.md#generate_meal_plan) | **GET** /mealplanner/generate | Generate Meal Plan
[**generate_shopping_list**](MealPlanningApi.md#generate_shopping_list) | **POST** /mealplanner/{username}/shopping-list/{start-date}/{end-date} | Generate Shopping List
[**get_meal_plan_template**](MealPlanningApi.md#get_meal_plan_template) | **GET** /mealplanner/{username}/templates/{id} | Get Meal Plan Template
[**get_meal_plan_templates**](MealPlanningApi.md#get_meal_plan_templates) | **GET** /mealplanner/{username}/templates | Get Meal Plan Templates
[**get_meal_plan_week**](MealPlanningApi.md#get_meal_plan_week) | **GET** /mealplanner/{username}/week/{start-date} | Get Meal Plan Week
[**get_shopping_list**](MealPlanningApi.md#get_shopping_list) | **GET** /mealplanner/{username}/shopping-list | Get Shopping List


# **add_meal_plan_template**
> AddMealPlanTemplate200Response add_meal_plan_template(username, hash, add_to_meal_plan_request)

Add Meal Plan Template

Add a meal plan template for a user.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.add_meal_plan_template200_response import AddMealPlanTemplate200Response
from openapi_client.model.add_to_meal_plan_request import AddToMealPlanRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    hash = "4b5v4398573406" # str | The private hash for the username.
    add_to_meal_plan_request = AddToMealPlanRequest(
        username="dsky",
        hash="4b5v4398573406",
    ) # AddToMealPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add Meal Plan Template
        api_response = api_instance.add_meal_plan_template(username, hash, add_to_meal_plan_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->add_meal_plan_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **hash** | **str**| The private hash for the username. |
 **add_to_meal_plan_request** | [**AddToMealPlanRequest**](AddToMealPlanRequest.md)|  |

### Return type

[**AddMealPlanTemplate200Response**](AddMealPlanTemplate200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: 
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_to_meal_plan**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_to_meal_plan(username, hash, add_to_meal_plan_request)

Add to Meal Plan

Add an item to the user's meal plan.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.add_to_meal_plan_request import AddToMealPlanRequest
from openapi_client.model.add_to_meal_plan_request1 import AddToMealPlanRequest1
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    hash = "hash_example" # str | The private hash for the username.
    add_to_meal_plan_request = AddToMealPlanRequest(
        username="dsky",
        hash="4b5v4398573406",
    ) # AddToMealPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add to Meal Plan
        api_response = api_instance.add_to_meal_plan(username, hash, add_to_meal_plan_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->add_to_meal_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **hash** | **str**| The private hash for the username. |
 **add_to_meal_plan_request** | [**AddToMealPlanRequest**](AddToMealPlanRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: , application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_to_shopping_list**
> GenerateShoppingList200Response add_to_shopping_list(username, hash, add_to_meal_plan_request)

Add to Shopping List

Add an item to the current shopping list of a user.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.generate_shopping_list200_response import GenerateShoppingList200Response
from openapi_client.model.add_to_shopping_list_request import AddToShoppingListRequest
from openapi_client.model.add_to_meal_plan_request import AddToMealPlanRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    hash = "hash_example" # str | The private hash for the username.
    add_to_meal_plan_request = AddToMealPlanRequest(
        username="dsky",
        hash="4b5v4398573406",
    ) # AddToMealPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add to Shopping List
        api_response = api_instance.add_to_shopping_list(username, hash, add_to_meal_plan_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->add_to_shopping_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **hash** | **str**| The private hash for the username. |
 **add_to_meal_plan_request** | [**AddToMealPlanRequest**](AddToMealPlanRequest.md)|  |

### Return type

[**GenerateShoppingList200Response**](GenerateShoppingList200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: , application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_meal_plan_day**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} clear_meal_plan_day(username, date, hash, clear_meal_plan_day_request)

Clear Meal Plan Day

Delete all planned items from the user's meal plan for a specific day.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.clear_meal_plan_day_request import ClearMealPlanDayRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    date = "2020-06-01" # str | The date in the format yyyy-mm-dd.
    hash = "hash_example" # str | The private hash for the username.
    clear_meal_plan_day_request = ClearMealPlanDayRequest(
        username="dsky",
        date="2020-06-01",
        hash="4b5v4398573406",
    ) # ClearMealPlanDayRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Clear Meal Plan Day
        api_response = api_instance.clear_meal_plan_day(username, date, hash, clear_meal_plan_day_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->clear_meal_plan_day: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **date** | **str**| The date in the format yyyy-mm-dd. |
 **hash** | **str**| The private hash for the username. |
 **clear_meal_plan_day_request** | [**ClearMealPlanDayRequest**](ClearMealPlanDayRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: 
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_user**
> ConnectUser200Response connect_user(body)

Connect User

In order to call user-specific endpoints, you need to connect your app's users to spoonacular users.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.connect_user_request import ConnectUserRequest
from openapi_client.model.connect_user200_response import ConnectUser200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Connect User
        api_response = api_instance.connect_user(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->connect_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**ConnectUser200Response**](ConnectUser200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: , application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_from_meal_plan**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_from_meal_plan(username, id, hash, delete_from_meal_plan_request)

Delete from Meal Plan

Delete an item from the user's meal plan.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.delete_from_meal_plan_request import DeleteFromMealPlanRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    id = 15678 # float | The shopping list item id.
    hash = "hash_example" # str | The private hash for the username.
    delete_from_meal_plan_request = DeleteFromMealPlanRequest(
        username="dsky",
        id=15678,
        hash="4b5v4398573406",
    ) # DeleteFromMealPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete from Meal Plan
        api_response = api_instance.delete_from_meal_plan(username, id, hash, delete_from_meal_plan_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->delete_from_meal_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **id** | **float**| The shopping list item id. |
 **hash** | **str**| The private hash for the username. |
 **delete_from_meal_plan_request** | [**DeleteFromMealPlanRequest**](DeleteFromMealPlanRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: 
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_from_shopping_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_from_shopping_list(username, id, hash, delete_from_meal_plan_request)

Delete from Shopping List

Delete an item from the current shopping list of the user.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.delete_from_meal_plan_request import DeleteFromMealPlanRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    id = 1 # int | The item's id.
    hash = "hash_example" # str | The private hash for the username.
    delete_from_meal_plan_request = DeleteFromMealPlanRequest(
        username="dsky",
        id=15678,
        hash="4b5v4398573406",
    ) # DeleteFromMealPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete from Shopping List
        api_response = api_instance.delete_from_shopping_list(username, id, hash, delete_from_meal_plan_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->delete_from_shopping_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **id** | **int**| The item&#39;s id. |
 **hash** | **str**| The private hash for the username. |
 **delete_from_meal_plan_request** | [**DeleteFromMealPlanRequest**](DeleteFromMealPlanRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: 
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meal_plan_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_meal_plan_template(username, id, hash, delete_from_meal_plan_request)

Delete Meal Plan Template

Delete a meal plan template for a user.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.delete_from_meal_plan_request import DeleteFromMealPlanRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    id = 1 # int | The item's id.
    hash = "4b5v4398573406" # str | The private hash for the username.
    delete_from_meal_plan_request = DeleteFromMealPlanRequest(
        username="dsky",
        id=15678,
        hash="4b5v4398573406",
    ) # DeleteFromMealPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Meal Plan Template
        api_response = api_instance.delete_meal_plan_template(username, id, hash, delete_from_meal_plan_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->delete_meal_plan_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **id** | **int**| The item&#39;s id. |
 **hash** | **str**| The private hash for the username. |
 **delete_from_meal_plan_request** | [**DeleteFromMealPlanRequest**](DeleteFromMealPlanRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: 
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_meal_plan**
> GenerateMealPlan200Response generate_meal_plan()

Generate Meal Plan

Generate a meal plan with three meals per day (breakfast, lunch, and dinner).

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.generate_meal_plan200_response import GenerateMealPlan200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    time_frame = "day" # str | Either for one \"day\" or an entire \"week\". (optional)
    target_calories = 2000 # float | What is the caloric target for one day? The meal plan generator will try to get as close as possible to that goal. (optional)
    diet = "vegetarian" # str | Enter a diet that the meal plan has to adhere to. See a full list of supported diets. (optional)
    exclude = "shellfish, olives" # str | A comma-separated list of allergens or ingredients that must be excluded. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate Meal Plan
        api_response = api_instance.generate_meal_plan(time_frame=time_frame, target_calories=target_calories, diet=diet, exclude=exclude)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->generate_meal_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_frame** | **str**| Either for one \&quot;day\&quot; or an entire \&quot;week\&quot;. | [optional]
 **target_calories** | **float**| What is the caloric target for one day? The meal plan generator will try to get as close as possible to that goal. | [optional]
 **diet** | **str**| Enter a diet that the meal plan has to adhere to. See a full list of supported diets. | [optional]
 **exclude** | **str**| A comma-separated list of allergens or ingredients that must be excluded. | [optional]

### Return type

[**GenerateMealPlan200Response**](GenerateMealPlan200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_shopping_list**
> GenerateShoppingList200Response generate_shopping_list(username, start_date, end_date, hash, generate_shopping_list_request)

Generate Shopping List

Generate the shopping list for a user from the meal planner in a given time frame.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.generate_shopping_list200_response import GenerateShoppingList200Response
from openapi_client.model.generate_shopping_list_request import GenerateShoppingListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    start_date = "2020-06-01" # str | The start date in the format yyyy-mm-dd.
    end_date = "2020-06-07" # str | The end date in the format yyyy-mm-dd.
    hash = "hash_example" # str | The private hash for the username.
    generate_shopping_list_request = GenerateShoppingListRequest(
        username="dsky",
        start_date="2020-06-01",
        end_date="2020-06-07",
        hash="4b5v4398573406",
    ) # GenerateShoppingListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Shopping List
        api_response = api_instance.generate_shopping_list(username, start_date, end_date, hash, generate_shopping_list_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->generate_shopping_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **start_date** | **str**| The start date in the format yyyy-mm-dd. |
 **end_date** | **str**| The end date in the format yyyy-mm-dd. |
 **hash** | **str**| The private hash for the username. |
 **generate_shopping_list_request** | [**GenerateShoppingListRequest**](GenerateShoppingListRequest.md)|  |

### Return type

[**GenerateShoppingList200Response**](GenerateShoppingList200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: 
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meal_plan_template**
> GetMealPlanTemplate200Response get_meal_plan_template(username, id, hash)

Get Meal Plan Template

Get information about a meal plan template.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.get_meal_plan_template200_response import GetMealPlanTemplate200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    id = 1 # int | The item's id.
    hash = "hash_example" # str | The private hash for the username.

    # example passing only required values which don't have defaults set
    try:
        # Get Meal Plan Template
        api_response = api_instance.get_meal_plan_template(username, id, hash)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->get_meal_plan_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **id** | **int**| The item&#39;s id. |
 **hash** | **str**| The private hash for the username. |

### Return type

[**GetMealPlanTemplate200Response**](GetMealPlanTemplate200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meal_plan_templates**
> GetMealPlanTemplates200Response get_meal_plan_templates(username, hash)

Get Meal Plan Templates

Get meal plan templates from user or public ones.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.get_meal_plan_templates200_response import GetMealPlanTemplates200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    hash = "hash_example" # str | The private hash for the username.

    # example passing only required values which don't have defaults set
    try:
        # Get Meal Plan Templates
        api_response = api_instance.get_meal_plan_templates(username, hash)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->get_meal_plan_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **hash** | **str**| The private hash for the username. |

### Return type

[**GetMealPlanTemplates200Response**](GetMealPlanTemplates200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meal_plan_week**
> GetMealPlanWeek200Response get_meal_plan_week(username, start_date, hash)

Get Meal Plan Week

Retrieve a meal planned week for the given user. The username must be a spoonacular user and the hash must the the user's hash that can be found in his/her account.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.get_meal_plan_week200_response import GetMealPlanWeek200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    start_date = "2020-06-01" # str | The start date of the meal planned week in the format yyyy-mm-dd.
    hash = "hash_example" # str | The private hash for the username.

    # example passing only required values which don't have defaults set
    try:
        # Get Meal Plan Week
        api_response = api_instance.get_meal_plan_week(username, start_date, hash)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->get_meal_plan_week: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **start_date** | **str**| The start date of the meal planned week in the format yyyy-mm-dd. |
 **hash** | **str**| The private hash for the username. |

### Return type

[**GetMealPlanWeek200Response**](GetMealPlanWeek200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_list**
> GetShoppingList200Response get_shopping_list(username, hash)

Get Shopping List

Get the current shopping list for the given user.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import meal_planning_api
from openapi_client.model.get_shopping_list200_response import GetShoppingList200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spoonacular.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meal_planning_api.MealPlanningApi(api_client)
    username = "dsky" # str | The username.
    hash = "hash_example" # str | The private hash for the username.

    # example passing only required values which don't have defaults set
    try:
        # Get Shopping List
        api_response = api_instance.get_shopping_list(username, hash)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MealPlanningApi->get_shopping_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. |
 **hash** | **str**| The private hash for the username. |

### Return type

[**GetShoppingList200Response**](GetShoppingList200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

