import streamlit as st
import requests
import json
import time
from PIL import Image

st.set_page_config(page_title="30%70",page_icon = ":🧊:", layout= "wide")
st.header("30/70")


 

tab1, tab2, tab3, tab4 = st.tabs(["Meal Finder", "Groceries", "Weight Tracker", "Find Restaurants"])

with tab1:
   st.header("Meal Finder")
   st.image("https://media.cnn.com/api/v1/images/stellar/prod/201222103421-healthyfactor-meals.jpg",width=400)
   calories=st.slider('Calories',50, 800, None,5)
   maxProtein= st.slider('Maximum Protein',10,100,None,1,)
   minProtein=st.slider('Minimum Protein',10, 100, None,1)
   maxCarbs= st.slider('Maximum Carbs',10,100,None,1,)
   minCarbs=st.slider('Minimum Carbs',10, 100, None,1)
   maxFat= st.slider('Maximum Fat',1,100,None,1,)
   minFat=st.slider('Minimum Fat',1, 100, None,1)

   if st.button('Find Meal'):
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search"

        querystring = {"query":"burger","offset":"0","number":"1","minCalories":50,"maxCalories":calories,"minProtein":minFat,"maxProtein":maxProtein,"minFat":minFat,"maxFat":maxFat,"minCarbs":minCarbs,"maxCarbs":maxCarbs}

        headers = {
            "X-RapidAPI-Key": "e3204cea803349a783d0c7a7f379c3c1",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        st.write(response.json())

with tab2:
   st.header("Groceries")
   st.image("https://hips.hearstapps.com/hmg-prod/images/healthy-groceries-1525213305.jpg", width=400)
   itemName = st.text_input("Item's Name:");
   if itemName:
      st.write('Input the macros of ',itemName)
   itemCalories = st.number_input('Calories:', min_value=0, max_value=800, value=50, step=10)
   itemProteins = st.number_input('Protein:', min_value=0, max_value=100, value=0, step=1)
   itemCarbs = st.number_input('Carbs:', min_value=0, max_value=100, value=0, step=1)
   itemFats = st.number_input('Fats:', min_value=0, max_value=100, value=0, step=1)

   if st.button('Find Item'):
      url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/search"

      querystring = {"query":itemName,"maxCalories":itemCalories,"minProtein":"0","maxProtein":itemProteins,"minFat":"0","maxFat":itemFats,"minCarbs":"0","maxCarbs":itemCarbs,"minCalories":"0","offset":"0","number":"20"}

      headers = {
         "X-RapidAPI-Key": "442463fda5msh2003056aa2a46ebp1d1738jsn41994962d005",
         "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
      }

      response = requests.request("GET", url, headers=headers, params=querystring)

      result = response.json()


      for i in result["products"]:
         st.image(i["image"], caption=i["title"])
         st.write("")




with tab3:
   st.header("Weight Tracker")
   st.image("https://assets.roguefitness.com/f_auto,q_auto,c_limit,w_1536,b_rgb:f8f8f8/catalog/Conditioning/Strength%20Equipment/Dumbbells/IP1100/IP1100-H_ejvjae.png", width=400)
   
with tab4:
   col1, col3, col2 = st.columns((2,2,2))
   with st.sidebar:
      st.title("Pick a type of cuisine")
      cuisine = st.radio(label = "Cuisine Type", options = ['Mexican', 'Italian', 'Chinese', 'Mediterranean'], help = "Select a cuisine out of **4** choices")
      st.header("Pick your restaurant(s) attributes")
      budget = st.number_input(
         "Budget",
         help = "Enter a budget by **typing** or using the **buttons** on the right (in USD)"
      )
      distance = st.text_input(
         "Distance limit",
         placeholder= "Enter a distantance limit",
      )
      rating = st.number_input(
         "Minimum rating",
         help = "Enter a rating by **typing** or using the **buttons** on the right",
         max_value= 5.00
      )
      button = st.button('Find Restaurant')
   if button:
      url = "https://api.spoonacular.com/food/restaurants/search?apiKey=e3204cea803349a783d0c7a7f379c3c1"
      querystring = {"query": "", "lat": 38.835268, "lng": -77.309476,
      "distance": int(distance), "budget": int(budget), "cuisine": cuisine, "min-rating": float(rating),
      "sort": "", "page": 0}

      headers = {
         "X-RapidAPI-Key": "e3204cea803349a783d0c7a7f379c3c1",
         "X-RapidAPI-Host": "https://api.spoonacular.com"
      }
      with st.spinner("Loading..."):
        time.sleep(5)
      response = requests.request("GET", url, headers=headers, params=querystring)
      data = response.json()
      for info in data["restaurants"]:
         with col1:
            for img in info["logo_photos"]:
               st.image(img, width = 200, caption = "Source: " + info["name"])
               st.write("-----------------------------------------------------------")
         with col3:
            st.write("Name: " + info["name"])
            st.write("Average rating: " + str(round(info["weighted_rating_value"], 1)))
            if(info["is_open"] == False):
               st.write("Closed at the moment.")
            if(info["is_open"] == True):
               st.write("Open!")
            st.write("Phone number: " + str(info["phone_number"]))
            st.write("Street address: " + info["address"]["street_addr"])
            st.write("\n")
            st.write("-----------------------------------------------------------")
      st.success("Done!")
