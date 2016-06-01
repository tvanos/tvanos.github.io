import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv
import html5lib

r = requests.get("http://www.ontariogasprices.com/Pioneer_Gas_Stations/St_Catharines/70472/index.aspx")
soup = BeautifulSoup(r.content, "html5lib")

content = soup.find_all("dd")

Address_List = []
for item in content: 
	item = item.text
	Address_List.append(item)
	#print each.contents.find_all("d1", {"class": "spa_cont"})
	#print each.contents.find_all("dd").text

Address_List = 	Address_List[:4]
print Address_List