from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from flask import Markup


def printh2():

	my_site = 'https://www.readersdigest.ca/health/healthy-living/self-quarantine-activities/'

	req = Request(
		my_site,
		headers={'User-Agent': 'Mozilla/5.0'}
	)

	resp = urlopen(req)
	bs_obj = BeautifulSoup(resp.read(), 'lxml')
	
	data = Markup(bs_obj.find_all('h2'))
	
	return data