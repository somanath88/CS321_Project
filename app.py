import streamlit as st
import requests
st.set_page_config(page_title="30%70",page_icon = ":🧊:", layout= "wide")
st.header("30/70")


# if st.button('Meal Finder'):
#     st.write(meal_finder)    

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

with tab3:
   st.header("Weight Tracker")
   st.image("https://assets.roguefitness.com/f_auto,q_auto,c_limit,w_1536,b_rgb:f8f8f8/catalog/Conditioning/Strength%20Equipment/Dumbbells/IP1100/IP1100-H_ejvjae.png", width=400)
   
with tab4:
   st.header("Restaurants")
   st.image("https://images.pexels.com/photos/941861/pexels-photo-941861.jpeg?cs=srgb&dl=pexels-chan-walrus-941861.jpg&fm=jpg",width=400)
   cuisine = st.text_input(
        "Pick a type of cuisine",
        placeholder= "Enter a cuisine",
   )
   budget = st.text_input(
        "Enter your budget",
        placeholder= "Enter a budget",
   )
   distance = st.text_input(
        "Enter restaurant distance limit in miles",
        placeholder= "Enter a distant limit",
   )
   rating = st.text_input(
        "Enter minimum rating for restaurant",
        placeholder= "Enter a rating",
   )
   if st.button('Find Restaurant'):
      url = "https://api.spoonacular.com/food/restaurants/search?apiKey=e3204cea803349a783d0c7a7f379c3c1"
      querystring = {"query": "", "lat": 38.835268, "lng": -77.309476,
      "distance": int(distance), "budget": int(budget), "cuisine": cuisine, "min-rating": float(rating),
      "sort": "cheapest", "page": 0}

      '''
      no sure we need this but I kept
      it just in case
      
      p.s delete this comment when necessary! (eventually all comments needs to be deleted)
      '''
      headers = {
         "X-RapidAPI-Key": "e3204cea803349a783d0c7a7f379c3c1",
         "X-RapidAPI-Host": "https://api.spoonacular.com"
      }

      response = requests.request("GET", url, headers=headers, params=querystring)
      data = response.json()
      for info in data["restaurants"]:
         for img in info["logo_photos"]:
            st.image(img, 100)
         st.write("Name: " + info["name"])
         st.write("Average rating: " + str(round(info["weighted_rating_value"], 1)))
         st.write("Description: " + info["description"])
         for img in info["food_photos"]:
            st.image(img, 100)
         st.write("Type: " + info["type"].capitalize())
         st.write("Phone number: " + str(info["phone_number"]))
         st.write("Street address: " + info["address"]["street_addr"])
         st.write("City: " + info["address"]["city"])
         st.write("State: " + info["address"]["state"])
         st.write("Zip code: " + info["address"]["zipcode"])
         st.write("Local operational hours:")
         for key, value in info["local_hours"]["operational"].items():
            st.write(key + ": " + value)
         st.write("Delivery hours:")
         for key, value in info["local_hours"]["delivery"].items():
            st.write(key + ": " + value)
         st.write("Pickup hours:")
         for key, value in info["local_hours"]["pickup"].items():
            st.write(key + ": " + value)
         st.write("Cuisines:")
         for key in info["cuisines"]:
            st.write(key)
         if(info["is_open"] == False):
            st.write("Closed at the moment.")
         if(info["is_open"] == True):
            st.write("Open!")
         if(info["offers_first_party_delivery"] == False):
            st.write("Delivery is not handled by " + info["name"])
         if(info["offers_first_party_delivery"] == True):
            st.write("Delivery can be done by " + info["name"])
         if(info["offers_third_party_delivery"] == False):
            st.write("Delivery is not possible through third-party!")
         if(info["offers_first_party_delivery"] == True):
            st.write("Delivery can be done by third-party!")
   
