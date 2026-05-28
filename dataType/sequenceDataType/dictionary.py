"""Dictionary : collection of data items(data structure) that key-value pair, mutable,order(version 3.7),
don't allow duplicate value"""
# a = {
#     "name":"sujan", #we can use input
#     "age" : 99,
#     "address ":"lalitpur"
# }
# print(len(a))
# b = dict(name = "sujan", age =23)
# print(b)
# print(a["name"])
# print(a.get("add","data is not found")) #--> it give output without any error , we used most
#valu can be multiple but not key 
# print(a.keys()) #-->it show only key 
# print(a.values()) #-->it show only values
# print(a.items()) #-->it shows both key and values
# a["email"] = "sujan@gmail.com"
# a["name"] ="sujan dai"
# print(a)
# b = {
#     "age":23,
#     "mail":"sujanlama@gmail.com"
# }
# a.update(b)
# print(a)
# a.pop("name") #--> give 
# print(a)
# a.popitem() -->last item deletion
# print(a)
# del a["name"]
# print(a)
# a.clear()
# a.setdefault("mail","sujan@gmail.com") #

# print(a)
# b= ["ram","hari","shyam"]
# c = dict.fromkeys(b,"present")
# c["ram"] ="absent"
# print(c)

#nested dictionary
# b = {
#    "roll no 1":{
#        "name :":"sujan",
#        "age" :23
#    },
   
#    "roll no 2":{
#        "name": "anjan",
#        "age":22
#    }
# }
# c= b["roll no 1"]["name"]= "sujan lama"
# print(c)

"""Build a simple English-to-Nepali translation program using a Python dictionary. Your program should:
•⁠  ⁠Contain at least 10 English words and their Nepali translations.
•⁠  ⁠Ask the user to enter an English word.
•⁠  ⁠Display the Nepali translation if the word exists in the dictionary.
•⁠  ⁠Print a friendly "Word not found" message if the word is not in the dictionary.
•⁠  ⁠Allow the user to keep searching until they choose to quit (use a loop)"""
#code
# val ={
#     "mother":"आमा",
#     "father":"बुबा",
#     "love":"माया",
#     "text":"पाठ",
#     "school":"विद्यालय"
# }

# user_input = input("Enter word you want to translate:")
# # print("Translate :",val.get(user_input,"word is not found"))
# print(f'{val.get(user_input,"word is not found !!")}')

#You are given the nested dictionary below
# my_details = {
#   'name': 'sujan',
#   'grade': 0,
#   'address': 'ktm',
  
# 'hobbies': {
#     'sports': 'running',
#     'game': 'pubg',
#     'novel': 'xyz',
#     'anime': 'one piece',
# },

# 'email': 'sujan@gmail.com'
# }

# d = my_details["hobbies"]["novel"] ="Harry Potter"
# print(f"updated : {d}")

# data = {
#   "coord": {
#     "lon": 10.99,
#     "lat": 44.34
#   },
#   "weather": [
#     {
#       "id": 501,
#       "main": "Rain",
#       "description": "moderate rain",
#       "icon": "10d"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 298.48,
#     "feels_like": 298.74,
#   },
#   "visibility": 10000,
#   "wind": {
#     "speed": 0.62,
#     "deg": 349,
#     "gust": 1.18
#   }
# }

# print(data["weather"])

# detail = {
#     'name':'sujan'
    
# }
# detail['age'] =23
# detail['name']='hari'
# print(detail)

# a=['sujan','rohan']
# b =dict.fromkeys(a,'present')
# b['sujan'] ='absent'
# print(b)