import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv


f_SC = open(r'D:\Web_Crawler\f_SC.txt', 'r')
f_NF = open(r'D:\Web_Crawler\f_NF.txt', 'r')
f_NOTL = open(r'D:\Web_Crawler\F_NOTL.txt', 'r')

f_SC_new = open(r'D:\Web_Crawler\f_SC_new.txt', 'w')
f_NF_new = open(r'D:\Web_Crawler\f_NF_new.txt', 'w')
f_NOTL_new = open(r'D:\Web_Crawler\f_NOTL_new.txt', 'w')

#pattern = (r'\d+')
#for eachline in f: 
#	print eachline
	#eachline = re.findall(pattern, str(eachline))
	
	#f.write('\n' & eachline)
	


pattern = (r'\d+')
for eachline in f_SC: 
	eachline = re.findall(pattern, str(eachline))
	print eachline
	if eachline != []:
		f_SC_new.write('\n')
		f_SC_new.write(str(eachline))
	
	
pattern = (r'\d+')
for eachline in f_NF: 
	eachline = re.findall(pattern, str(eachline))
	print eachline
	if eachline != []:
		f_NF_new.write('\n')
		f_NF_new.write(str(eachline))
		
pattern = (r'\d+')
for eachline in f_NOTL: 
	eachline = re.findall(pattern, str(eachline))
	print eachline
	if eachline != []:
		f_NOTL_new.write('\n')
		f_NOTL_new.write(str(eachline))
				
f_SC.close()
f_NF.close()
f_NOTL.close()
f_SC_new.close()
f_NF_new.close()
f_NOTL_new.close()