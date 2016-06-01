import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv
## MUST REMOVE SQUARE BRACKETS IN TEXT FILE



f_SC_new = open(r'D:\Web_Crawler\f_SC_new.txt', 'r')
f_NF_new = open(r'D:\Web_Crawler\f_NF_new.txt', 'r')
f_NOTL_new = open(r'D:\Web_Crawler\f_NOTL_new.txt', 'r')

SC_Stations = open(r'D:\Web_Crawler\SC_Stations.txt', 'w')
NF_Stations = open(r'D:\Web_Crawler\NF_Stations.txt', 'w')
NOTL_Stations = open(r'D:\Web_Crawler\NOTL_Stations.txt', 'w')

#--------------------------------------------------------------------------------
SC_Station_List = []
for eachline in f_SC_new: 
	SC_Station_List.append(eachline)

	SC_Station_List = map(str.strip, SC_Station_List)	

for eachline in SC_Station_List: 
	#eachline = int(eachline) 
	SC_Stations.write("%s\n" % eachline)
print SC_Station_List


#--------------------------------------------------------------------------------

NF_Station_List = []
for eachline in f_NF_new: 
	NF_Station_List.append(eachline)
	
NF_Station_List = map(str.strip, NF_Station_List)	

for eachline in NF_Station_List: 
	#eachline = int(eachline) 	
	NF_Stations.write("%s\n" % eachline)
print NF_Station_List

#--------------------------------------------------------------------------------

NOTL_Station_List = []
for eachline in f_NOTL_new: 
	NOTL_Station_List.append(eachline)
NOTL_Station_List = map(str.strip, NOTL_Station_List)	

for eachline in NOTL_Station_List: 
	#eachline = int(eachline) 
	NOTL_Stations.write("%s\n" % eachline)
print NOTL_Station_List


f_SC_new.close()
f_NF_new.close()
f_NOTL_new.close() 

SC_Stations.close()
NF_Stations.close()
NOTL_Stations.close()

