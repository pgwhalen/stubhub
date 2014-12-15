# outside
import requests
from pymongo import MongoClient
import json

# me
import configs


### Get it
api_url = 'https://api.stubhub.com'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + configs.app_token}

event_id = 9156760

full_url = api_url + '/search/inventory/v1'

query = {'eventId': event_id}

r = requests.get(full_url, params=query, headers=headers)

print "STATUS: " + str(r.status_code)
print r.json()
the_json = r.json()



### Store it
c = MongoClient(configs.mongo_conn)
db = c.stubhub
events = db.events

events.insert(the_json)