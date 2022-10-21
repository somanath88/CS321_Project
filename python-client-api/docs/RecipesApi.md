# openapi_client.RecipesApi

All URIs are relative to *https://api.spoonacular.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_a_recipe_search_query**](RecipesApi.md#analyze_a_recipe_search_query) | **GET** /recipes/queries/analyze | Analyze a Recipe Search Query
[**analyze_recipe_instructions**](RecipesApi.md#analyze_recipe_instructions) | **POST** /recipes/analyzeInstructions | Analyze Recipe Instructions
[**autocomplete_recipe_search**](RecipesApi.md#autocomplete_recipe_search) | **GET** /recipes/autocomplete | Autocomplete Recipe Search
[**classify_cuisine**](RecipesApi.md#classify_cuisine) | **POST** /recipes/cuisine | Classify Cuisine
[**compute_glycemic_load**](RecipesApi.md#compute_glycemic_load) | **POST** /food/ingredients/glycemicLoad | Compute Glycemic Load
[**convert_amounts**](RecipesApi.md#convert_amounts) | **GET** /recipes/convert | Convert Amounts
[**create_recipe_card**](RecipesApi.md#create_recipe_card) | **POST** /recipes/visualizeRecipe | Create Recipe Card
[**equipment_by_id_image**](RecipesApi.md#equipment_by_id_image) | **GET** /recipes/{id}/equipmentWidget.png | Equipment by ID Image
[**extract_recipe_from_website**](RecipesApi.md#extract_recipe_from_website) | **GET** /recipes/extract | Extract Recipe from Website
[**get_analyzed_recipe_instructions**](RecipesApi.md#get_analyzed_recipe_instructions) | **GET** /recipes/{id}/analyzedInstructions | Get Analyzed Recipe Instructions
[**get_random_recipes**](RecipesApi.md#get_random_recipes) | **GET** /recipes/random | Get Random Recipes
[**get_recipe_equipment_by_id**](RecipesApi.md#get_recipe_equipment_by_id) | **GET** /recipes/{id}/equipmentWidget.json | Equipment by ID
[**get_recipe_information**](RecipesApi.md#get_recipe_information) | **GET** /recipes/{id}/information | Get Recipe Information
[**get_recipe_information_bulk**](RecipesApi.md#get_recipe_information_bulk) | **GET** /recipes/informationBulk | Get Recipe Information Bulk
[**get_recipe_ingredients_by_id**](RecipesApi.md#get_recipe_ingredients_by_id) | **GET** /recipes/{id}/ingredientWidget.json | Ingredients by ID
[**get_recipe_nutrition_widget_by_id**](RecipesApi.md#get_recipe_nutrition_widget_by_id) | **GET** /recipes/{id}/nutritionWidget.json | Nutrition by ID
[**get_recipe_price_breakdown_by_id**](RecipesApi.md#get_recipe_price_breakdown_by_id) | **GET** /recipes/{id}/priceBreakdownWidget.json | Price Breakdown by ID
[**get_recipe_taste_by_id**](RecipesApi.md#get_recipe_taste_by_id) | **GET** /recipes/{id}/tasteWidget.json | Taste by ID
[**get_similar_recipes**](RecipesApi.md#get_similar_recipes) | **GET** /recipes/{id}/similar | Get Similar Recipes
[**guess_nutrition_by_dish_name**](RecipesApi.md#guess_nutrition_by_dish_name) | **GET** /recipes/guessNutrition | Guess Nutrition by Dish Name
[**ingredients_by_id_image**](RecipesApi.md#ingredients_by_id_image) | **GET** /recipes/{id}/ingredientWidget.png | Ingredients by ID Image
[**parse_ingredients**](RecipesApi.md#parse_ingredients) | **POST** /recipes/parseIngredients | Parse Ingredients
[**price_breakdown_by_id_image**](RecipesApi.md#price_breakdown_by_id_image) | **GET** /recipes/{id}/priceBreakdownWidget.png | Price Breakdown by ID Image
[**quick_answer**](RecipesApi.md#quick_answer) | **GET** /recipes/quickAnswer | Quick Answer
[**recipe_nutrition_by_id_image**](RecipesApi.md#recipe_nutrition_by_id_image) | **GET** /recipes/{id}/nutritionWidget.png | Recipe Nutrition by ID Image
[**recipe_nutrition_label_image**](RecipesApi.md#recipe_nutrition_label_image) | **GET** /recipes/{id}/nutritionLabel.png | Recipe Nutrition Label Image
[**recipe_nutrition_label_widget**](RecipesApi.md#recipe_nutrition_label_widget) | **GET** /recipes/{id}/nutritionLabel | Recipe Nutrition Label Widget
[**recipe_taste_by_id_image**](RecipesApi.md#recipe_taste_by_id_image) | **GET** /recipes/{id}/tasteWidget.png | Recipe Taste by ID Image
[**search_recipes**](RecipesApi.md#search_recipes) | **GET** /recipes/complexSearch | Search Recipes
[**search_recipes_by_ingredients**](RecipesApi.md#search_recipes_by_ingredients) | **GET** /recipes/findByIngredients | Search Recipes by Ingredients
[**search_recipes_by_nutrients**](RecipesApi.md#search_recipes_by_nutrients) | **GET** /recipes/findByNutrients | Search Recipes by Nutrients
[**summarize_recipe**](RecipesApi.md#summarize_recipe) | **GET** /recipes/{id}/summary | Summarize Recipe
[**visualize_equipment**](RecipesApi.md#visualize_equipment) | **POST** /recipes/visualizeEquipment | Equipment Widget
[**visualize_price_breakdown**](RecipesApi.md#visualize_price_breakdown) | **POST** /recipes/visualizePriceEstimator | Price Breakdown Widget
[**visualize_recipe_equipment_by_id**](RecipesApi.md#visualize_recipe_equipment_by_id) | **GET** /recipes/{id}/equipmentWidget | Equipment by ID Widget
[**visualize_recipe_ingredients_by_id**](RecipesApi.md#visualize_recipe_ingredients_by_id) | **GET** /recipes/{id}/ingredientWidget | Ingredients by ID Widget
[**visualize_recipe_nutrition**](RecipesApi.md#visualize_recipe_nutrition) | **POST** /recipes/visualizeNutrition | Recipe Nutrition Widget
[**visualize_recipe_nutrition_by_id**](RecipesApi.md#visualize_recipe_nutrition_by_id) | **GET** /recipes/{id}/nutritionWidget | Recipe Nutrition by ID Widget
[**visualize_recipe_price_breakdown_by_id**](RecipesApi.md#visualize_recipe_price_breakdown_by_id) | **GET** /recipes/{id}/priceBreakdownWidget | Price Breakdown by ID Widget
[**visualize_recipe_taste**](RecipesApi.md#visualize_recipe_taste) | **POST** /recipes/visualizeTaste | Recipe Taste Widget
[**visualize_recipe_taste_by_id**](RecipesApi.md#visualize_recipe_taste_by_id) | **GET** /recipes/{id}/tasteWidget | Recipe Taste by ID Widget


# **analyze_a_recipe_search_query**
> AnalyzeARecipeSearchQuery200Response analyze_a_recipe_search_query(q)

Analyze a Recipe Search Query

Parse a recipe search query to find out its intention.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.analyze_a_recipe_search_query200_response import AnalyzeARecipeSearchQuery200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    q = "salmon with fusilli and no nuts" # str | The recipe search query.

    # example passing only required values which don't have defaults set
    try:
        # Analyze a Recipe Search Query
        api_response = api_instance.analyze_a_recipe_search_query(q)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->analyze_a_recipe_search_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The recipe search query. |

### Return type

[**AnalyzeARecipeSearchQuery200Response**](AnalyzeARecipeSearchQuery200Response.md)

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

# **analyze_recipe_instructions**
> AnalyzeRecipeInstructions200Response analyze_recipe_instructions()

Analyze Recipe Instructions

This endpoint allows you to break down instructions into atomic steps. Furthermore, each step will contain the ingredients and equipment required. Additionally, all ingredients and equipment from the recipe's instructions will be extracted independently of the step they're used in.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.analyze_recipe_instructions200_response import AnalyzeRecipeInstructions200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Analyze Recipe Instructions
        api_response = api_instance.analyze_recipe_instructions(content_type=content_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->analyze_recipe_instructions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]

### Return type

[**AnalyzeRecipeInstructions200Response**](AnalyzeRecipeInstructions200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_recipe_search**
> [AutocompleteRecipeSearch200ResponseInner] autocomplete_recipe_search()

Autocomplete Recipe Search

Autocomplete a partial input to suggest possible recipe names.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.autocomplete_recipe_search200_response_inner import AutocompleteRecipeSearch200ResponseInner
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
    api_instance = recipes_api.RecipesApi(api_client)
    query = "burger" # str | The (natural language) search query. (optional)
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Autocomplete Recipe Search
        api_response = api_instance.autocomplete_recipe_search(query=query, number=number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->autocomplete_recipe_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The (natural language) search query. | [optional]
 **number** | **int**| The maximum number of items to return (between 1 and 100). Defaults to 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**[AutocompleteRecipeSearch200ResponseInner]**](AutocompleteRecipeSearch200ResponseInner.md)

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

# **classify_cuisine**
> ClassifyCuisine200Response classify_cuisine()

Classify Cuisine

Classify the recipe's cuisine.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.classify_cuisine200_response import ClassifyCuisine200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Classify Cuisine
        api_response = api_instance.classify_cuisine(content_type=content_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->classify_cuisine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]

### Return type

[**ClassifyCuisine200Response**](ClassifyCuisine200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_glycemic_load**
> ComputeGlycemicLoad200Response compute_glycemic_load(compute_glycemic_load_request)

Compute Glycemic Load

Retrieve the glycemic index for a list of ingredients and compute the individual and total glycemic load.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.compute_glycemic_load_request import ComputeGlycemicLoadRequest
from openapi_client.model.compute_glycemic_load200_response import ComputeGlycemicLoad200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    compute_glycemic_load_request = ComputeGlycemicLoadRequest(
        ingredients=[
            "ingredients_example",
        ],
    ) # ComputeGlycemicLoadRequest | 
    language = "en" # str | The language of the input. Either 'en' or 'de'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Compute Glycemic Load
        api_response = api_instance.compute_glycemic_load(compute_glycemic_load_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->compute_glycemic_load: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Compute Glycemic Load
        api_response = api_instance.compute_glycemic_load(compute_glycemic_load_request, language=language)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->compute_glycemic_load: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_glycemic_load_request** | [**ComputeGlycemicLoadRequest**](ComputeGlycemicLoadRequest.md)|  |
 **language** | **str**| The language of the input. Either &#39;en&#39; or &#39;de&#39;. | [optional]

### Return type

[**ComputeGlycemicLoad200Response**](ComputeGlycemicLoad200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_amounts**
> ConvertAmounts200Response convert_amounts(ingredient_name, source_amount, source_unit, target_unit)

Convert Amounts

Convert amounts like \"2 cups of flour to grams\".

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.convert_amounts200_response import ConvertAmounts200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    ingredient_name = "flour" # str | The ingredient which you want to convert.
    source_amount = 2.5 # float | The amount from which you want to convert, e.g. the 2.5 in \"2.5 cups of flour to grams\".
    source_unit = "cups" # str | The unit from which you want to convert, e.g. the grams in \"2.5 cups of flour to grams\". You can also use \"piece\", e.g. \"3.4 oz tomatoes to piece\"
    target_unit = "grams" # str | The unit to which you want to convert, e.g. the grams in \"2.5 cups of flour to grams\". You can also use \"piece\", e.g. \"3.4 oz tomatoes to piece\"

    # example passing only required values which don't have defaults set
    try:
        # Convert Amounts
        api_response = api_instance.convert_amounts(ingredient_name, source_amount, source_unit, target_unit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->convert_amounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingredient_name** | **str**| The ingredient which you want to convert. |
 **source_amount** | **float**| The amount from which you want to convert, e.g. the 2.5 in \&quot;2.5 cups of flour to grams\&quot;. |
 **source_unit** | **str**| The unit from which you want to convert, e.g. the grams in \&quot;2.5 cups of flour to grams\&quot;. You can also use \&quot;piece\&quot;, e.g. \&quot;3.4 oz tomatoes to piece\&quot; |
 **target_unit** | **str**| The unit to which you want to convert, e.g. the grams in \&quot;2.5 cups of flour to grams\&quot;. You can also use \&quot;piece\&quot;, e.g. \&quot;3.4 oz tomatoes to piece\&quot; |

### Return type

[**ConvertAmounts200Response**](ConvertAmounts200Response.md)

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

# **create_recipe_card**
> CreateRecipeCard200Response create_recipe_card()

Create Recipe Card

Generate a recipe card for a recipe.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.create_recipe_card200_response import CreateRecipeCard200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Recipe Card
        api_response = api_instance.create_recipe_card(content_type=content_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->create_recipe_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]

### Return type

[**CreateRecipeCard200Response**](CreateRecipeCard200Response.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **equipment_by_id_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} equipment_by_id_image(id)

Equipment by ID Image

Visualize a recipe's equipment list as an image.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 44860 # float | The recipe id.

    # example passing only required values which don't have defaults set
    try:
        # Equipment by ID Image
        api_response = api_instance.equipment_by_id_image(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->equipment_by_id_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_recipe_from_website**
> GetRecipeInformation200Response extract_recipe_from_website(url)

Extract Recipe from Website

This endpoint lets you extract recipe data such as title, ingredients, and instructions from any properly formatted Website.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_information200_response import GetRecipeInformation200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    url = "https://foodista.com/recipe/ZHK4KPB6/chocolate-crinkle-cookies" # str | The URL of the recipe page.
    force_extraction = True # bool | If true, the extraction will be triggered whether we already know the recipe or not. Use this only if information is missing as this operation is slower. (optional)
    analyze = False # bool | If true, the recipe will be analyzed and classified resolving in more data such as cuisines, dish types, and more. (optional)
    include_nutrition = False # bool | Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings. (optional) if omitted the server will use the default value of False
    include_taste = False # bool | Whether taste data should be added to correctly parsed ingredients. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Extract Recipe from Website
        api_response = api_instance.extract_recipe_from_website(url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->extract_recipe_from_website: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extract Recipe from Website
        api_response = api_instance.extract_recipe_from_website(url, force_extraction=force_extraction, analyze=analyze, include_nutrition=include_nutrition, include_taste=include_taste)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->extract_recipe_from_website: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The URL of the recipe page. |
 **force_extraction** | **bool**| If true, the extraction will be triggered whether we already know the recipe or not. Use this only if information is missing as this operation is slower. | [optional]
 **analyze** | **bool**| If true, the recipe will be analyzed and classified resolving in more data such as cuisines, dish types, and more. | [optional]
 **include_nutrition** | **bool**| Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings. | [optional] if omitted the server will use the default value of False
 **include_taste** | **bool**| Whether taste data should be added to correctly parsed ingredients. | [optional] if omitted the server will use the default value of False

### Return type

[**GetRecipeInformation200Response**](GetRecipeInformation200Response.md)

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

# **get_analyzed_recipe_instructions**
> GetAnalyzedRecipeInstructions200Response get_analyzed_recipe_instructions(id)

Get Analyzed Recipe Instructions

Get an analyzed breakdown of a recipe's instructions. Each step is enriched with the ingredients and equipment required.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_analyzed_recipe_instructions200_response import GetAnalyzedRecipeInstructions200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    step_breakdown = True # bool | Whether to break down the recipe steps even more. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Analyzed Recipe Instructions
        api_response = api_instance.get_analyzed_recipe_instructions(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_analyzed_recipe_instructions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Analyzed Recipe Instructions
        api_response = api_instance.get_analyzed_recipe_instructions(id, step_breakdown=step_breakdown)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_analyzed_recipe_instructions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **step_breakdown** | **bool**| Whether to break down the recipe steps even more. | [optional]

### Return type

[**GetAnalyzedRecipeInstructions200Response**](GetAnalyzedRecipeInstructions200Response.md)

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

# **get_random_recipes**
> GetRandomRecipes200Response get_random_recipes()

Get Random Recipes

Find random (popular) recipes. If you need to filter recipes by diet, nutrition etc. you might want to consider using the complex recipe search endpoint and set the sort request parameter to random.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_random_recipes200_response import GetRandomRecipes200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    limit_license = True # bool | Whether the recipes should have an open license that allows display with proper attribution. (optional) if omitted the server will use the default value of True
    tags = "tags_example" # str | The tags (can be diets, meal types, cuisines, or intolerances) that the recipe must have. (optional)
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Random Recipes
        api_response = api_instance.get_random_recipes(limit_license=limit_license, tags=tags, number=number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_random_recipes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_license** | **bool**| Whether the recipes should have an open license that allows display with proper attribution. | [optional] if omitted the server will use the default value of True
 **tags** | **str**| The tags (can be diets, meal types, cuisines, or intolerances) that the recipe must have. | [optional]
 **number** | **int**| The maximum number of items to return (between 1 and 100). Defaults to 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**GetRandomRecipes200Response**](GetRandomRecipes200Response.md)

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

# **get_recipe_equipment_by_id**
> GetRecipeEquipmentByID200Response get_recipe_equipment_by_id(id)

Equipment by ID

Get a recipe's equipment list.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_equipment_by_id200_response import GetRecipeEquipmentByID200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.

    # example passing only required values which don't have defaults set
    try:
        # Equipment by ID
        api_response = api_instance.get_recipe_equipment_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_equipment_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |

### Return type

[**GetRecipeEquipmentByID200Response**](GetRecipeEquipmentByID200Response.md)

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

# **get_recipe_information**
> GetRecipeInformation200Response get_recipe_information(id)

Get Recipe Information

Use a recipe id to get full information about a recipe, such as ingredients, nutrition, diet and allergen information, etc.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_information200_response import GetRecipeInformation200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    include_nutrition = False # bool | Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Recipe Information
        api_response = api_instance.get_recipe_information(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_information: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Recipe Information
        api_response = api_instance.get_recipe_information(id, include_nutrition=include_nutrition)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **include_nutrition** | **bool**| Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings. | [optional] if omitted the server will use the default value of False

### Return type

[**GetRecipeInformation200Response**](GetRecipeInformation200Response.md)

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

# **get_recipe_information_bulk**
> [GetRecipeInformationBulk200ResponseInner] get_recipe_information_bulk(ids)

Get Recipe Information Bulk

Get information about multiple recipes at once. This is equivalent to calling the Get Recipe Information endpoint multiple times, but faster.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_information_bulk200_response_inner import GetRecipeInformationBulk200ResponseInner
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
    api_instance = recipes_api.RecipesApi(api_client)
    ids = "715538,716429" # str | A comma-separated list of recipe ids.
    include_nutrition = False # bool | Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Recipe Information Bulk
        api_response = api_instance.get_recipe_information_bulk(ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_information_bulk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Recipe Information Bulk
        api_response = api_instance.get_recipe_information_bulk(ids, include_nutrition=include_nutrition)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_information_bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| A comma-separated list of recipe ids. |
 **include_nutrition** | **bool**| Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings. | [optional] if omitted the server will use the default value of False

### Return type

[**[GetRecipeInformationBulk200ResponseInner]**](GetRecipeInformationBulk200ResponseInner.md)

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

# **get_recipe_ingredients_by_id**
> GetRecipeIngredientsByID200Response get_recipe_ingredients_by_id(id)

Ingredients by ID

Get a recipe's ingredient list.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_ingredients_by_id200_response import GetRecipeIngredientsByID200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.

    # example passing only required values which don't have defaults set
    try:
        # Ingredients by ID
        api_response = api_instance.get_recipe_ingredients_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_ingredients_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |

### Return type

[**GetRecipeIngredientsByID200Response**](GetRecipeIngredientsByID200Response.md)

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

# **get_recipe_nutrition_widget_by_id**
> GetRecipeNutritionWidgetByID200Response get_recipe_nutrition_widget_by_id(id)

Nutrition by ID

Get a recipe's nutrition data.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_nutrition_widget_by_id200_response import GetRecipeNutritionWidgetByID200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.

    # example passing only required values which don't have defaults set
    try:
        # Nutrition by ID
        api_response = api_instance.get_recipe_nutrition_widget_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_nutrition_widget_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |

### Return type

[**GetRecipeNutritionWidgetByID200Response**](GetRecipeNutritionWidgetByID200Response.md)

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

# **get_recipe_price_breakdown_by_id**
> GetRecipePriceBreakdownByID200Response get_recipe_price_breakdown_by_id(id)

Price Breakdown by ID

Get a recipe's price breakdown data.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_price_breakdown_by_id200_response import GetRecipePriceBreakdownByID200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.

    # example passing only required values which don't have defaults set
    try:
        # Price Breakdown by ID
        api_response = api_instance.get_recipe_price_breakdown_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_price_breakdown_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |

### Return type

[**GetRecipePriceBreakdownByID200Response**](GetRecipePriceBreakdownByID200Response.md)

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

# **get_recipe_taste_by_id**
> GetRecipeTasteByID200Response get_recipe_taste_by_id(id)

Taste by ID

Get a recipe's taste. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_recipe_taste_by_id200_response import GetRecipeTasteByID200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    normalize = True # bool | Normalize to the strongest taste. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Taste by ID
        api_response = api_instance.get_recipe_taste_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_taste_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Taste by ID
        api_response = api_instance.get_recipe_taste_by_id(id, normalize=normalize)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_taste_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **normalize** | **bool**| Normalize to the strongest taste. | [optional] if omitted the server will use the default value of True

### Return type

[**GetRecipeTasteByID200Response**](GetRecipeTasteByID200Response.md)

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

# **get_similar_recipes**
> [GetSimilarRecipes200ResponseInner] get_similar_recipes(id)

Get Similar Recipes

Find recipes which are similar to the given one.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.get_similar_recipes200_response_inner import GetSimilarRecipes200ResponseInner
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) if omitted the server will use the default value of 10
    limit_license = True # bool | Whether the recipes should have an open license that allows display with proper attribution. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get Similar Recipes
        api_response = api_instance.get_similar_recipes(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_similar_recipes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Similar Recipes
        api_response = api_instance.get_similar_recipes(id, number=number, limit_license=limit_license)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->get_similar_recipes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **number** | **int**| The maximum number of items to return (between 1 and 100). Defaults to 10. | [optional] if omitted the server will use the default value of 10
 **limit_license** | **bool**| Whether the recipes should have an open license that allows display with proper attribution. | [optional] if omitted the server will use the default value of True

### Return type

[**[GetSimilarRecipes200ResponseInner]**](GetSimilarRecipes200ResponseInner.md)

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

# **guess_nutrition_by_dish_name**
> GuessNutritionByDishName200Response guess_nutrition_by_dish_name(title)

Guess Nutrition by Dish Name

Estimate the macronutrients of a dish based on its title.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.guess_nutrition_by_dish_name200_response import GuessNutritionByDishName200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    title = "Spaghetti Aglio et Olio" # str | The title of the dish.

    # example passing only required values which don't have defaults set
    try:
        # Guess Nutrition by Dish Name
        api_response = api_instance.guess_nutrition_by_dish_name(title)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->guess_nutrition_by_dish_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title of the dish. |

### Return type

[**GuessNutritionByDishName200Response**](GuessNutritionByDishName200Response.md)

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

# **ingredients_by_id_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} ingredients_by_id_image(id)

Ingredients by ID Image

Visualize a recipe's ingredient list.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1082038 # float | The recipe id.
    measure = "metric" # str | Whether the the measures should be 'us' or 'metric'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ingredients by ID Image
        api_response = api_instance.ingredients_by_id_image(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->ingredients_by_id_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ingredients by ID Image
        api_response = api_instance.ingredients_by_id_image(id, measure=measure)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->ingredients_by_id_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |
 **measure** | **str**| Whether the the measures should be &#39;us&#39; or &#39;metric&#39;. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_ingredients**
> [ParseIngredients200ResponseInner] parse_ingredients()

Parse Ingredients

Extract an ingredient from plain text.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.parse_ingredients200_response_inner import ParseIngredients200ResponseInner
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)
    language = "en" # str | The language of the input. Either 'en' or 'de'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Parse Ingredients
        api_response = api_instance.parse_ingredients(content_type=content_type, language=language)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->parse_ingredients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]
 **language** | **str**| The language of the input. Either &#39;en&#39; or &#39;de&#39;. | [optional]

### Return type

[**[ParseIngredients200ResponseInner]**](ParseIngredients200ResponseInner.md)

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_breakdown_by_id_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} price_breakdown_by_id_image(id)

Price Breakdown by ID Image

Visualize a recipe's price breakdown.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1082038 # float | The recipe id.

    # example passing only required values which don't have defaults set
    try:
        # Price Breakdown by ID Image
        api_response = api_instance.price_breakdown_by_id_image(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->price_breakdown_by_id_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quick_answer**
> QuickAnswer200Response quick_answer(q)

Quick Answer

Answer a nutrition related natural language question.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.quick_answer200_response import QuickAnswer200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    q = "How much vitamin c is in 2 apples?" # str | The nutrition related question.

    # example passing only required values which don't have defaults set
    try:
        # Quick Answer
        api_response = api_instance.quick_answer(q)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->quick_answer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The nutrition related question. |

### Return type

[**QuickAnswer200Response**](QuickAnswer200Response.md)

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

# **recipe_nutrition_by_id_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} recipe_nutrition_by_id_image(id)

Recipe Nutrition by ID Image

Visualize a recipe's nutritional information as an image.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1082038 # float | The recipe id.

    # example passing only required values which don't have defaults set
    try:
        # Recipe Nutrition by ID Image
        api_response = api_instance.recipe_nutrition_by_id_image(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_nutrition_by_id_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_nutrition_label_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} recipe_nutrition_label_image(id)

Recipe Nutrition Label Image

Get a recipe's nutrition label as an image.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 641166 # float | The recipe id.
    show_optional_nutrients = False # bool | Whether to show optional nutrients. (optional)
    show_zero_values = False # bool | Whether to show zero values. (optional)
    show_ingredients = False # bool | Whether to show a list of ingredients. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recipe Nutrition Label Image
        api_response = api_instance.recipe_nutrition_label_image(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_nutrition_label_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Nutrition Label Image
        api_response = api_instance.recipe_nutrition_label_image(id, show_optional_nutrients=show_optional_nutrients, show_zero_values=show_zero_values, show_ingredients=show_ingredients)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_nutrition_label_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |
 **show_optional_nutrients** | **bool**| Whether to show optional nutrients. | [optional]
 **show_zero_values** | **bool**| Whether to show zero values. | [optional]
 **show_ingredients** | **bool**| Whether to show a list of ingredients. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_nutrition_label_widget**
> str recipe_nutrition_label_widget(id)

Recipe Nutrition Label Widget

Get a recipe's nutrition label as an HTML widget.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 641166 # float | The recipe id.
    default_css = False # bool | Whether the default CSS should be added to the response. (optional) if omitted the server will use the default value of True
    show_optional_nutrients = False # bool | Whether to show optional nutrients. (optional)
    show_zero_values = False # bool | Whether to show zero values. (optional)
    show_ingredients = False # bool | Whether to show a list of ingredients. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recipe Nutrition Label Widget
        api_response = api_instance.recipe_nutrition_label_widget(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_nutrition_label_widget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Nutrition Label Widget
        api_response = api_instance.recipe_nutrition_label_widget(id, default_css=default_css, show_optional_nutrients=show_optional_nutrients, show_zero_values=show_zero_values, show_ingredients=show_ingredients)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_nutrition_label_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |
 **default_css** | **bool**| Whether the default CSS should be added to the response. | [optional] if omitted the server will use the default value of True
 **show_optional_nutrients** | **bool**| Whether to show optional nutrients. | [optional]
 **show_zero_values** | **bool**| Whether to show zero values. | [optional]
 **show_ingredients** | **bool**| Whether to show a list of ingredients. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_taste_by_id_image**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} recipe_taste_by_id_image(id)

Recipe Taste by ID Image

Get a recipe's taste as an image. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 69095 # float | The recipe id.
    normalize = False # bool | Normalize to the strongest taste. (optional)
    rgb = "75,192,192" # str | Red, green, blue values for the chart color. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recipe Taste by ID Image
        api_response = api_instance.recipe_taste_by_id_image(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_taste_by_id_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Taste by ID Image
        api_response = api_instance.recipe_taste_by_id_image(id, normalize=normalize, rgb=rgb)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipe_taste_by_id_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The recipe id. |
 **normalize** | **bool**| Normalize to the strongest taste. | [optional]
 **rgb** | **str**| Red, green, blue values for the chart color. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_recipes**
> SearchRecipes200Response search_recipes()

Search Recipes

Search through hundreds of thousands of recipes using advanced filtering and ranking. NOTE: This method combines searching by query, by ingredients, and by nutrients into one endpoint.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.search_recipes200_response import SearchRecipes200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    query = "burger" # str | The (natural language) search query. (optional)
    cuisine = "italian" # str | The cuisine(s) of the recipes. One or more, comma separated (will be interpreted as 'OR'). See a full list of supported cuisines. (optional)
    exclude_cuisine = "greek" # str | The cuisine(s) the recipes must not match. One or more, comma separated (will be interpreted as 'AND'). See a full list of supported cuisines. (optional)
    diet = "vegetarian" # str | The diet for which the recipes must be suitable. See a full list of supported diets. (optional)
    intolerances = "gluten" # str | A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances. (optional)
    equipment = "pan" # str | The equipment required. Multiple values will be interpreted as 'or'. For example, value could be \"blender, frying pan, bowl\". (optional)
    include_ingredients = "tomato,cheese" # str | A comma-separated list of ingredients that should/must be used in the recipes. (optional)
    exclude_ingredients = "eggs" # str | A comma-separated list of ingredients or ingredient types that the recipes must not contain. (optional)
    type = "main course" # str | The type of recipe. See a full list of supported meal types. (optional)
    instructions_required = True # bool | Whether the recipes must have instructions. (optional)
    fill_ingredients = False # bool | Add information about the ingredients and whether they are used or missing in relation to the query. (optional)
    add_recipe_information = False # bool | If set to true, you get more information about the recipes returned. (optional)
    add_recipe_nutrition = False # bool | If set to true, you get nutritional information about each recipes returned. (optional)
    author = "coffeebean" # str | The username of the recipe author. (optional)
    tags = "tags_example" # str | The tags (can be diets, meal types, cuisines, or intolerances) that the recipe must have. (optional)
    recipe_box_id = 2468 # float | The id of the recipe box to which the search should be limited to. (optional)
    title_match = "Crock Pot" # str | Enter text that must be found in the title of the recipes. (optional)
    max_ready_time = 20 # float | The maximum time in minutes it should take to prepare and cook the recipe. (optional)
    ignore_pantry = False # bool | Whether to ignore typical pantry items, such as water, salt, flour, etc. (optional) if omitted the server will use the default value of False
    sort = "calories" # str | The strategy to sort recipes by. See a full list of supported sorting options. (optional)
    sort_direction = "asc" # str | The direction in which to sort. Must be either 'asc' (ascending) or 'desc' (descending). (optional)
    min_carbs = 10 # float | The minimum amount of carbohydrates in grams the recipe must have. (optional)
    max_carbs = 100 # float | The maximum amount of carbohydrates in grams the recipe can have. (optional)
    min_protein = 10 # float | The minimum amount of protein in grams the recipe must have. (optional)
    max_protein = 100 # float | The maximum amount of protein in grams the recipe can have. (optional)
    min_calories = 50 # float | The minimum amount of calories the recipe must have. (optional)
    max_calories = 800 # float | The maximum amount of calories the recipe can have. (optional)
    min_fat = 1 # float | The minimum amount of fat in grams the recipe must have. (optional)
    max_fat = 100 # float | The maximum amount of fat in grams the recipe can have. (optional)
    min_alcohol = 0 # float | The minimum amount of alcohol in grams the recipe must have. (optional)
    max_alcohol = 100 # float | The maximum amount of alcohol in grams the recipe can have. (optional)
    min_caffeine = 0 # float | The minimum amount of caffeine in milligrams the recipe must have. (optional)
    max_caffeine = 100 # float | The maximum amount of caffeine in milligrams the recipe can have. (optional)
    min_copper = 0 # float | The minimum amount of copper in milligrams the recipe must have. (optional)
    max_copper = 100 # float | The maximum amount of copper in milligrams the recipe can have. (optional)
    min_calcium = 0 # float | The minimum amount of calcium in milligrams the recipe must have. (optional)
    max_calcium = 100 # float | The maximum amount of calcium in milligrams the recipe can have. (optional)
    min_choline = 0 # float | The minimum amount of choline in milligrams the recipe must have. (optional)
    max_choline = 100 # float | The maximum amount of choline in milligrams the recipe can have. (optional)
    min_cholesterol = 0 # float | The minimum amount of cholesterol in milligrams the recipe must have. (optional)
    max_cholesterol = 100 # float | The maximum amount of cholesterol in milligrams the recipe can have. (optional)
    min_fluoride = 0 # float | The minimum amount of fluoride in milligrams the recipe must have. (optional)
    max_fluoride = 100 # float | The maximum amount of fluoride in milligrams the recipe can have. (optional)
    min_saturated_fat = 0 # float | The minimum amount of saturated fat in grams the recipe must have. (optional)
    max_saturated_fat = 100 # float | The maximum amount of saturated fat in grams the recipe can have. (optional)
    min_vitamin_a = 0 # float | The minimum amount of Vitamin A in IU the recipe must have. (optional)
    max_vitamin_a = 100 # float | The maximum amount of Vitamin A in IU the recipe can have. (optional)
    min_vitamin_c = 0 # float | The minimum amount of Vitamin C milligrams the recipe must have. (optional)
    max_vitamin_c = 100 # float | The maximum amount of Vitamin C in milligrams the recipe can have. (optional)
    min_vitamin_d = 0 # float | The minimum amount of Vitamin D in micrograms the recipe must have. (optional)
    max_vitamin_d = 100 # float | The maximum amount of Vitamin D in micrograms the recipe can have. (optional)
    min_vitamin_e = 0 # float | The minimum amount of Vitamin E in milligrams the recipe must have. (optional)
    max_vitamin_e = 100 # float | The maximum amount of Vitamin E in milligrams the recipe can have. (optional)
    min_vitamin_k = 0 # float | The minimum amount of Vitamin K in micrograms the recipe must have. (optional)
    max_vitamin_k = 100 # float | The maximum amount of Vitamin K in micrograms the recipe can have. (optional)
    min_vitamin_b1 = 0 # float | The minimum amount of Vitamin B1 in milligrams the recipe must have. (optional)
    max_vitamin_b1 = 100 # float | The maximum amount of Vitamin B1 in milligrams the recipe can have. (optional)
    min_vitamin_b2 = 0 # float | The minimum amount of Vitamin B2 in milligrams the recipe must have. (optional)
    max_vitamin_b2 = 100 # float | The maximum amount of Vitamin B2 in milligrams the recipe can have. (optional)
    min_vitamin_b5 = 0 # float | The minimum amount of Vitamin B5 in milligrams the recipe must have. (optional)
    max_vitamin_b5 = 100 # float | The maximum amount of Vitamin B5 in milligrams the recipe can have. (optional)
    min_vitamin_b3 = 0 # float | The minimum amount of Vitamin B3 in milligrams the recipe must have. (optional)
    max_vitamin_b3 = 100 # float | The maximum amount of Vitamin B3 in milligrams the recipe can have. (optional)
    min_vitamin_b6 = 0 # float | The minimum amount of Vitamin B6 in milligrams the recipe must have. (optional)
    max_vitamin_b6 = 100 # float | The maximum amount of Vitamin B6 in milligrams the recipe can have. (optional)
    min_vitamin_b12 = 0 # float | The minimum amount of Vitamin B12 in micrograms the recipe must have. (optional)
    max_vitamin_b12 = 100 # float | The maximum amount of Vitamin B12 in micrograms the recipe can have. (optional)
    min_fiber = 0 # float | The minimum amount of fiber in grams the recipe must have. (optional)
    max_fiber = 100 # float | The maximum amount of fiber in grams the recipe can have. (optional)
    min_folate = 0 # float | The minimum amount of folate in micrograms the recipe must have. (optional)
    max_folate = 100 # float | The maximum amount of folate in micrograms the recipe can have. (optional)
    min_folic_acid = 0 # float | The minimum amount of folic acid in micrograms the recipe must have. (optional)
    max_folic_acid = 100 # float | The maximum amount of folic acid in micrograms the recipe can have. (optional)
    min_iodine = 0 # float | The minimum amount of iodine in micrograms the recipe must have. (optional)
    max_iodine = 100 # float | The maximum amount of iodine in micrograms the recipe can have. (optional)
    min_iron = 0 # float | The minimum amount of iron in milligrams the recipe must have. (optional)
    max_iron = 100 # float | The maximum amount of iron in milligrams the recipe can have. (optional)
    min_magnesium = 0 # float | The minimum amount of magnesium in milligrams the recipe must have. (optional)
    max_magnesium = 100 # float | The maximum amount of magnesium in milligrams the recipe can have. (optional)
    min_manganese = 0 # float | The minimum amount of manganese in milligrams the recipe must have. (optional)
    max_manganese = 100 # float | The maximum amount of manganese in milligrams the recipe can have. (optional)
    min_phosphorus = 0 # float | The minimum amount of phosphorus in milligrams the recipe must have. (optional)
    max_phosphorus = 100 # float | The maximum amount of phosphorus in milligrams the recipe can have. (optional)
    min_potassium = 0 # float | The minimum amount of potassium in milligrams the recipe must have. (optional)
    max_potassium = 100 # float | The maximum amount of potassium in milligrams the recipe can have. (optional)
    min_selenium = 0 # float | The minimum amount of selenium in micrograms the recipe must have. (optional)
    max_selenium = 100 # float | The maximum amount of selenium in micrograms the recipe can have. (optional)
    min_sodium = 0 # float | The minimum amount of sodium in milligrams the recipe must have. (optional)
    max_sodium = 100 # float | The maximum amount of sodium in milligrams the recipe can have. (optional)
    min_sugar = 0 # float | The minimum amount of sugar in grams the recipe must have. (optional)
    max_sugar = 100 # float | The maximum amount of sugar in grams the recipe can have. (optional)
    min_zinc = 0 # float | The minimum amount of zinc in milligrams the recipe must have. (optional)
    max_zinc = 100 # float | The maximum amount of zinc in milligrams the recipe can have. (optional)
    offset = 0 # int | The number of results to skip (between 0 and 900). (optional)
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) if omitted the server will use the default value of 10
    limit_license = True # bool | Whether the recipes should have an open license that allows display with proper attribution. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Recipes
        api_response = api_instance.search_recipes(query=query, cuisine=cuisine, exclude_cuisine=exclude_cuisine, diet=diet, intolerances=intolerances, equipment=equipment, include_ingredients=include_ingredients, exclude_ingredients=exclude_ingredients, type=type, instructions_required=instructions_required, fill_ingredients=fill_ingredients, add_recipe_information=add_recipe_information, add_recipe_nutrition=add_recipe_nutrition, author=author, tags=tags, recipe_box_id=recipe_box_id, title_match=title_match, max_ready_time=max_ready_time, ignore_pantry=ignore_pantry, sort=sort, sort_direction=sort_direction, min_carbs=min_carbs, max_carbs=max_carbs, min_protein=min_protein, max_protein=max_protein, min_calories=min_calories, max_calories=max_calories, min_fat=min_fat, max_fat=max_fat, min_alcohol=min_alcohol, max_alcohol=max_alcohol, min_caffeine=min_caffeine, max_caffeine=max_caffeine, min_copper=min_copper, max_copper=max_copper, min_calcium=min_calcium, max_calcium=max_calcium, min_choline=min_choline, max_choline=max_choline, min_cholesterol=min_cholesterol, max_cholesterol=max_cholesterol, min_fluoride=min_fluoride, max_fluoride=max_fluoride, min_saturated_fat=min_saturated_fat, max_saturated_fat=max_saturated_fat, min_vitamin_a=min_vitamin_a, max_vitamin_a=max_vitamin_a, min_vitamin_c=min_vitamin_c, max_vitamin_c=max_vitamin_c, min_vitamin_d=min_vitamin_d, max_vitamin_d=max_vitamin_d, min_vitamin_e=min_vitamin_e, max_vitamin_e=max_vitamin_e, min_vitamin_k=min_vitamin_k, max_vitamin_k=max_vitamin_k, min_vitamin_b1=min_vitamin_b1, max_vitamin_b1=max_vitamin_b1, min_vitamin_b2=min_vitamin_b2, max_vitamin_b2=max_vitamin_b2, min_vitamin_b5=min_vitamin_b5, max_vitamin_b5=max_vitamin_b5, min_vitamin_b3=min_vitamin_b3, max_vitamin_b3=max_vitamin_b3, min_vitamin_b6=min_vitamin_b6, max_vitamin_b6=max_vitamin_b6, min_vitamin_b12=min_vitamin_b12, max_vitamin_b12=max_vitamin_b12, min_fiber=min_fiber, max_fiber=max_fiber, min_folate=min_folate, max_folate=max_folate, min_folic_acid=min_folic_acid, max_folic_acid=max_folic_acid, min_iodine=min_iodine, max_iodine=max_iodine, min_iron=min_iron, max_iron=max_iron, min_magnesium=min_magnesium, max_magnesium=max_magnesium, min_manganese=min_manganese, max_manganese=max_manganese, min_phosphorus=min_phosphorus, max_phosphorus=max_phosphorus, min_potassium=min_potassium, max_potassium=max_potassium, min_selenium=min_selenium, max_selenium=max_selenium, min_sodium=min_sodium, max_sodium=max_sodium, min_sugar=min_sugar, max_sugar=max_sugar, min_zinc=min_zinc, max_zinc=max_zinc, offset=offset, number=number, limit_license=limit_license)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->search_recipes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The (natural language) search query. | [optional]
 **cuisine** | **str**| The cuisine(s) of the recipes. One or more, comma separated (will be interpreted as &#39;OR&#39;). See a full list of supported cuisines. | [optional]
 **exclude_cuisine** | **str**| The cuisine(s) the recipes must not match. One or more, comma separated (will be interpreted as &#39;AND&#39;). See a full list of supported cuisines. | [optional]
 **diet** | **str**| The diet for which the recipes must be suitable. See a full list of supported diets. | [optional]
 **intolerances** | **str**| A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances. | [optional]
 **equipment** | **str**| The equipment required. Multiple values will be interpreted as &#39;or&#39;. For example, value could be \&quot;blender, frying pan, bowl\&quot;. | [optional]
 **include_ingredients** | **str**| A comma-separated list of ingredients that should/must be used in the recipes. | [optional]
 **exclude_ingredients** | **str**| A comma-separated list of ingredients or ingredient types that the recipes must not contain. | [optional]
 **type** | **str**| The type of recipe. See a full list of supported meal types. | [optional]
 **instructions_required** | **bool**| Whether the recipes must have instructions. | [optional]
 **fill_ingredients** | **bool**| Add information about the ingredients and whether they are used or missing in relation to the query. | [optional]
 **add_recipe_information** | **bool**| If set to true, you get more information about the recipes returned. | [optional]
 **add_recipe_nutrition** | **bool**| If set to true, you get nutritional information about each recipes returned. | [optional]
 **author** | **str**| The username of the recipe author. | [optional]
 **tags** | **str**| The tags (can be diets, meal types, cuisines, or intolerances) that the recipe must have. | [optional]
 **recipe_box_id** | **float**| The id of the recipe box to which the search should be limited to. | [optional]
 **title_match** | **str**| Enter text that must be found in the title of the recipes. | [optional]
 **max_ready_time** | **float**| The maximum time in minutes it should take to prepare and cook the recipe. | [optional]
 **ignore_pantry** | **bool**| Whether to ignore typical pantry items, such as water, salt, flour, etc. | [optional] if omitted the server will use the default value of False
 **sort** | **str**| The strategy to sort recipes by. See a full list of supported sorting options. | [optional]
 **sort_direction** | **str**| The direction in which to sort. Must be either &#39;asc&#39; (ascending) or &#39;desc&#39; (descending). | [optional]
 **min_carbs** | **float**| The minimum amount of carbohydrates in grams the recipe must have. | [optional]
 **max_carbs** | **float**| The maximum amount of carbohydrates in grams the recipe can have. | [optional]
 **min_protein** | **float**| The minimum amount of protein in grams the recipe must have. | [optional]
 **max_protein** | **float**| The maximum amount of protein in grams the recipe can have. | [optional]
 **min_calories** | **float**| The minimum amount of calories the recipe must have. | [optional]
 **max_calories** | **float**| The maximum amount of calories the recipe can have. | [optional]
 **min_fat** | **float**| The minimum amount of fat in grams the recipe must have. | [optional]
 **max_fat** | **float**| The maximum amount of fat in grams the recipe can have. | [optional]
 **min_alcohol** | **float**| The minimum amount of alcohol in grams the recipe must have. | [optional]
 **max_alcohol** | **float**| The maximum amount of alcohol in grams the recipe can have. | [optional]
 **min_caffeine** | **float**| The minimum amount of caffeine in milligrams the recipe must have. | [optional]
 **max_caffeine** | **float**| The maximum amount of caffeine in milligrams the recipe can have. | [optional]
 **min_copper** | **float**| The minimum amount of copper in milligrams the recipe must have. | [optional]
 **max_copper** | **float**| The maximum amount of copper in milligrams the recipe can have. | [optional]
 **min_calcium** | **float**| The minimum amount of calcium in milligrams the recipe must have. | [optional]
 **max_calcium** | **float**| The maximum amount of calcium in milligrams the recipe can have. | [optional]
 **min_choline** | **float**| The minimum amount of choline in milligrams the recipe must have. | [optional]
 **max_choline** | **float**| The maximum amount of choline in milligrams the recipe can have. | [optional]
 **min_cholesterol** | **float**| The minimum amount of cholesterol in milligrams the recipe must have. | [optional]
 **max_cholesterol** | **float**| The maximum amount of cholesterol in milligrams the recipe can have. | [optional]
 **min_fluoride** | **float**| The minimum amount of fluoride in milligrams the recipe must have. | [optional]
 **max_fluoride** | **float**| The maximum amount of fluoride in milligrams the recipe can have. | [optional]
 **min_saturated_fat** | **float**| The minimum amount of saturated fat in grams the recipe must have. | [optional]
 **max_saturated_fat** | **float**| The maximum amount of saturated fat in grams the recipe can have. | [optional]
 **min_vitamin_a** | **float**| The minimum amount of Vitamin A in IU the recipe must have. | [optional]
 **max_vitamin_a** | **float**| The maximum amount of Vitamin A in IU the recipe can have. | [optional]
 **min_vitamin_c** | **float**| The minimum amount of Vitamin C milligrams the recipe must have. | [optional]
 **max_vitamin_c** | **float**| The maximum amount of Vitamin C in milligrams the recipe can have. | [optional]
 **min_vitamin_d** | **float**| The minimum amount of Vitamin D in micrograms the recipe must have. | [optional]
 **max_vitamin_d** | **float**| The maximum amount of Vitamin D in micrograms the recipe can have. | [optional]
 **min_vitamin_e** | **float**| The minimum amount of Vitamin E in milligrams the recipe must have. | [optional]
 **max_vitamin_e** | **float**| The maximum amount of Vitamin E in milligrams the recipe can have. | [optional]
 **min_vitamin_k** | **float**| The minimum amount of Vitamin K in micrograms the recipe must have. | [optional]
 **max_vitamin_k** | **float**| The maximum amount of Vitamin K in micrograms the recipe can have. | [optional]
 **min_vitamin_b1** | **float**| The minimum amount of Vitamin B1 in milligrams the recipe must have. | [optional]
 **max_vitamin_b1** | **float**| The maximum amount of Vitamin B1 in milligrams the recipe can have. | [optional]
 **min_vitamin_b2** | **float**| The minimum amount of Vitamin B2 in milligrams the recipe must have. | [optional]
 **max_vitamin_b2** | **float**| The maximum amount of Vitamin B2 in milligrams the recipe can have. | [optional]
 **min_vitamin_b5** | **float**| The minimum amount of Vitamin B5 in milligrams the recipe must have. | [optional]
 **max_vitamin_b5** | **float**| The maximum amount of Vitamin B5 in milligrams the recipe can have. | [optional]
 **min_vitamin_b3** | **float**| The minimum amount of Vitamin B3 in milligrams the recipe must have. | [optional]
 **max_vitamin_b3** | **float**| The maximum amount of Vitamin B3 in milligrams the recipe can have. | [optional]
 **min_vitamin_b6** | **float**| The minimum amount of Vitamin B6 in milligrams the recipe must have. | [optional]
 **max_vitamin_b6** | **float**| The maximum amount of Vitamin B6 in milligrams the recipe can have. | [optional]
 **min_vitamin_b12** | **float**| The minimum amount of Vitamin B12 in micrograms the recipe must have. | [optional]
 **max_vitamin_b12** | **float**| The maximum amount of Vitamin B12 in micrograms the recipe can have. | [optional]
 **min_fiber** | **float**| The minimum amount of fiber in grams the recipe must have. | [optional]
 **max_fiber** | **float**| The maximum amount of fiber in grams the recipe can have. | [optional]
 **min_folate** | **float**| The minimum amount of folate in micrograms the recipe must have. | [optional]
 **max_folate** | **float**| The maximum amount of folate in micrograms the recipe can have. | [optional]
 **min_folic_acid** | **float**| The minimum amount of folic acid in micrograms the recipe must have. | [optional]
 **max_folic_acid** | **float**| The maximum amount of folic acid in micrograms the recipe can have. | [optional]
 **min_iodine** | **float**| The minimum amount of iodine in micrograms the recipe must have. | [optional]
 **max_iodine** | **float**| The maximum amount of iodine in micrograms the recipe can have. | [optional]
 **min_iron** | **float**| The minimum amount of iron in milligrams the recipe must have. | [optional]
 **max_iron** | **float**| The maximum amount of iron in milligrams the recipe can have. | [optional]
 **min_magnesium** | **float**| The minimum amount of magnesium in milligrams the recipe must have. | [optional]
 **max_magnesium** | **float**| The maximum amount of magnesium in milligrams the recipe can have. | [optional]
 **min_manganese** | **float**| The minimum amount of manganese in milligrams the recipe must have. | [optional]
 **max_manganese** | **float**| The maximum amount of manganese in milligrams the recipe can have. | [optional]
 **min_phosphorus** | **float**| The minimum amount of phosphorus in milligrams the recipe must have. | [optional]
 **max_phosphorus** | **float**| The maximum amount of phosphorus in milligrams the recipe can have. | [optional]
 **min_potassium** | **float**| The minimum amount of potassium in milligrams the recipe must have. | [optional]
 **max_potassium** | **float**| The maximum amount of potassium in milligrams the recipe can have. | [optional]
 **min_selenium** | **float**| The minimum amount of selenium in micrograms the recipe must have. | [optional]
 **max_selenium** | **float**| The maximum amount of selenium in micrograms the recipe can have. | [optional]
 **min_sodium** | **float**| The minimum amount of sodium in milligrams the recipe must have. | [optional]
 **max_sodium** | **float**| The maximum amount of sodium in milligrams the recipe can have. | [optional]
 **min_sugar** | **float**| The minimum amount of sugar in grams the recipe must have. | [optional]
 **max_sugar** | **float**| The maximum amount of sugar in grams the recipe can have. | [optional]
 **min_zinc** | **float**| The minimum amount of zinc in milligrams the recipe must have. | [optional]
 **max_zinc** | **float**| The maximum amount of zinc in milligrams the recipe can have. | [optional]
 **offset** | **int**| The number of results to skip (between 0 and 900). | [optional]
 **number** | **int**| The maximum number of items to return (between 1 and 100). Defaults to 10. | [optional] if omitted the server will use the default value of 10
 **limit_license** | **bool**| Whether the recipes should have an open license that allows display with proper attribution. | [optional] if omitted the server will use the default value of True

### Return type

[**SearchRecipes200Response**](SearchRecipes200Response.md)

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

# **search_recipes_by_ingredients**
> [SearchRecipesByIngredients200ResponseInner] search_recipes_by_ingredients()

Search Recipes by Ingredients

 Ever wondered what recipes you can cook with the ingredients you have in your fridge or pantry? This endpoint lets you find recipes that either maximize the usage of ingredients you have at hand (pre shopping) or minimize the ingredients that you don't currently have (post shopping).         

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.search_recipes_by_ingredients200_response_inner import SearchRecipesByIngredients200ResponseInner
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
    api_instance = recipes_api.RecipesApi(api_client)
    ingredients = "carrots,tomatoes" # str | A comma-separated list of ingredients that the recipes should contain. (optional)
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) if omitted the server will use the default value of 10
    limit_license = True # bool | Whether the recipes should have an open license that allows display with proper attribution. (optional) if omitted the server will use the default value of True
    ranking = 1 # float | Whether to maximize used ingredients (1) or minimize missing ingredients (2) first. (optional)
    ignore_pantry = False # bool | Whether to ignore typical pantry items, such as water, salt, flour, etc. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Recipes by Ingredients
        api_response = api_instance.search_recipes_by_ingredients(ingredients=ingredients, number=number, limit_license=limit_license, ranking=ranking, ignore_pantry=ignore_pantry)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->search_recipes_by_ingredients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingredients** | **str**| A comma-separated list of ingredients that the recipes should contain. | [optional]
 **number** | **int**| The maximum number of items to return (between 1 and 100). Defaults to 10. | [optional] if omitted the server will use the default value of 10
 **limit_license** | **bool**| Whether the recipes should have an open license that allows display with proper attribution. | [optional] if omitted the server will use the default value of True
 **ranking** | **float**| Whether to maximize used ingredients (1) or minimize missing ingredients (2) first. | [optional]
 **ignore_pantry** | **bool**| Whether to ignore typical pantry items, such as water, salt, flour, etc. | [optional] if omitted the server will use the default value of False

### Return type

[**[SearchRecipesByIngredients200ResponseInner]**](SearchRecipesByIngredients200ResponseInner.md)

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

# **search_recipes_by_nutrients**
> [SearchRecipesByNutrients200ResponseInner] search_recipes_by_nutrients()

Search Recipes by Nutrients

Find a set of recipes that adhere to the given nutritional limits. You may set limits for macronutrients (calories, protein, fat, and carbohydrate) and/or many micronutrients.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.search_recipes_by_nutrients200_response_inner import SearchRecipesByNutrients200ResponseInner
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
    api_instance = recipes_api.RecipesApi(api_client)
    min_carbs = 10 # float | The minimum amount of carbohydrates in grams the recipe must have. (optional)
    max_carbs = 100 # float | The maximum amount of carbohydrates in grams the recipe can have. (optional)
    min_protein = 10 # float | The minimum amount of protein in grams the recipe must have. (optional)
    max_protein = 100 # float | The maximum amount of protein in grams the recipe can have. (optional)
    min_calories = 50 # float | The minimum amount of calories the recipe must have. (optional)
    max_calories = 800 # float | The maximum amount of calories the recipe can have. (optional)
    min_fat = 1 # float | The minimum amount of fat in grams the recipe must have. (optional)
    max_fat = 100 # float | The maximum amount of fat in grams the recipe can have. (optional)
    min_alcohol = 0 # float | The minimum amount of alcohol in grams the recipe must have. (optional)
    max_alcohol = 100 # float | The maximum amount of alcohol in grams the recipe can have. (optional)
    min_caffeine = 0 # float | The minimum amount of caffeine in milligrams the recipe must have. (optional)
    max_caffeine = 100 # float | The maximum amount of caffeine in milligrams the recipe can have. (optional)
    min_copper = 0 # float | The minimum amount of copper in milligrams the recipe must have. (optional)
    max_copper = 100 # float | The maximum amount of copper in milligrams the recipe can have. (optional)
    min_calcium = 0 # float | The minimum amount of calcium in milligrams the recipe must have. (optional)
    max_calcium = 100 # float | The maximum amount of calcium in milligrams the recipe can have. (optional)
    min_choline = 0 # float | The minimum amount of choline in milligrams the recipe must have. (optional)
    max_choline = 100 # float | The maximum amount of choline in milligrams the recipe can have. (optional)
    min_cholesterol = 0 # float | The minimum amount of cholesterol in milligrams the recipe must have. (optional)
    max_cholesterol = 100 # float | The maximum amount of cholesterol in milligrams the recipe can have. (optional)
    min_fluoride = 0 # float | The minimum amount of fluoride in milligrams the recipe must have. (optional)
    max_fluoride = 100 # float | The maximum amount of fluoride in milligrams the recipe can have. (optional)
    min_saturated_fat = 0 # float | The minimum amount of saturated fat in grams the recipe must have. (optional)
    max_saturated_fat = 100 # float | The maximum amount of saturated fat in grams the recipe can have. (optional)
    min_vitamin_a = 0 # float | The minimum amount of Vitamin A in IU the recipe must have. (optional)
    max_vitamin_a = 100 # float | The maximum amount of Vitamin A in IU the recipe can have. (optional)
    min_vitamin_c = 0 # float | The minimum amount of Vitamin C in milligrams the recipe must have. (optional)
    max_vitamin_c = 100 # float | The maximum amount of Vitamin C in milligrams the recipe can have. (optional)
    min_vitamin_d = 0 # float | The minimum amount of Vitamin D in micrograms the recipe must have. (optional)
    max_vitamin_d = 100 # float | The maximum amount of Vitamin D in micrograms the recipe can have. (optional)
    min_vitamin_e = 0 # float | The minimum amount of Vitamin E in milligrams the recipe must have. (optional)
    max_vitamin_e = 100 # float | The maximum amount of Vitamin E in milligrams the recipe can have. (optional)
    min_vitamin_k = 0 # float | The minimum amount of Vitamin K in micrograms the recipe must have. (optional)
    max_vitamin_k = 100 # float | The maximum amount of Vitamin K in micrograms the recipe can have. (optional)
    min_vitamin_b1 = 0 # float | The minimum amount of Vitamin B1 in milligrams the recipe must have. (optional)
    max_vitamin_b1 = 100 # float | The maximum amount of Vitamin B1 in milligrams the recipe can have. (optional)
    min_vitamin_b2 = 0 # float | The minimum amount of Vitamin B2 in milligrams the recipe must have. (optional)
    max_vitamin_b2 = 100 # float | The maximum amount of Vitamin B2 in milligrams the recipe can have. (optional)
    min_vitamin_b5 = 0 # float | The minimum amount of Vitamin B5 in milligrams the recipe must have. (optional)
    max_vitamin_b5 = 100 # float | The maximum amount of Vitamin B5 in milligrams the recipe can have. (optional)
    min_vitamin_b3 = 0 # float | The minimum amount of Vitamin B3 in milligrams the recipe must have. (optional)
    max_vitamin_b3 = 100 # float | The maximum amount of Vitamin B3 in milligrams the recipe can have. (optional)
    min_vitamin_b6 = 0 # float | The minimum amount of Vitamin B6 in milligrams the recipe must have. (optional)
    max_vitamin_b6 = 100 # float | The maximum amount of Vitamin B6 in milligrams the recipe can have. (optional)
    min_vitamin_b12 = 0 # float | The minimum amount of Vitamin B12 in micrograms the recipe must have. (optional)
    max_vitamin_b12 = 100 # float | The maximum amount of Vitamin B12 in micrograms the recipe can have. (optional)
    min_fiber = 0 # float | The minimum amount of fiber in grams the recipe must have. (optional)
    max_fiber = 100 # float | The maximum amount of fiber in grams the recipe can have. (optional)
    min_folate = 0 # float | The minimum amount of folate in micrograms the recipe must have. (optional)
    max_folate = 100 # float | The maximum amount of folate in micrograms the recipe can have. (optional)
    min_folic_acid = 0 # float | The minimum amount of folic acid in micrograms the recipe must have. (optional)
    max_folic_acid = 100 # float | The maximum amount of folic acid in micrograms the recipe can have. (optional)
    min_iodine = 0 # float | The minimum amount of iodine in micrograms the recipe must have. (optional)
    max_iodine = 100 # float | The maximum amount of iodine in micrograms the recipe can have. (optional)
    min_iron = 0 # float | The minimum amount of iron in milligrams the recipe must have. (optional)
    max_iron = 100 # float | The maximum amount of iron in milligrams the recipe can have. (optional)
    min_magnesium = 0 # float | The minimum amount of magnesium in milligrams the recipe must have. (optional)
    max_magnesium = 100 # float | The maximum amount of magnesium in milligrams the recipe can have. (optional)
    min_manganese = 0 # float | The minimum amount of manganese in milligrams the recipe must have. (optional)
    max_manganese = 100 # float | The maximum amount of manganese in milligrams the recipe can have. (optional)
    min_phosphorus = 0 # float | The minimum amount of phosphorus in milligrams the recipe must have. (optional)
    max_phosphorus = 100 # float | The maximum amount of phosphorus in milligrams the recipe can have. (optional)
    min_potassium = 0 # float | The minimum amount of potassium in milligrams the recipe must have. (optional)
    max_potassium = 100 # float | The maximum amount of potassium in milligrams the recipe can have. (optional)
    min_selenium = 0 # float | The minimum amount of selenium in micrograms the recipe must have. (optional)
    max_selenium = 100 # float | The maximum amount of selenium in micrograms the recipe can have. (optional)
    min_sodium = 0 # float | The minimum amount of sodium in milligrams the recipe must have. (optional)
    max_sodium = 100 # float | The maximum amount of sodium in milligrams the recipe can have. (optional)
    min_sugar = 0 # float | The minimum amount of sugar in grams the recipe must have. (optional)
    max_sugar = 100 # float | The maximum amount of sugar in grams the recipe can have. (optional)
    min_zinc = 0 # float | The minimum amount of zinc in milligrams the recipe must have. (optional)
    max_zinc = 100 # float | The maximum amount of zinc in milligrams the recipe can have. (optional)
    offset = 0 # int | The number of results to skip (between 0 and 900). (optional)
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) if omitted the server will use the default value of 10
    random = False # bool | If true, every request will give you a random set of recipes within the requested limits. (optional)
    limit_license = True # bool | Whether the recipes should have an open license that allows display with proper attribution. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Recipes by Nutrients
        api_response = api_instance.search_recipes_by_nutrients(min_carbs=min_carbs, max_carbs=max_carbs, min_protein=min_protein, max_protein=max_protein, min_calories=min_calories, max_calories=max_calories, min_fat=min_fat, max_fat=max_fat, min_alcohol=min_alcohol, max_alcohol=max_alcohol, min_caffeine=min_caffeine, max_caffeine=max_caffeine, min_copper=min_copper, max_copper=max_copper, min_calcium=min_calcium, max_calcium=max_calcium, min_choline=min_choline, max_choline=max_choline, min_cholesterol=min_cholesterol, max_cholesterol=max_cholesterol, min_fluoride=min_fluoride, max_fluoride=max_fluoride, min_saturated_fat=min_saturated_fat, max_saturated_fat=max_saturated_fat, min_vitamin_a=min_vitamin_a, max_vitamin_a=max_vitamin_a, min_vitamin_c=min_vitamin_c, max_vitamin_c=max_vitamin_c, min_vitamin_d=min_vitamin_d, max_vitamin_d=max_vitamin_d, min_vitamin_e=min_vitamin_e, max_vitamin_e=max_vitamin_e, min_vitamin_k=min_vitamin_k, max_vitamin_k=max_vitamin_k, min_vitamin_b1=min_vitamin_b1, max_vitamin_b1=max_vitamin_b1, min_vitamin_b2=min_vitamin_b2, max_vitamin_b2=max_vitamin_b2, min_vitamin_b5=min_vitamin_b5, max_vitamin_b5=max_vitamin_b5, min_vitamin_b3=min_vitamin_b3, max_vitamin_b3=max_vitamin_b3, min_vitamin_b6=min_vitamin_b6, max_vitamin_b6=max_vitamin_b6, min_vitamin_b12=min_vitamin_b12, max_vitamin_b12=max_vitamin_b12, min_fiber=min_fiber, max_fiber=max_fiber, min_folate=min_folate, max_folate=max_folate, min_folic_acid=min_folic_acid, max_folic_acid=max_folic_acid, min_iodine=min_iodine, max_iodine=max_iodine, min_iron=min_iron, max_iron=max_iron, min_magnesium=min_magnesium, max_magnesium=max_magnesium, min_manganese=min_manganese, max_manganese=max_manganese, min_phosphorus=min_phosphorus, max_phosphorus=max_phosphorus, min_potassium=min_potassium, max_potassium=max_potassium, min_selenium=min_selenium, max_selenium=max_selenium, min_sodium=min_sodium, max_sodium=max_sodium, min_sugar=min_sugar, max_sugar=max_sugar, min_zinc=min_zinc, max_zinc=max_zinc, offset=offset, number=number, random=random, limit_license=limit_license)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->search_recipes_by_nutrients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_carbs** | **float**| The minimum amount of carbohydrates in grams the recipe must have. | [optional]
 **max_carbs** | **float**| The maximum amount of carbohydrates in grams the recipe can have. | [optional]
 **min_protein** | **float**| The minimum amount of protein in grams the recipe must have. | [optional]
 **max_protein** | **float**| The maximum amount of protein in grams the recipe can have. | [optional]
 **min_calories** | **float**| The minimum amount of calories the recipe must have. | [optional]
 **max_calories** | **float**| The maximum amount of calories the recipe can have. | [optional]
 **min_fat** | **float**| The minimum amount of fat in grams the recipe must have. | [optional]
 **max_fat** | **float**| The maximum amount of fat in grams the recipe can have. | [optional]
 **min_alcohol** | **float**| The minimum amount of alcohol in grams the recipe must have. | [optional]
 **max_alcohol** | **float**| The maximum amount of alcohol in grams the recipe can have. | [optional]
 **min_caffeine** | **float**| The minimum amount of caffeine in milligrams the recipe must have. | [optional]
 **max_caffeine** | **float**| The maximum amount of caffeine in milligrams the recipe can have. | [optional]
 **min_copper** | **float**| The minimum amount of copper in milligrams the recipe must have. | [optional]
 **max_copper** | **float**| The maximum amount of copper in milligrams the recipe can have. | [optional]
 **min_calcium** | **float**| The minimum amount of calcium in milligrams the recipe must have. | [optional]
 **max_calcium** | **float**| The maximum amount of calcium in milligrams the recipe can have. | [optional]
 **min_choline** | **float**| The minimum amount of choline in milligrams the recipe must have. | [optional]
 **max_choline** | **float**| The maximum amount of choline in milligrams the recipe can have. | [optional]
 **min_cholesterol** | **float**| The minimum amount of cholesterol in milligrams the recipe must have. | [optional]
 **max_cholesterol** | **float**| The maximum amount of cholesterol in milligrams the recipe can have. | [optional]
 **min_fluoride** | **float**| The minimum amount of fluoride in milligrams the recipe must have. | [optional]
 **max_fluoride** | **float**| The maximum amount of fluoride in milligrams the recipe can have. | [optional]
 **min_saturated_fat** | **float**| The minimum amount of saturated fat in grams the recipe must have. | [optional]
 **max_saturated_fat** | **float**| The maximum amount of saturated fat in grams the recipe can have. | [optional]
 **min_vitamin_a** | **float**| The minimum amount of Vitamin A in IU the recipe must have. | [optional]
 **max_vitamin_a** | **float**| The maximum amount of Vitamin A in IU the recipe can have. | [optional]
 **min_vitamin_c** | **float**| The minimum amount of Vitamin C in milligrams the recipe must have. | [optional]
 **max_vitamin_c** | **float**| The maximum amount of Vitamin C in milligrams the recipe can have. | [optional]
 **min_vitamin_d** | **float**| The minimum amount of Vitamin D in micrograms the recipe must have. | [optional]
 **max_vitamin_d** | **float**| The maximum amount of Vitamin D in micrograms the recipe can have. | [optional]
 **min_vitamin_e** | **float**| The minimum amount of Vitamin E in milligrams the recipe must have. | [optional]
 **max_vitamin_e** | **float**| The maximum amount of Vitamin E in milligrams the recipe can have. | [optional]
 **min_vitamin_k** | **float**| The minimum amount of Vitamin K in micrograms the recipe must have. | [optional]
 **max_vitamin_k** | **float**| The maximum amount of Vitamin K in micrograms the recipe can have. | [optional]
 **min_vitamin_b1** | **float**| The minimum amount of Vitamin B1 in milligrams the recipe must have. | [optional]
 **max_vitamin_b1** | **float**| The maximum amount of Vitamin B1 in milligrams the recipe can have. | [optional]
 **min_vitamin_b2** | **float**| The minimum amount of Vitamin B2 in milligrams the recipe must have. | [optional]
 **max_vitamin_b2** | **float**| The maximum amount of Vitamin B2 in milligrams the recipe can have. | [optional]
 **min_vitamin_b5** | **float**| The minimum amount of Vitamin B5 in milligrams the recipe must have. | [optional]
 **max_vitamin_b5** | **float**| The maximum amount of Vitamin B5 in milligrams the recipe can have. | [optional]
 **min_vitamin_b3** | **float**| The minimum amount of Vitamin B3 in milligrams the recipe must have. | [optional]
 **max_vitamin_b3** | **float**| The maximum amount of Vitamin B3 in milligrams the recipe can have. | [optional]
 **min_vitamin_b6** | **float**| The minimum amount of Vitamin B6 in milligrams the recipe must have. | [optional]
 **max_vitamin_b6** | **float**| The maximum amount of Vitamin B6 in milligrams the recipe can have. | [optional]
 **min_vitamin_b12** | **float**| The minimum amount of Vitamin B12 in micrograms the recipe must have. | [optional]
 **max_vitamin_b12** | **float**| The maximum amount of Vitamin B12 in micrograms the recipe can have. | [optional]
 **min_fiber** | **float**| The minimum amount of fiber in grams the recipe must have. | [optional]
 **max_fiber** | **float**| The maximum amount of fiber in grams the recipe can have. | [optional]
 **min_folate** | **float**| The minimum amount of folate in micrograms the recipe must have. | [optional]
 **max_folate** | **float**| The maximum amount of folate in micrograms the recipe can have. | [optional]
 **min_folic_acid** | **float**| The minimum amount of folic acid in micrograms the recipe must have. | [optional]
 **max_folic_acid** | **float**| The maximum amount of folic acid in micrograms the recipe can have. | [optional]
 **min_iodine** | **float**| The minimum amount of iodine in micrograms the recipe must have. | [optional]
 **max_iodine** | **float**| The maximum amount of iodine in micrograms the recipe can have. | [optional]
 **min_iron** | **float**| The minimum amount of iron in milligrams the recipe must have. | [optional]
 **max_iron** | **float**| The maximum amount of iron in milligrams the recipe can have. | [optional]
 **min_magnesium** | **float**| The minimum amount of magnesium in milligrams the recipe must have. | [optional]
 **max_magnesium** | **float**| The maximum amount of magnesium in milligrams the recipe can have. | [optional]
 **min_manganese** | **float**| The minimum amount of manganese in milligrams the recipe must have. | [optional]
 **max_manganese** | **float**| The maximum amount of manganese in milligrams the recipe can have. | [optional]
 **min_phosphorus** | **float**| The minimum amount of phosphorus in milligrams the recipe must have. | [optional]
 **max_phosphorus** | **float**| The maximum amount of phosphorus in milligrams the recipe can have. | [optional]
 **min_potassium** | **float**| The minimum amount of potassium in milligrams the recipe must have. | [optional]
 **max_potassium** | **float**| The maximum amount of potassium in milligrams the recipe can have. | [optional]
 **min_selenium** | **float**| The minimum amount of selenium in micrograms the recipe must have. | [optional]
 **max_selenium** | **float**| The maximum amount of selenium in micrograms the recipe can have. | [optional]
 **min_sodium** | **float**| The minimum amount of sodium in milligrams the recipe must have. | [optional]
 **max_sodium** | **float**| The maximum amount of sodium in milligrams the recipe can have. | [optional]
 **min_sugar** | **float**| The minimum amount of sugar in grams the recipe must have. | [optional]
 **max_sugar** | **float**| The maximum amount of sugar in grams the recipe can have. | [optional]
 **min_zinc** | **float**| The minimum amount of zinc in milligrams the recipe must have. | [optional]
 **max_zinc** | **float**| The maximum amount of zinc in milligrams the recipe can have. | [optional]
 **offset** | **int**| The number of results to skip (between 0 and 900). | [optional]
 **number** | **int**| The maximum number of items to return (between 1 and 100). Defaults to 10. | [optional] if omitted the server will use the default value of 10
 **random** | **bool**| If true, every request will give you a random set of recipes within the requested limits. | [optional]
 **limit_license** | **bool**| Whether the recipes should have an open license that allows display with proper attribution. | [optional] if omitted the server will use the default value of True

### Return type

[**[SearchRecipesByNutrients200ResponseInner]**](SearchRecipesByNutrients200ResponseInner.md)

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

# **summarize_recipe**
> SummarizeRecipe200Response summarize_recipe(id)

Summarize Recipe

Automatically generate a short description that summarizes key information about the recipe.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
from openapi_client.model.summarize_recipe200_response import SummarizeRecipe200Response
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.

    # example passing only required values which don't have defaults set
    try:
        # Summarize Recipe
        api_response = api_instance.summarize_recipe(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->summarize_recipe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |

### Return type

[**SummarizeRecipe200Response**](SummarizeRecipe200Response.md)

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

# **visualize_equipment**
> str visualize_equipment()

Equipment Widget

Visualize the equipment used to make a recipe.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)
    accept = "application/json" # str | Accept header. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Equipment Widget
        api_response = api_instance.visualize_equipment(content_type=content_type, accept=accept)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_equipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]
 **accept** | **str**| Accept header. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_price_breakdown**
> str visualize_price_breakdown()

Price Breakdown Widget

Visualize the price breakdown of a recipe.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)
    accept = "application/json" # str | Accept header. (optional)
    language = "en" # str | The language of the input. Either 'en' or 'de'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Price Breakdown Widget
        api_response = api_instance.visualize_price_breakdown(content_type=content_type, accept=accept, language=language)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_price_breakdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]
 **accept** | **str**| Accept header. | [optional]
 **language** | **str**| The language of the input. Either &#39;en&#39; or &#39;de&#39;. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_equipment_by_id**
> str visualize_recipe_equipment_by_id(id)

Equipment by ID Widget

Visualize a recipe's equipment list.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    default_css = False # bool | Whether the default CSS should be added to the response. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Equipment by ID Widget
        api_response = api_instance.visualize_recipe_equipment_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_equipment_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Equipment by ID Widget
        api_response = api_instance.visualize_recipe_equipment_by_id(id, default_css=default_css)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_equipment_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **default_css** | **bool**| Whether the default CSS should be added to the response. | [optional] if omitted the server will use the default value of True

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_ingredients_by_id**
> str visualize_recipe_ingredients_by_id(id)

Ingredients by ID Widget

Visualize a recipe's ingredient list.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    default_css = False # bool | Whether the default CSS should be added to the response. (optional) if omitted the server will use the default value of True
    measure = "metric" # str | Whether the the measures should be 'us' or 'metric'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ingredients by ID Widget
        api_response = api_instance.visualize_recipe_ingredients_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_ingredients_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ingredients by ID Widget
        api_response = api_instance.visualize_recipe_ingredients_by_id(id, default_css=default_css, measure=measure)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_ingredients_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **default_css** | **bool**| Whether the default CSS should be added to the response. | [optional] if omitted the server will use the default value of True
 **measure** | **str**| Whether the the measures should be &#39;us&#39; or &#39;metric&#39;. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_nutrition**
> str visualize_recipe_nutrition()

Recipe Nutrition Widget

Visualize a recipe's nutritional information as HTML including CSS.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    content_type = "application/json" # str | The content type. (optional)
    accept = "application/json" # str | Accept header. (optional)
    language = "en" # str | The language of the input. Either 'en' or 'de'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Nutrition Widget
        api_response = api_instance.visualize_recipe_nutrition(content_type=content_type, accept=accept, language=language)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_nutrition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type. | [optional]
 **accept** | **str**| Accept header. | [optional]
 **language** | **str**| The language of the input. Either &#39;en&#39; or &#39;de&#39;. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_nutrition_by_id**
> str visualize_recipe_nutrition_by_id(id)

Recipe Nutrition by ID Widget

Visualize a recipe's nutritional information as HTML including CSS.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    default_css = False # bool | Whether the default CSS should be added to the response. (optional) if omitted the server will use the default value of True
    accept = "application/json" # str | Accept header. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recipe Nutrition by ID Widget
        api_response = api_instance.visualize_recipe_nutrition_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_nutrition_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Nutrition by ID Widget
        api_response = api_instance.visualize_recipe_nutrition_by_id(id, default_css=default_css, accept=accept)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_nutrition_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **default_css** | **bool**| Whether the default CSS should be added to the response. | [optional] if omitted the server will use the default value of True
 **accept** | **str**| Accept header. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_price_breakdown_by_id**
> str visualize_recipe_price_breakdown_by_id(id)

Price Breakdown by ID Widget

Visualize a recipe's price breakdown.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    default_css = False # bool | Whether the default CSS should be added to the response. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Price Breakdown by ID Widget
        api_response = api_instance.visualize_recipe_price_breakdown_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_price_breakdown_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Price Breakdown by ID Widget
        api_response = api_instance.visualize_recipe_price_breakdown_by_id(id, default_css=default_css)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_price_breakdown_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **default_css** | **bool**| Whether the default CSS should be added to the response. | [optional] if omitted the server will use the default value of True

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_taste**
> str visualize_recipe_taste()

Recipe Taste Widget

Visualize a recipe's taste information as HTML including CSS. You can play around with that endpoint!

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    language = "en" # str | The language of the input. Either 'en' or 'de'. (optional)
    content_type = "application/json" # str | The content type. (optional)
    accept = "application/json" # str | Accept header. (optional)
    normalize = True # bool | Whether to normalize to the strongest taste. (optional)
    rgb = "75,192,192" # str | Red, green, blue values for the chart color. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Taste Widget
        api_response = api_instance.visualize_recipe_taste(language=language, content_type=content_type, accept=accept, normalize=normalize, rgb=rgb)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_taste: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| The language of the input. Either &#39;en&#39; or &#39;de&#39;. | [optional]
 **content_type** | **str**| The content type. | [optional]
 **accept** | **str**| Accept header. | [optional]
 **normalize** | **bool**| Whether to normalize to the strongest taste. | [optional]
 **rgb** | **str**| Red, green, blue values for the chart color. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualize_recipe_taste_by_id**
> str visualize_recipe_taste_by_id(id)

Recipe Taste by ID Widget

Get a recipe's taste. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

### Example

* Api Key Authentication (apiKeyScheme):

```python
import time
import openapi_client
from com.spoonacular import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    id = 1 # int | The item's id.
    normalize = True # bool | Whether to normalize to the strongest taste. (optional) if omitted the server will use the default value of True
    rgb = "75,192,192" # str | Red, green, blue values for the chart color. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recipe Taste by ID Widget
        api_response = api_instance.visualize_recipe_taste_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_taste_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recipe Taste by ID Widget
        api_response = api_instance.visualize_recipe_taste_by_id(id, normalize=normalize, rgb=rgb)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->visualize_recipe_taste_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The item&#39;s id. |
 **normalize** | **bool**| Whether to normalize to the strongest taste. | [optional] if omitted the server will use the default value of True
 **rgb** | **str**| Red, green, blue values for the chart color. | [optional]

### Return type

**str**

### Authorization

[apiKeyScheme](../README.md#apiKeyScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

