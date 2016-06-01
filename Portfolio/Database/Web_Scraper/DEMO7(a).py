import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv


#filename = os.path.join( "D:", "Web_Crawler")

#if os.path.exists(r'D:\Web_Crawler\stationIDs') = False: 
f_SC = open(r'D:\Web_Crawler\f_SC.txt', 'w')
f_NF = open(r'D:\Web_Crawler\f_NF.txt', 'w')
f_NOTL = open(r'D:\Web_Crawler\F_NOTL.txt', 'w')


St_Catharines_Stations = "http://www.ontariogasprices.com/GasPriceSearch.aspx?fuel=A&typ=adv&srch=0&area=St%20Catharines&site=Ontario&tme_limit=50"
Niagara_Falls_Stations = "http://www.ontariogasprices.com/GasPriceSearch.aspx?typ=adv&fuel=A&srch=0&area=Niagara+Falls&site=Ontario&tme_limit=50"
NOTL_Stations = "http://www.ontariogasprices.com/GasPriceSearch.aspx?typ=adv&fuel=A&srch=0&area=Niagara-on-the-Lake&site=Ontario&tme_limit=50"

r = requests.get(St_Catharines_Stations);
soup = BeautifulSoup(r.content);
		
links = soup.find_all("a");
for link in links: 
	if "index.asp" in link.get("href"):
		link = "<a href='%s'><%s</a>" %(link.get("href"), link.text)
		print link
		f_SC.write(link)
		f_SC.write('\n')
f_SC.close()

r = requests.get(Niagara_Falls_Stations);
soup = BeautifulSoup(r.content);
		
links = soup.find_all("a");
for link in links: 
	if "index.asp" in link.get("href"):
		link = "<a href='%s'><%s</a>" %(link.get("href"), link.text)
		print link
		f_NF.write(link)
		f_NF.write('\n')
f_NF.close()

r = requests.get(NOTL_Stations);
soup = BeautifulSoup(r.content);
		
links = soup.find_all("a");
for link in links: 
	if "index.asp" in link.get("href"):
		link = "<a href='%s'><%s</a>" %(link.get("href"), link.text)
		print link
		f_NOTL.write(link)
		f_NOTL.write('\n')
f_NOTL.close()