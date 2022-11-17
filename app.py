#Somanath Dandibhotla, Rohit Barua, Faisal Alkaabi
import streamlit as st
import requests
import json
import time
from datetime import date, datetime
import subprocess
import os
import sys
import yaml
import calendar
import random
from numpy.random import choice
from PIL import Image 

st.set_page_config(page_title="I'm[Balanced] = '30/70';",page_icon = ":pizza:", layout= "wide", initial_sidebar_state="collapsed")
#st.header("I'm[Balanced] = '30/70';")
st.markdown('<p class="big-font"><b>I\'m<span style="font-family:Courier New; color:White; font-size: 40px;">[</span>Balanced<span style="font-family:Courier New; color:White; font-size: 40px;">]</span></b><span class="small-font"><b><span style="font-family:Courier New; color:White; font-size: 20px;">=</span> \'30/70\'<span style="font-family:Courier New; color:White; font-size: 20px;">;</span></b></span></p>', unsafe_allow_html=True)
st.markdown("""<style>.big-font {font-family:Courier New; color:White; font-size:40px !important;}</style>""", unsafe_allow_html=True)
st.markdown("""<style>.small-font {font-family:Courier New; color:White;font-size:20px !important;}</style>""", unsafe_allow_html=True)

 

tab1, tab2, tab3, tab4 = st.tabs(["Meal Finder", "Groceries", "Weight Tracker", "Find Restaurants"])

hide_menu_style = """
         <style>
         
         footer {visibility: hidden; }
         </style>
         """
st.markdown(hide_menu_style, unsafe_allow_html=True)


