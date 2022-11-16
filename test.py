import streamlit as st
import requests
import json
import time
from datetime import date, datetime
import os
import sys
import yaml
import calendar
import random
from numpy.random import choice
from PIL import Image

st.set_page_config(page_title="70%30",page_icon = ":🧊:", layout= "wide")
st.header("70/30 Balance")


 

tab1, tab2, tab3, tab4 = st.tabs(["Meal Finder", "Groceries", "Weight Training Tracker", "Find Restaurants"])

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

      #st.write(result)

      for i in result["menuItems"]:
         st.image(i["image"], caption=i["title"]+"\nRestaurant: "+i["restaurantChain"],width=200)


with tab2:
   st.header("Groceries")
   st.image("https://hips.hearstapps.com/hmg-prod/images/healthy-groceries-1525213305.jpg", width=250)
   itemName = st.text_input("Item's Name:");
   if itemName:
      st.write('Input the macros of ',itemName)
   itemCalories = st.number_input('Calories:', min_value=0, max_value=800, value=50, step=10)
   itemProteins = st.number_input('Protein:', min_value=0, max_value=100, value=0, step=1)
   itemCarbs = st.number_input('Carbs:', min_value=0, max_value=100, value=0, step=1)
   itemFats = st.number_input('Fats:', min_value=0, max_value=100, value=0, step=1)

   if st.button('Find Item'):
      url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/search"

      querystring = {"query":itemName,"maxCalories":itemCalories,"minProtein":"0","maxProtein":itemProteins,"minFat":"0","maxFat":itemFats,"minCarbs":"0","maxCarbs":itemCarbs,"minCalories":"0","offset":"0","number":"10"}

      headers = {
         "X-RapidAPI-Key": "442463fda5msh2003056aa2a46ebp1d1738jsn41994962d005",
         "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
      }

      response = requests.request("GET", url, headers=headers, params=querystring)

      result = response.json()


      for i in result["products"]:
         st.image(i["image"], caption=i["title"],width=250)
         st.write("")




