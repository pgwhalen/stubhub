# outside
import requests
from pymongo import MongoClient
import json
from datetime import datetime

# me
import configs


### Grab it
api_url = 'https://api.stubhub.com'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + configs.app_token}

event_id = 9156760

full_url = api_url + '/search/inventory/v1'

query = {'eventId': event_id}

r = requests.get(full_url, params=query, headers=headers)

print "STATUS: " + str(r.status_code)
print r.json()
event_listings = r.json()

print len(event_listings['listing'])

now = datetime.today()
listings_to_add = []
for l in event_listings['listing']:
	listing = {
			   "eventId": event_listings["eventId"],
			   "datetime": now,

			   "seatNumbers": l['seatNumbers'],
			   "currentPrice": l['currentPrice']['amount'],
			   "listingId": l["listingId"],
			   "sectionId": l["sectionId"],
			   "sectionName": l["sectionName"],
			   "sellerSectionName": ["sellerSectionName"],
			   "zoneId": l["zoneId"],
			   "zoneName": l["zoneName"],
			   "row": l["row"],
			   "seatNumbers": l["seatNumbers"],
			   "quantity": l["quantity"]
			   }

	listings_to_add.append(listing)


### Store it
c = MongoClient(configs.mongo_conn)
db = c.stubhub
events = db.events
listings = db.listings

listings.insert(listings_to_add)


### Get it
# listings = events.find_one()['listing']