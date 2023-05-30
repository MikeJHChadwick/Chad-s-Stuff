import json
from pprint import pp
import requests 


# url='https://www.themuse.com/api/public/jobs?category=Data%20Science&page='
# lst = []
# lst1 = []
# for i in range(1,100):
#     url = (f'https://www.themuse.com/api/public/jobs?category=Data%20Science&page={i}')
#     response = requests.get(url)
#     todos = json.loads(response.text)
#     # pp(todos)
#     # lst.append(i['name']) 
#     lst.append(todos) 
#     for j in todos:
#         if j['results']:
#             lst1.append(j)
   
#     # url= url+[str(i)]
# # pp(lst)
# pp(lst1)

url = 'https://www.themuse.com/api/public/jobs'
headers = {'Content-type': 'application/json'}
results = []
params = {'category': 'Data and Analytics', 'location': 'Chicago, IL', 'page': '0', 'descending': 'True'}
resp = requests.get(url, params=params, headers=headers).json()

pp(resp)

