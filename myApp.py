import requests
import json

URL="http://127.0.0.1:8000/studentApi"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    if r.content:
        data = r.json()
        print(data)
    else:
        print("Empty response received from the API")

# get_data()

def post_data():
    data = {
        'roll': 104,
        'name': 'Rj',
        'city': 'Dhaka'
    }

    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    print(response.json())

post_data()
    
def cmplt_update_data():
    data = {
        'id': 1,
        'roll': 103,
        'name': 'Rijbi',
        'city': 'Dhaka'
    }

    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    print(response.json())

# cmplt_update_data()

def prtl_update_data():
    data = {
        'id': 2,
        'name': 'Rahat',
        'city': 'Dhaka'
    }

    json_data = json.dumps(data)
    response = requests.patch(url=URL, data=json_data)
    print(response.json())

# prtl_update_data()
    
def delete_data():
    data={'id':1}
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data=json_data)
    print(res.json())

# delete_data()