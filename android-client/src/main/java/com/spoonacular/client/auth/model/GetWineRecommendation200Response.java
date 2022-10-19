/**
 * spoonacular API
 * The spoonacular Nutrition, Recipe, and Food API allows you to access over 380,000 recipes, thousands of ingredients, 800,000 food products, and 100,000 menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.
 *
 * The version of the OpenAPI document: 1.1
 * Contact: mail@spoonacular.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package com.spoonacular.client.model;

import com.spoonacular.client.model.GetWineRecommendation200ResponseRecommendedWinesInner;
import java.util.*;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * 
 **/
@ApiModel(description = "")
public class GetWineRecommendation200Response {
  
  @SerializedName("recommendedWines")
  private Set<GetWineRecommendation200ResponseRecommendedWinesInner> recommendedWines = null;
  @SerializedName("totalFound")
  private Integer totalFound = null;

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public Set<GetWineRecommendation200ResponseRecommendedWinesInner> getRecommendedWines() {
    return recommendedWines;
  }
  public void setRecommendedWines(Set<GetWineRecommendation200ResponseRecommendedWinesInner> recommendedWines) {
    this.recommendedWines = recommendedWines;
  }

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public Integer getTotalFound() {
    return totalFound;
  }
  public void setTotalFound(Integer totalFound) {
    this.totalFound = totalFound;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetWineRecommendation200Response getWineRecommendation200Response = (GetWineRecommendation200Response) o;
    return (this.recommendedWines == null ? getWineRecommendation200Response.recommendedWines == null : this.recommendedWines.equals(getWineRecommendation200Response.recommendedWines)) &&
        (this.totalFound == null ? getWineRecommendation200Response.totalFound == null : this.totalFound.equals(getWineRecommendation200Response.totalFound));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.recommendedWines == null ? 0: this.recommendedWines.hashCode());
    result = 31 * result + (this.totalFound == null ? 0: this.totalFound.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetWineRecommendation200Response {\n");
    
    sb.append("  recommendedWines: ").append(recommendedWines).append("\n");
    sb.append("  totalFound: ").append(totalFound).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}
