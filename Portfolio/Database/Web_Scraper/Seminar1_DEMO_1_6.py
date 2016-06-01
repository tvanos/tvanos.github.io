DEMO 1

import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv

r = requests.get("http://www.ontariogasprices.com/GasPriceSearch.aspx?fuel=A&typ=adv&srch=0&area=St%20Catharines&site=Ontario&tme_limit=50") 
	
soup = BeautifulSoup(r.content) # soup is just a variable BeautifulSoup reccomends 

links = soup.find_all("a")

for link in links:
		print "<a href='%s'><%s</a>" %(link.get("href"), link.text)

DEMO 2 

for link in links: 
	if "http" in link.get("href"):
		print "<a href='%s'><%s</a>" %(link.get("href"), link.text)
		

DEMO 3 

Gas_Data = soup.find_all("div", {"id": "pp_table"})
print Gas_Data

for item in Gas_Data: 
	print item.text
	
	
DEMO 4 
Gas_Data = soup.find_all("div", {"id": "pp_table"})
for item in Gas_Data: 
	print item.contents # content is then a list 


Gas_Data = soup.find_all("div", {"id": "pp_table"})
for item in Gas_Data:
	Gas_Price = soup.find_all("div", {"class": "sp_p"})
	print item
	
Gas_Prices = soup.find_all("div", {"class": "sp_p"})
for item in Gas_Prices:
	print item.contents  


DEMO 5 

Gas_Price_List = []
Gas_Prices = soup.find_all("div", {"class": "sp_p"})
for item in Gas_Prices:
	print item
	Gas_Price_List.append(item)

print Gas_Price_List

DEMO 6

Gas_Price_List = []
Gas_Prices = soup.find_all("div", {"class": "sp_p"})
for item in Gas_Prices:
	print item
	Gas_Price_List.append(item)

Gas_Price_List_Final = []
pattern = (r'\d+')
for item in Gas_Prices:


Gas_Price_List = []
pattern = (r'\d+')
Gas_Prices = soup.find_all("div", {"class": "sp_p"})
for item in Gas_Prices:
	item = re.findall(pattern, str(item))
	item.insert(-1, '.') 
	item = ''.join(item)
	Gas_Price_List.append(item);
	
	
for item in Gas_Price_List: 
	item = item.join
	print item
	
print Gas_Price_List	
print Gas_Price_List_Final.append(pattern.findall(item)) for item in Gas_Price_List

print Gas_Price_List_Final

