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

import com.spoonacular.client.model.GetAnalyzedRecipeInstructions200ResponseIngredientsInner;
import java.util.*;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * 
 **/
@ApiModel(description = "")
public class GetMealPlanTemplates200Response {
  
  @SerializedName("templates")
  private Set<GetAnalyzedRecipeInstructions200ResponseIngredientsInner> templates = null;

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public Set<GetAnalyzedRecipeInstructions200ResponseIngredientsInner> getTemplates() {
    return templates;
  }
  public void setTemplates(Set<GetAnalyzedRecipeInstructions200ResponseIngredientsInner> templates) {
    this.templates = templates;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetMealPlanTemplates200Response getMealPlanTemplates200Response = (GetMealPlanTemplates200Response) o;
    return (this.templates == null ? getMealPlanTemplates200Response.templates == null : this.templates.equals(getMealPlanTemplates200Response.templates));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.templates == null ? 0: this.templates.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetMealPlanTemplates200Response {\n");
    
    sb.append("  templates: ").append(templates).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}
