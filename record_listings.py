# outside
import requests
from pymongo import MongoClient
import json
from datetime import datetime

# me
import configs
import stubhub_api

stubhub = MongoClient(configs.mongo_conn).stubhub
events = stubhub.events
listings = stubhub.listings
now = datetime.today()

def get_events_to_track():
	event_ids = []
	for e in events.find():
		if (e['id']):
			event_ids.append(e['id'])
	return event_ids

def record_listings_for_event(event_id):
	event_listings = stubhub_api.get_listings_for_event(event_id)
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
	print "Found " + str(len(listings_to_add)) + " to add for " + str(event_id)

	listings.insert(listings_to_add)

if __name__ == "__main__":
	event_ids = get_events_to_track()

	for event_id in event_ids:
		record_listings_for_event(event_id)
	
	print "Done recording listings for " + str(len(event_ids)) + " events"