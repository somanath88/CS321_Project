import openapi_client
import time
import openapi_client
from pprint import pprint
from com.spoonacular import ingredients_api
from openapi_client.model.autocomplete_ingredient_search200_response_inner import AutocompleteIngredientSearch200ResponseInner
from openapi_client.model.compute_ingredient_amount200_response import ComputeIngredientAmount200Response
from openapi_client.model.get_ingredient_information200_response import GetIngredientInformation200Response
from openapi_client.model.get_ingredient_substitutes200_response import GetIngredientSubstitutes200Response
from openapi_client.model.ingredient_search200_response import IngredientSearch200Response
from openapi_client.model.map_ingredients_to_grocery_products200_response_inner import MapIngredientsToGroceryProducts200ResponseInner
from openapi_client.model.map_ingredients_to_grocery_products_request import MapIngredientsToGroceryProductsRequest
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
    api_instance = ingredients_api.IngredientsApi(api_client)
    query = "burger" # str | The (natural language) search query. (optional)
    number = 10 # int | The maximum number of items to return (between 1 and 100). Defaults to 10. (optional) (default to 10)
    meta_information = False # bool | Whether to return more meta information about the ingredients. (optional)
    intolerances = "egg" # str | A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances. (optional)

    try:
        # Autocomplete Ingredient Search
        api_response = api_instance.autocomplete_ingredient_search(query=query, number=number, meta_information=meta_information, intolerances=intolerances)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IngredientsApi->autocomplete_ingredient_search: %s\n" % e)