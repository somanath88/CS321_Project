#This file is used for testing api calls.


#the following are some tests for Meal Finder

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search"

test1 = {"query":"burger","offset":"0","number":"1","minCalories":0,"maxCalories":200,"minProtein":0,"maxProtein":20,"minFat":0,"maxFat":20,"minCarbs":0,"maxCarbs":20}

test2 = {"query":"pasta","offset":"0","number":"1","minCalories":0,"maxCalories":800,"minProtein":0,"maxProtein":11,"minFat":0,"maxFat":2,"minCarbs":0,"maxCarbs":12}

test3 = {"query":"pizza","offset":"0","number":"1","minCalories":0,"maxCalories":300,"minProtein":0,"maxProtein":10,"minFat":0,"maxFat":3,"minCarbs":0,"maxCarbs":10}

test4 = {"query":"sushi","offset":"0","number":"1","minCalories":0,"maxCalories":400,"minProtein":0,"maxProtein":20,"minFat":0,"maxFat":20,"minCarbs":0,"maxCarbs":16}

test5 = {"query":"sandwitch","offset":"0","number":"1","minCalories":0,"maxCalories":700,"minProtein":0,"maxProtein":14,"minFat":0,"maxFat":12,"minCarbs":0,"maxCarbs":19}

headers = {
            "X-RapidAPI-Key": "Insert Key Here",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

response1 = requests.request("GET", url, headers=headers, params=test1)

response2 = requests.request("GET", url, headers=headers, params=test2)

response3 = requests.request("GET", url, headers=headers, params=test3)

response4 = requests.request("GET", url, headers=headers, params=test4)

response5 = requests.request("GET", url, headers=headers, params=test5)

result1 = response1.json()

result2 = response2.json()

result3 = response3.json()

result4 = response4.json()

result5 = response5.json()

#checking the restults

print("The following results are from MEAL FINDER TESTS")
for i in result1["menuItems"]:
	print(i)

for i in result2["menuItems"]:
	print(i)

for i in result3["menuItems"]:
	print(i)

for i in result4["menuItems"]:
	print(i)

for i in result5["menuItems"]:
	print(i)



print("\n\n\n")


#the following are some tests for Groceries Finder

itemTest1 = {"query":"yogurt","maxCalories":150,"minProtein":"0","maxProtein":10,"minFat":"0","maxFat":11,"minCarbs":"0","maxCarbs":14,"minCalories":"0","offset":"0","number":"5"}

itemTest2 = {"query":"peanut","maxCalories":200,"minProtein":"0","maxProtein":12,"minFat":"0","maxFat":4,"minCarbs":"0","maxCarbs":8,"minCalories":"0","offset":"0","number":"5"}

itemTest3= {"query":"cerial","maxCalories":300,"minProtein":"0","maxProtein":15,"minFat":"0","maxFat":7,"minCarbs":"0","maxCarbs":25,"minCalories":"0","offset":"0","number":"5"}

itemTest4= {"query":"oats","maxCalories":110,"minProtein":"0","maxProtein":7,"minFat":"0","maxFat":9,"minCarbs":"0","maxCarbs":30,"minCalories":"0","offset":"0","number":"5"}

itemTest5= {"query":"cheese","maxCalories":80,"minProtein":"0","maxProtein":10,"minFat":"0","maxFat":11,"minCarbs":"0","maxCarbs":7,"minCalories":"0","offset":"0","number":"5"}

headers = {
         "X-RapidAPI-Key": "Insert Key Here",
         "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
      }


response1 = requests.request("GET", url, headers=headers, params=itemTest1)

response2 = requests.request("GET", url, headers=headers, params=itemTest2)

response3 = requests.request("GET", url, headers=headers, params=itemTest3)

response4 = requests.request("GET", url, headers=headers, params=itemTest4)

response5 = requests.request("GET", url, headers=headers, params=itemTest5)

result1 = response1.json()

result2 = response2.json()

result3 = response3.json()

result4 = response4.json()

result5 = response5.json()

#checking the restults

print("The following results are from Grocery Finder TESTS")
for i in result1["products"]:
	print(i)

for i in result2["products"]:
	print(i)

for i in result3["products"]:
	print(i)

for i in result4["products"]:
	print(i)

for i in result5["products"]:
	print(i)


