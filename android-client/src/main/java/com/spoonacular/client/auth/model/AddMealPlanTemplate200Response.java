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

import com.spoonacular.client.model.AddMealPlanTemplate200ResponseItemsInner;
import java.util.*;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * 
 **/
@ApiModel(description = "")
public class AddMealPlanTemplate200Response {
  
  @SerializedName("name")
  private String name = null;
  @SerializedName("items")
  private Set<AddMealPlanTemplate200ResponseItemsInner> items = null;
  @SerializedName("publishAsPublic")
  private Boolean publishAsPublic = null;

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public Set<AddMealPlanTemplate200ResponseItemsInner> getItems() {
    return items;
  }
  public void setItems(Set<AddMealPlanTemplate200ResponseItemsInner> items) {
    this.items = items;
  }

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public Boolean getPublishAsPublic() {
    return publishAsPublic;
  }
  public void setPublishAsPublic(Boolean publishAsPublic) {
    this.publishAsPublic = publishAsPublic;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddMealPlanTemplate200Response addMealPlanTemplate200Response = (AddMealPlanTemplate200Response) o;
    return (this.name == null ? addMealPlanTemplate200Response.name == null : this.name.equals(addMealPlanTemplate200Response.name)) &&
        (this.items == null ? addMealPlanTemplate200Response.items == null : this.items.equals(addMealPlanTemplate200Response.items)) &&
        (this.publishAsPublic == null ? addMealPlanTemplate200Response.publishAsPublic == null : this.publishAsPublic.equals(addMealPlanTemplate200Response.publishAsPublic));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.name == null ? 0: this.name.hashCode());
    result = 31 * result + (this.items == null ? 0: this.items.hashCode());
    result = 31 * result + (this.publishAsPublic == null ? 0: this.publishAsPublic.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddMealPlanTemplate200Response {\n");
    
    sb.append("  name: ").append(name).append("\n");
    sb.append("  items: ").append(items).append("\n");
    sb.append("  publishAsPublic: ").append(publishAsPublic).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}