with tab1:
   st.header("Meal Finder")
   st.image("https://media.cnn.com/api/v1/images/stellar/prod/201222103421-healthyfactor-meals.jpg",width=400)
   mealType = st.text_input("Meal Type:");
   if mealType:
      st.success('You chose '+mealType,icon="✅")
      #st.write('Input the macros of the ',mealType)
   calories=st.slider('Calories',50, 800, None,5)
   maxProtein= st.slider('Maximum Protein',5,100,None,1,)
   maxCarbs= st.slider('Maximum Carbs',5,100,None,1,)
   maxFat= st.slider('Maximum Fat',1,100,None,1,)

   if st.button('Find Meal'):
      url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search"

      querystring = {"query":mealType,"offset":"0","number":"5","minCalories":0,"maxCalories":calories,"minProtein":0,"maxProtein":maxProtein,"minFat":0,"maxFat":maxFat,"minCarbs":0,"maxCarbs":maxCarbs}

      headers = {
            "X-RapidAPI-Key": "442463fda5msh2003056aa2a46ebp1d1738jsn41994962d005",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

      response = requests.request("GET", url, headers=headers, params=querystring)

      result = response.json()

      url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/"

      


      for i in result["menuItems"]:
         st.image(i["image"], caption=i["title"]+"\nRestaurant: "+i["restaurantChain"],width=200)
         response2 = requests.request("GET", url2+str(i["id"]), headers=headers)
         result2 = response2.json()
         #st.write(result2)
         st.caption("Calories: "+str(result2["nutrition"]["calories"]))
         st.caption("Protein: "+str(result2["nutrition"]["protein"]))
         st.caption("Carbs: "+str(result2["nutrition"]["carbs"]))
         st.caption("Fat: "+str(result2["nutrition"]["fat"]))
         st.write("\n")


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

      querystring = {"query":itemName,"maxCalories":itemCalories,"minProtein":"0","maxProtein":itemProteins,"minFat":"0","maxFat":itemFats,"minCarbs":"0","maxCarbs":itemCarbs,"minCalories":"0","offset":"0","number":"5"}

      headers = {
         "X-RapidAPI-Key": "442463fda5msh2003056aa2a46ebp1d1738jsn41994962d005",
         "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
      }

      response = requests.request("GET", url, headers=headers, params=querystring)

      result = response.json()

      url2 = url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/"

      for i in result["products"]:
         st.image(i["image"], caption=i["title"],width=250)
         response2 = requests.request("GET", url2+str(i["id"]), headers=headers)
         result2 = response2.json()
         st.caption("Calories: "+str(result2["nutrition"]["calories"]))
         st.caption("Protein: "+str(result2["nutrition"]["protein"]))
         st.caption("Carbs: "+str(result2["nutrition"]["carbs"]))
         st.caption("Fat: "+str(result2["nutrition"]["fat"]))
         st.write("\n")




with tab3:
   st.header("Weight Tracker")
   col1, col2, col3 = st.columns(3)
   col2.write("\n")
   col2.image("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bench-press-spot-1571829590.jpg?resize=980:*",caption="Weight Tracking is important when it comes to growing muscle because it has been proven that increasing the weight you lift on a personalized schedule everytime you train a specific muscle, leads to fast muscle gains.", width=400)
   col2.write("\n")
   col2.image("https://regymenfitness.com/wp-content/uploads/2021/12/Sportive-serious-people-liftin-980x654.jpg",caption="This function focuses on training 13 muscle groups, and includes 75 in-built exercises to choose from. Feel free to add your own custom exercise and weekly routine! (an average of 5 popular exercises included for each muscle group).", width=400)
   col2.write("\n")
   col2.image("https://content.active.com/Assets/Active.com+Content+Site+Digital+Assets/Fitness/Articles/10+Weightlifting+Exercises+for+Beginners/weightlifting-exercises-for-beginners-carousel.jpg",caption="The weight training tracker will suggest weights to lift based on a certain formula that is suggested by professional trainers to help you increase your ability each time you train a certain muscle.", width=400)
   
   if col2.button("Run Python Code"):
      subprocess.run([f"{sys.executable}", "fitness_planner.py"])
   
with tab4:
   source = "Source: Freepik"
   col1, col3, col2 = st.columns((5,1,5))

   with st.sidebar:
      st.title("Pick a type of cuisine")
      cuisine = st.radio(label = "Cuisine Type", options = ['American', 'Chinese', 'Indian', 'Italian', 'Japanese', 'Mexican'], help = "Select a cuisine out of **6** choices")
      st.header("Pick your restaurant(s) attributes")
      budget = st.number_input(
         "Budget",
         help = "Enter a budget by **typing** or using the **buttons** on the right (USD)"
      )
      distance = st.selectbox(
         "Distance limit",
         ('1', '2', '3'),
         help = "Select a distance limit out of **3** choices (miles)"
      )
      rating = st.number_input(
         "Minimum rating",
         help = "Enter a rating by **typing** or using the **buttons** on the right",
         max_value= 5.00
      )
      name = ""
      st.header("Optional")
      name = st.text_input(
         "Restaurant name",
         placeholder = "Enter a restaurant name",
         help = "Enter a restaurant name by typing on the field below"
      )

      button = st.button('Find Restaurant')

   if not button:
      with col1:
         st.subheader("American cuisine")
         st.image("https://img.freepik.com/free-photo/still-life-delicious-american-hamburger_23-2149637291.jpg?w=1480&t=st=1668638075~exp=1668638675~hmac=edf0afa2de94963930e5f67270710b13fb5a6e5e8fbd8da607fe8fef1c61f0e0",
            caption= source
         )
         st.write(
            '''
            **Description:** American cuisine consists of the cooking style and traditional dishes in the United States
            It has been significantly influenced by Europeans, indigenous Native Americans, Africans, Asians, Pacific Islanders,
            and many more cultures and traditions. Principal influences on American cuisine are Native American, British, Jewish,
            German, Spanish, West African, Greek and Italian cuisines. While some of American cuisine is fusion cuisine, many regions
            in the United States have a specific regional cuisine (Wikipedia).
            '''
         )
         st.subheader("Indian cuisine")
         st.image("https://img.freepik.com/free-photo/indian-butter-chicken-black-bowl-wooden-table_123827-20633.jpg?w=1480&t=st=1668652473~exp=1668653073~hmac=7cfea617d56db5c38b3412ebf51c7677aa94672bd1031517552342775ced7fb2",
            caption= source
         )
         st.write(
            '''
            **Description:** Indian cuisine consists of a variety of regional and traditional cuisines native to India. Given
            the diversity in soil, climate, culture, ethnic groups, and occupations, these cuisines vary substantially and use
            locally available spices, herbs, vegetables, and fruits. The Columbian discovery of the New World brought a number
            of new vegetables and fruit to India. A number of these such as potatoes, tomatoes, chillies, peanuts, and guava have become
            staples in many regions of India (Wikipedia).
            '''
         )
         st.subheader("Japanese cuisine")
         st.image("https://img.freepik.com/free-photo/japanese-seafood-ramen-with-cuttlefish-sauce_1205-11088.jpg?w=1480&t=st=1668653071~exp=1668653671~hmac=abceb4a7186938806416fb6b2f012e8404dadb01139a19b25ac26af9c6140b01",
            caption= source
         )
         st.write(
            '''
            **Description:** encompasses the regional and traditional foods of Japan, which have developed through centuries of political,
            economic, and social changes. The traditional cuisine of Japan is based on rice with miso soup and other dishes; there is an
            emphasis on seasonal ingredients. Side dishes often consist of fish, pickled vegetables, and vegetables cooked in broth. Seafood
            is common, often grilled, but also served raw as sashimi or in sushi. Seafood and vegetables are also deep-fried in a light batter,
            as tempura. Apart from rice, a staple includes noodles, such as soba and udon (Wikipedia).
            '''
         )

      with col2:
         st.subheader("Chinese cuisine")
         st.image("https://img.freepik.com/free-photo/top-view-closeup-plates-chinese-foods-white-table_181624-48736.jpg?w=1480&t=st=1668650166~exp=1668650766~hmac=cef76c5a8057d77837aeae44a01744aecf792dc4044ef8bb3edf78653fa218e8",
            caption= source,
         )
         st.write(
            '''
            **Description:** Chinese cuisine encompasses the numerous cuisines originating from China, as well as overseas cuisines
            created by the Chinese diaspora. Because of the Chinese diaspora and historical power of the country, Chinese cuisine
            has influenced many other cuisines in Asia and beyond, with modifications made to cater to local palates.
            Chinese food staples such as rice, soy sauce, noodles, tea, chili oil, and tofu, and utensils such as chopsticks
            and the wok, can now be found worldwide (Wikipedia).
            '''
         )
         st.subheader("Italian cuisine")
         st.image("https://img.freepik.com/free-photo/tasty-appetizing-classic-italian-spaghetti-pasta-with-tomato-sauce-cheese-parmesan-basil-plate-ingredients-cooking-pasta-dark-table-flat-lay-top-view-copy-spce_1150-45812.jpg?w=1480&t=st=1668648377~exp=1668648977~hmac=ce7dab7d13ef19a9a5263aa0d7397b53682f775914c7349a94ce3554b443b1b0",
            caption= source,
         )
         st.write(
            '''
            **Description:** Italian cuisine is a Mediterranean cuisine consisting of the ingredients, recipes, and cooking
            techniques developed across the Italian Peninsula since antiquity, and later spread around the world together
            with waves of Italian diaspora. Significant changes occurred with the colonization of the Americas and the
            introduction of potatoes, tomatoes, capsicums, maize and sugar beet -- the latter introduced in quantity in
            the 18th century. It is one of the best-known and most appreciated gastronomies worldwide (Wikipedia).
            '''
         )
         st.subheader("Mexican cuisine")
         st.image("https://img.freepik.com/free-photo/traditional-mexican-delicious-dish-front-view_23-2148224145.jpg?w=1480&t=st=1668654960~exp=1668655560~hmac=6a57ee7061cdefd65bcf00248c6eb8fb74d9f8c1587fd8f28b4d856d7cd06331",
            caption= source,
         )
         st.write(
            '''
            **Description:** Mexican cuisine consists of the cooking cuisines and traditions of the modern country of Mexico.
            Its earliest roots lie in Mesoamerican cuisine. Today's food staples are native to the land and include corn (maize), 
            beans, squash, amaranth, chia, avocados, tomatoes, tomatillos, cacao, vanilla, agave, turkey, spirulina, sweet potato, 
            catcus, and chili pepper. Its history over the centuries has resulted in regional cuisines based on local conditions, 
            including Bada Med, Chiapas, Veracruz, Oaxacan, and the American cuisines of New Mexican and Tex-Mex (Wikipedia).
            '''
         )

   if button:
      with st.spinner("Loading..."):
        time.sleep(5)
      url = "https://api.spoonacular.com/food/restaurants/search?apiKey=e3204cea803349a783d0c7a7f379c3c1"
      querystring = {"query": name, "lat": 38.835268, "lng": -77.309476,
      "distance": int(distance), "budget": int(budget), "cuisine": cuisine, "min-rating": float(rating),
      "sort": "", "page": 0}

      headers = {
         "X-RapidAPI-Key": "e3204cea803349a783d0c7a7f379c3c1",
         "X-RapidAPI-Host": "https://api.spoonacular.com"
      }
      response = requests.request("GET", url, headers=headers, params=querystring)
      data = response.json()
      st.markdown(
         """
         <style>
         .container {
            display: flex;
         }
         .logo-text {
            font-weight: 100 !important;
            font-size: 25px !important;
            color: #ffffff !important;
            padding-top: 85px !important;
            padding-left: 35px !important;
         }
         .logo-img {
            float: left;
            padding-top: 75px !important;
            width: 50%;
         }
         </style>
         """,
         unsafe_allow_html=True
      )
      st.title("Restaurants")
      for info in data["restaurants"]:
         if(info["is_open"] == False):
            status = "Closed"
         if(info["is_open"] == True):
            status = "Open"
         for img in info["logo_photos"]:
            st.markdown(
               f"""
               <div class= "container">
                  <img class= "logo-img" src= {img}>
                  <p class= "logo-text"> Name: {info["name"]}<br><br>
                     Type: {(info["type"].capitalize())}<br><br>
                     Currently: {status}<br><br>
                     Average rating: {round(info["weighted_rating_value"], 1)}<br><br>
                     Phone number: {info["phone_number"]}<br><br>
                     Street address: {info["address"]["street_addr"]}
                  </p>
               </div>
               """,
               unsafe_allow_html=True
            )
      st.write("-----------------------------------------------------------")
      st.success("Done!")
