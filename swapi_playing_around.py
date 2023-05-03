import json
from pprint import pp
import requests 

# response= requests.get("https://swapi.dev/api/")
# todos= json.loads(response.text) # load = deserialize json data from a file;  loads = deserialize json data from a python string
# pp(todos)

# starships = requests.get("https://swapi.dev/api/starships")
# todo1 = json.loads(starships.text)
# pp(todo1)

url='https://swapi.dev/api/planets/?page=1'
lst = []
while url is not None:
    response = requests.get(url)
    todos = json.loads(response.text)
    # pp(todos)
    for i in todos['results']:
        lst.append(i['name']) 
    url= todos['next']

print(lst)

    # for item in lst:
    #     resp = requests.get(item)
    #     data=json.loads(resp.text)
    #     print(data)


# ###

# url='https://swapi.dev/api/planets/?page=1'
# lst=[]
# while url is not None:
#     response = requests.get(url)
#     todos=json.loads(response.text)
#     #pprint(todos)
#     for i in todos['results']:
#         lst.append(i['name'])
#     url=todos['next']

# print(lst)

# ###



