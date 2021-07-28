# how to store meals in a list
meals = ["yoghurt", "roll", "steak"]

# create an empty dictionary
my_first_dictionary = {}
my_second_empty_dictionary = dict()

# how to store meals as a dictionary with key value pairs
meals = {
    "breakfast": "yoghurt",
    "lunch": "roll",
    "dinner": "steak"
}

# you can store pretty much anything in a dictionary however ridiculous
silly_thing = {
    1 : "3",
    "2" : "1",
    4 : True
}

# access particular elements in a dictionary
print(meals["breakfast"])

# find out if a particular key exists
print("breakfast" in meals)
print("supper" in meals)

# add a new element to a dictionary
meals["supper"] = "pancakes"
print(meals)

# replace existing elements
meals["dinner"] = "pasta"
print(meals)

# remove a particular key value pair
del(meals["breakfast"])
print(meals)

# print list of keys
print(list(meals))

# print view object of keys
print(meals.keys())

# print number of keys
print(len(meals.keys()))

# get values from a dictionary
print(meals.values())


countries = {
    "uk": {
        "capital": "London",
        "population": 1000
    },
    "germany": {
        "capital": "Berlin",
        "population": 5
    }
}

print(countries)

print(countries["germany"]["population"])