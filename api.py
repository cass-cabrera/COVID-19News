import requests, json

#uses covid-19 api to grab possible countries for data
def getKeys():
	endpoint = 'https://api.quarantine.country/'
	try: 
		r= requests.get(endpoint)
		data = r.json()
		options = list(data['regions'].keys())
		options.sort()
		return options
	except:
		return []

#gathers covid-19 statistics based on country 
def getStat(country):
	param = {"region":country}
	endpoint = 'https://api.quarantine.country/api/v1/summary/region'
	try:
		r = requests.get(endpoint, params=param)
		data = r.json()
		return data
	except:
		return []

#gathers the worldwide summary of covid-19 data
def getWorld():
	endpoint = 'https://api.quarantine.country/'
	try: 
		r= requests.get(endpoint)
		data = r.json()
		return data
	except:
		return []