with tab3:
   st.header("Weight Training Planner/Tracker")
   st.image("https://assets.roguefitness.com/f_auto,q_auto,c_limit,w_1536,b_rgb:f8f8f8/catalog/Conditioning/Strength%20Equipment/Dumbbells/IP1100/IP1100-H_ejvjae.png", width=400)

   def load_config(config):
      with open(config + '.yaml', 'r') as f:
         conf = yaml.safe_load(f)
      return conf

   def load_exercise_history():
      try:
         with open('data.json', 'r') as fp:
               data = json.load(fp)
         return data
      except IOError:
         return dict()

   def add_exercise_dictionary(dic, exercise, weight, reps):
      # {"bench press": {today: [{weight: 150, reps: 6}, {weight: 150, reps: 6}, {weight: 150, reps: 6}]}}
      today = str(date.today())
      if dic.get(exercise):
         if dic[exercise].get(today):
               dic[exercise][today] = dic[exercise][today] + [{ 'weight': weight, 'reps': reps}]
         else:
               dic[exercise][today] = [{ 'weight': weight, 'reps': reps}]
      else:
         dic[exercise] = { today: [{ 'weight': weight, 'reps': reps}]}
      return dic

   def save_exercise_history(data):
      with open('data.json', 'w') as fp:
         json.dump(data, fp)

   def extract_int(s):
      return [int(x) for x in s.split() if x.isdigit()][0]

   def convert_weight_string(s):
      """translates input to weight.
      "bar + 65" => 175 (lbs)
      not robust"""
      if "bar" in s:
         plate_weight = extract_int(s.split("bar")[1].split("+")[1]) # prettify
         return 45 + plate_weight * 2
      else:
         return extract_int(s)

   def round_nearest_five(num):
      return int(num//5*5+ (5 if (num%5) >= 2.5 else 0))

   def interact_with_user(exercise, num_sets, warmup=False): #dont need the warmup parameter it seems
      """Displays the current exercise and tracks number of reps performed"""
      exercise = random.choice([x.title().strip() for x in exercise.lstrip('*').lstrip('^').lstrip('=').split('OR')])
      exercise_history = load_exercise_history()

      prev_numbers = []
      if exercise_history.get(exercise):
         last_time = list(exercise_history[exercise].keys())[-1]
         #last_time_dow = calendar.day_name[datetime.strptime('2014-12-04', '%Y-%m-%d').date().weekday()]
         prev_numbers = exercise_history[exercise][last_time]

      #print(f"===== {exercise} =====")
      
      # if warmup:
      if prev_numbers:
         if exercise_history.get(exercise):
               while True:
                  try:
                     checker = 0
                     checker2 = 0
                     trueOrNot1 = 0
                     trueOrNot2 = 0
                     for i in reversed(prev_numbers):
                           checker += 1
                     if checker >= 3: # if there are 3 or more entries made
                           prev_num_str = [x['reps'] + ' lbs for ' + x['weight'] for x in prev_numbers]
                           for x in prev_num_str:
                              abota = x
                           for i in reversed(prev_numbers): # get third weight used back
                              threeBack = int(i["weight"])
                              checker2 += 1
                              if checker2 == 3:
                                 break
                           for i in reversed(prev_numbers): #check first one back
                              if int(i["weight"]) + 2 > threeBack:
                                 trueOrNot1 = 1
                              checker2 = 0
                              checker2 += 1
                              if checker2 == 1:
                                 break
                           for i in reversed(prev_numbers): #check second one back
                              if int(i["weight"]) + 2 > threeBack:
                                 trueOrNot2 = 1
                              checker2 = 0
                              checker2 += 1
                              if checker2 == 2:
                                 break
                           if trueOrNot1 == 1 and trueOrNot2 == 1:
                              inp = input(f"For '{exercise}', you last used {abota} reps on {last_time}.\nSuggestion: Looking at your workout history, per the 2/2 rule, you qualify for increasing your weights by 5-10 pounds. *User discretion is advised.*\nHow much weight(lbs) would you like to lift?: ")
                           else:
                              inp = input(f"For '{exercise}', you last used {abota} reps on {last_time}.\nHow much weight(lbs) would you like to lift ?: ")
                           # inp2 = input("How many reps would you like to do?: ")
                           weight = convert_weight_string(inp)
                           break
                     else: #if there are less than 2 entries made
                           prev_num_str = [x['weight'] + 'lbs for ' + x['reps'] for x in prev_numbers]
                           for x in prev_num_str:
                              abota = x
                           inp = input(f"For '{exercise}', you last used {abota} reps on {last_time}.\nHow much weight(lbs) would you like to lift ?: ")
                           # inp2 = input("How many reps would you like to do?: ")
                           weight = convert_weight_string(inp)
                           break
                  except:
                     print("Invalid input. Please try again.")
                     break
                  break
         else:
               inp = input(f"You have never logged this exercise, '{exercise}'. How much weight would you like to lift (lbs)?: ")
               weight = convert_weight_string(inp)
         # else:
         #     inp = input(f"You have never logged this exercise, '{exercise}'. How much weight would you like to lift (lbs)?: ")
         #     weight = convert_weight_string(inp)
      inp2 = input("How many reps would you like to do?: ")
      # else:
      #     weight = convert_weight_string(prev_numbers[0]["weight"])
      #print("       ( warm up ) ")
      print("")
      print("---- Workout Plan ----")
      
      def warmup_routine(reps, percent, setNumber):
         print(f"(Set {setNumber}) - {reps} reps of {round_nearest_five(weight*percent)} lbs.")
         #countdown_for_rest(rest_min)

      if num_sets == 1:
         for (percent, reps, setNumber) in [(1, int(inp2), 1)]:
               warmup_routine(reps, percent, setNumber)
      elif num_sets == 2:
         for (percent, reps, setNumber) in [(.5, int(inp2), 1), (1, int(0.5 * int(inp2)), 2)]:
               warmup_routine(reps, percent, setNumber)
      elif num_sets == 3:
         for (percent, reps, setNumber) in [(.4, int(0.5 * int(inp2)), 1), (.7, int(0.7 * int(inp2)), 2), (1, int(inp2), 3)]:
               warmup_routine(reps, percent, setNumber)
      elif num_sets == 4:
         for (percent, reps, setNumber) in [(.4, int(0.2 * int(inp2)), 1), (.6, int(0.5 * int(inp2)), 2), (.8, int(0.7 * int(inp2)), 3), (1, int(inp2), 4)]:
               warmup_routine(reps, percent, setNumber)
      elif num_sets == 5:
         for (percent, reps, setNumber) in [(.3, int(0.2 * int(inp2)), 1), (.5, int(0.4 * int(inp2)), 2), (.7,  int(0.6 * int(inp2)), 3), (1, int(0.8 * int(inp2)), 4), (.9, int(inp2), 5)]:
               warmup_routine(reps, percent, setNumber)
      else:
         print("Too many sets. Potentially harmful. Please try again.")
         exit()
               
      
      print("---- Log Your Sets ----")
      for s in range(num_sets): # TODO: handle warmups
         while True:
               try:
                  inp = input("(Set " + str(s+1) + ") - Enter info (weight, reps): ")
                  weight = inp.split(',', 1)[0]
                  reps = inp.split(',',1)[1].strip().replace('.','',1)
                  if reps.strip().replace('.','',1).isdigit():
                     break
                  else:
                     print("Invalid input. Please try again.")
               except:
                  print("Invalid input. Please try again.")

         exercise_history = add_exercise_dictionary(exercise_history, exercise, weight, reps)
         save_exercise_history(exercise_history)
      None

   def shuffle(exercises, count):
      """Apply modifiers and then randomly shuffles list"""
      def build_weights(exercises):
         weights = list(map(lambda x: 0.0 if x.startswith('*') else (1.0 if x.startswith('^') else 0.5), exercises))
         sum_weights = sum(weights)
         weights = list(map(lambda x: x/sum_weights, weights))
         return weights

      top_priority = [x for x in exercises if x.startswith('**')]
      weights = build_weights(exercises)
      # random.choices can result in duplicates
      the_rest = []
      for _ in range(count - len(top_priority)):
         chosen = random.choices(exercises, weights=weights, k=1)[0]
         while chosen in the_rest:
               chosen = random.choices(exercises, weights=weights, k=1)[0]
         the_rest.append(chosen)

      # ensuring = is last exercise performed
      return top_priority + [x for x in the_rest if not x.startswith('=')] + [x for x in the_rest if x.startswith('=')]

   def main():
      exercises = load_config("exercises")
      routine = load_config("routine")

      current_day = calendar.day_name[date.today().weekday()]
      todays_routine = routine.get(current_day, None)

      

      if todays_routine:
         exercisesInMuscleGroup = ""
         for muscle_group in todays_routine:
            exercisesInMuscleGroup += str(muscle_group) + ", "
         st.write("Today is **" + current_day + "** and you will be working on " + exercisesInMuscleGroup + "so have a great workout!")
         count = 0
         count2 = 6
         count3 = 13
         count4 = 19
         checkert = 0
         for muscle_group in todays_routine:
               exercise_set_count = todays_routine[muscle_group]
               muscle_group_exercises = shuffle(exercises[muscle_group], exercise_set_count)

               #Attempt 1
               for i in range(exercise_set_count):
                  # title = st.text_input('Movie title', 'Life of Brian')
                  # st.write('The current movie title is', title)
                  STcheck = st.text_input(f"Would you like to do '{muscle_group_exercises[i].title()}'? (Yes/No): ")
                  st.write(f"{STcheck}")
                  if STcheck.upper() == "no".upper():
                     continue
                  elif STcheck.upper() == "yes".upper():
                     st.write(f"===== {muscle_group_exercises[i].title()} =====")
                  else:
                     print("Invalid input. Please try again.")
                     #continue

                  
                  print(f"===== {muscle_group_exercises[i].title()} =====")
                  try:
                     inp = input(f"How many sets of '{muscle_group_exercises[i].title()}' would you like to do? (max:5): ")
                  except:
                     print("Invalid input. Please try again.")
                  interact_with_user(muscle_group_exercises[i], int(inp), i==0) 

                  
               #Attempt 2
               # for i in range(exercise_set_count):
               #    # if checkert == 1:
               #    #    continue
               #    STcheck = st.selectbox(f"Would you like to do '{muscle_group_exercises[i].title()}'?: ", ('Yes', 'No'), key = count2)
               #    if st.button("Go", key = count, disabled=False):
               #       if STcheck == "Yes":
               #          #st.write('You selected:', STcheck)
               #          count += 1
               #          count2 += 1
               #          #st.write(f"===== {muscle_group_exercises[i].title()} =====")
               #          # try:
               #          inp = st.number_input(f"How many sets of '{muscle_group_exercises[i].title()}' would you like to do? (max:5): ", min_value=1, max_value=5, step=1, key = count3)
               #          if st.button("Go", key = count4, disabled=False):
               #             count4 += 1
               #             st.write("here")
               #             interact_with_user(muscle_group_exercises[i], int(inp), i==0)
               #          count3 += 1
               #          # continue
               #          #inp = input(f"How many sets of '{muscle_group_exercises[i].title()}' would you like to do? (max:5): ")
               #          # except:
               #          #    print("Invalid input. Please try again.")
               #       elif STcheck == "No":
               #          count += 1
               #          count2 += 1
               #          # continue
               #    else:
               #       st.write('You selecteddd:', STcheck)
               #       count += 1
               #       count2 += 1
               #       # st.empty()
               #       checkert = 1
               #       break
               #       #continue
               #    # count += 1
               #    # count2 -= 1
               #    #check = input(f"Would you like to do '{muscle_group_exercises[i].title()}'? (Y/N): ")
               #    # if STcheck == "No":
      else:
         print("It is your Rest Day. See you tomorrow :)")

   if __name__ == '__main__':
      main()


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
         placeholder= "Enter a distance limit",
      )
      rating = st.number_input(
         "Minimum rating",
         help = "Enter a rating by **typing** or using the **buttons** on the right",
         max_value= 5.00
      )
      button = st.button('Find Restaurant')
   if button:
      url = "https://api.spoonacular.com/food/restaurants/search?apiKey=77495ee53c1a4c1a8310504513165f8e"
      querystring = {"query": "", "lat": 38.835268, "lng": -77.309476,
      "distance": int(distance), "budget": int(budget), "cuisine": cuisine, "min-rating": float(rating),
      "sort": "", "page": 0}

      headers = {
         "X-RapidAPI-Key": "77495ee53c1a4c1a8310504513165f8e",
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
