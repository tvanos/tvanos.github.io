import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv

#Station_ID_List = ['70472', '70469', '78939', '76825', '70673', '72111', '72106', '72398',
#'74884', '71916', '60210', '75911', '7918', '71439', '102295', '64921', '8372', '72104',
#'163161', '76835', '72102', '71411', '71416', '71419', '96387', '71424', '7917', '71431',
#'10362', '72120', '8362', '76827', '111039', '72295', '72410', '8361', '71339', '8384', 
#'5800', '75528', '72367', '71343', '70712', '70699', '70745', '7320', '60095', '60096',
#'4453', '70715', '71336', '8383', '122868', '71346', '8385', '71332', '71334', '60094'
#'8386', '8366', '60097']



f_new = open(r'D:\Web_Crawler\SC_Stations.txt', 'r')
#f_new = open(r'D:\Web_Crawler\NF_Stations.txt', 'r')
#f_new = open(r'D:\Web_Crawler\NOTL_Stations.txt', 'r')

Station_List = []
for eachline in f_new: 
	
	Station_List.append(eachline)
	
Station_List = map(str.strip, Station_List)	

for each in Station_List: 
	each = "http://www.ontariogasprices.com/Pioneer_Gas_Stations/St_Catharines/" + each + "/index.aspx"
	print each 
	r = requests.get(each) 


print Station_List
	