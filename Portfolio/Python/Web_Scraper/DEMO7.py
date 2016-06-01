import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv


#filename = os.path.join( "D:", "Web_Crawler")

#if os.path.exists(r'D:\Web_Crawler\stationIDs') = False: 
f = open(r'D:\Web_Crawler\RawStationIDs.txt', 'w')
	
All_Stations = ["http://www.ontariogasprices.com/GasPriceSearch.aspx?fuel=A&typ=adv&srch=0&area=St%20Catharines&site=Ontario&tme_limit=50",
"http://www.ontariogasprices.com/GasPriceSearch.aspx?typ=adv&fuel=A&srch=0&area=Niagara+Falls&site=Ontario&tme_limit=50",
"http://www.ontariogasprices.com/GasPriceSearch.aspx?typ=adv&fuel=A&srch=0&area=Niagara-on-the-Lake&site=Ontario&tme_limit=50",]

for item in All_Stations: 
		
	r = requests.get(item);
	soup = BeautifulSoup(r.content);
		
	links = soup.find_all("a");
	for link in links: 
		if "index.asp" in link.get("href"):
			link = "<a href='%s'><%s</a>" %(link.get("href"), link.text)
			print link
			f.write(link)
			f.write('\n')
f.close()

