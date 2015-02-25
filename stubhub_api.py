import configs
import requests

api_url = 'https://api.stubhub.com'

headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Bearer ' + configs.app_token,
	'Accept': 'application/json',
	'Accept-Encoding': 'application/json'
}

def get_event_info(event_id):
	url = api_url + '/catalog/events/v2/' + str(event_id)
	r = requests.get(url, headers=headers)
	return r.json()

def get_listings_for_event(event_id):
	url = api_url + '/search/inventory/v1'
	query = {'eventId': event_id}
	r = requests.get(url, params=query, headers=headers)
	return r.json()