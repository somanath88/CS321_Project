import streamlit as st
import requests
st.set_page_config(page_title="30%70",page_icon = ":🧊:", layout= "wide")
st.header("30/70")


# if st.button('Meal Finder'):
#     st.write(meal_finder)    

tab1, tab2, tab3,tab4 = st.tabs(["Meal Finder", "Groceries", "Weight Tracker","Gym Partner"])

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
    st.header("Gym Partner")
    st.image("https://img.freepik.com/free-photo/people-gym-talking-making-exercise-plans_23-2149175368.jpg",width=400)