import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv


#filename = os.path.join( "D:", "Web_Crawler")

#if os.path.exists(r'D:\Web_Crawler\stationIDs') = False: 
f = open(r'D:\Web_Crawler\RawStationIDs.txt', 'r')
f_new = open(r'D:\Web_Crawler\StationIDs.txt', 'w')

#pattern = (r'\d+')
#for eachline in f: 
#	print eachline
	#eachline = re.findall(pattern, str(eachline))
	
	#f.write('\n' & eachline)
	


pattern = (r'\d+')
for eachline in f: 
	eachline = re.findall(pattern, str(eachline))
	print eachline
	if eachline != []:
		f_new.write('\n')
		f_new.write(str(eachline))
	
	

f.close()
f_new.close()