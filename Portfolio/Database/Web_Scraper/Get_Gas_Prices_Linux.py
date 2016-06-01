#!/usr/bin/env python
"""
DESCRIPTION

    This is a webcrawler/scraper for harvesting OntarioGasPrices.com for all gas prices and station information
	The Script requires the porper path to the all_stations.txt file  
	
AUTHOR

    Travis Vanos <Travis.vanos@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.
	The script is for EDUCATIONAL PURPOSES ONLY 

VERSION

	Version: 1.1
"""

import sys, os, traceback, optparse
import time
import re
import requests 
from bs4 import BeautifulSoup
import csv
import html5lib
import datetime
from time import strftime
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders



#CREATES TIMESTAMP FOR FILE CREATION 
Time_Stamp = strftime("%Y-%m-%d")
now = datetime.datetime.now()

print os.getcwd()

dir = os.path.dirname(__file__)

filename = os.path.join(dir, 'Prices')

if not os.path.exists(filename):
    os.makedirs(filename)
	
#CREATES FILE IF NOT ALREADY PRESENT 
f = filename + Time_Stamp + r'.csv'
Gas_Price_CSV = open(f,'w')
Gas_Price_CSV.close()


#OPEN NEWLY CREATED FILE FOR WRITING
Gas_Price_CSV = open(f,'wb')

#READS WEBSITE URL's FROM All-Station.txt 
All_Stations = open(filename + r'/All_Stations.txt', 'r')

#WRITES COLUMN HEADERS FOR CSV FILE
Collected_Data = ["Gas Station Name", "Address", "Street Corner", "City and Postal Code", "Phone Number", "Regular", "MidGrade", "Premium", "Diesel", "Date Collected"]
wr = csv.writer(Gas_Price_CSV, dialect='excel')
wr.writerow(Collected_Data)

#EMPTY LIST FOR FINAL COLLECTED DATA TO APPEND TO CSV ROW 
Collected_Data = []

#STATION LIST COLLECTED AND POPULATED FORM All_Stations.txt
Station_List = []

#LOOP THROUGH EACH LINE OF All_Stations.txt AND APPEND TO Station_List
for eachline in All_Stations: 
	Station_List.append(eachline)
Station_List = map(str.strip, Station_List)	


#VISUAL FOR LOOP ITERATIONS 
i=0
for each in Station_List: 

	#VISUAL FOR LOOP ITERATIONS 
	i+=1 
	print i 
	if i <= 61:
		#EMPTIES LIST FOR Collected_Data
		Collected_Data = []
		
		#PTYON REQUESTS TO SEND GET REQUEST FOR EACH LINK IN Station_List
		r = requests.get(each)
		
		#CONTINUES IF WEBPAGE EXISTS AND RETURN HTTP CODE "200"
		if r.status_code == 200:
		
			#GAS STATION NAME	
			#soup VARIABLE CREATED FOR WEBPAGE CONTENTS PARSING WITH HTML5LIB INSTEAD OF BUILT-IN-PYTHON PARSER
			soup = BeautifulSoup(r.content, "html5lib")
			#VARIABLE CONTENT IS CREATED FOR ALL ITEMS WITH THE <"dt"> TAG
			content = soup.find_all("dt")
			
			#LIST FOR GETTING ALL TEXT ITEMS WITH <"dt"> TAG AND KEEPING THE FIRST ELEMENT
			Gas_Station_Name = []
			
			# LOOP THROUGH ALL ITEMS WITH <"dt"> TAG AND STORE IN Gas_Station_Name LIST
			for item in content: 
				item = item.text
				Gas_Station_Name.append(item)
				
			#RETRIEVES FIRST ELEMENT OF Gas_Station_Name AND STORES IT AS GAS STATION NAME AND APPENDS TO COLLECTED_DATA LIST
			Gas_Station_Name = 	Gas_Station_Name[0]
			Collected_Data.append(Gas_Station_Name)
			
			#SEARCH THROUGH <dd> TAGS FOR GAS STATION ADDRESS
			content = soup.find_all("dd")
			
			#CREATES LIST CALLED Address_List 
			Address_List = []
			
			#LOOPS THROUGH <dd> TAG ITEMS AND TAKES FIRST 4 ELEMENTS TO USE AS TEH ADDRESS INFORMATION 
			for item in content: 
				item = item.text
				Address_List.append(item)
			Address_List = 	Address_List[:4]
			
			#LOOPS THROUGH STRIPPED Address_List AND APPENDS ADDRESS DATA TO FINAL Collected_Data LIST
			for item in Address_List:
				Collected_Data.append(item)
				
			#Empty GAS PRICE LIST
			Regular_Gas_Price = []
			
			#REGEX SEARCH PATTERN 
			pattern = (r'\d+')
			
			#BEAUTIFUL soup FINDING TABLE (<td>) WITH CLASS: 'sp_A' - Regular Gas
			Regular_Gas_Prices = soup.find("td", {"class": "sp_A"})
			
			#SEARCHES DIV CLASSES FOR CRRENT GAS PRICES (STORED AS DIV TAGS) 
			#FOR LOOP for regular gas prices  
			for item in Regular_Gas_Prices:

				#IF STATION DOES NOT HAVE REGULAR GAS
				if Regular_Gas_Prices.find("div", {"class": "sp_no_price"}):
				
					#POPULATE LIST WITH PLACEHOLDER
					Regular_Gas_Price = ['---']
					
				else:	
				
					#FIRST THE CLASS 'sp_p sp_ml' IS ATTEMPTED 
					tmp = Regular_Gas_Prices.find_all("div", {"class": "sp_p sp_ml"})
					
					
					for item in tmp: 
					
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL REGULAR_GAS_PRICE LIST 
						Regular_Gas_Price.append(item)
						
					#CLASS 'sp_p' IS ATTEMPTED 
					tmp = Regular_Gas_Prices.find_all("div", {"class": "sp_p"})
					
					for item in tmp: 
					
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						Regular_Gas_Price.append(item)
						
			# STORES FIRST ELEMENT OF REGULAR_GAS_PRICE AND APPEND TO Collected_Data LIST			
			Regular_Gas_Price = Regular_Gas_Price[0]
			Collected_Data.append(Regular_Gas_Price)
			
			#MID GRADE GAS PRICE
			Mid_Grade_Gas_Price = []
			#BEAUTIFULSOUP FINDING TABLE (<td>) WITH CLASS: 'sp_B' - Mid Grade Gas
			Mid_Grade_Gas_Prices = soup.find("td", {"class": "sp_B"})
			
			for item in Mid_Grade_Gas_Prices:
				#print item
				if Mid_Grade_Gas_Prices.find("div", {"class": "sp_price"}):
					tmp = Mid_Grade_Gas_Prices.find_all("div", {"class": "sp_p sp_ml"})
					
					for item in tmp: 
						
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL Mid_Grade_Gas_Price LIST 
						Mid_Grade_Gas_Price.append(item)
						
					tmp = Mid_Grade_Gas_Prices.find_all("div", {"class": "sp_p"})
					
					for item in tmp: 
					
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL Mid_Grade_Gas_Price LIST 
						Mid_Grade_Gas_Price.append(item)
				else:	
					Mid_Grade_Gas_Price = ['---']
					
			Mid_Grade_Gas_Price = Mid_Grade_Gas_Price[0]
			Collected_Data.append(Mid_Grade_Gas_Price)

			# PREMIUM GAS PRICES
			Premium_Gas_Price = []
			
			#BEAUTIFUL soup FINDING TABLE (<td>) WITH CLASS: 'sp_A' - Premium Gas
			Premium_Gas_Prices = soup.find("td", {"class": "sp_C"})
			
			for item in Premium_Gas_Prices:
				#print item
				if Premium_Gas_Prices.find("div", {"class": "sp_price"}):
					tmp = Premium_Gas_Prices.find_all("div", {"class": "sp_p sp_ml"})
					
					for item in tmp: 
						
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL Premium_Gas_Price LIST 
						Premium_Gas_Price.append(item)
						
					tmp = Premium_Gas_Prices.find_all("div", {"class": "sp_p"})
					
					for item in tmp: 
						
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL Premium_Gas_Price LIST 
						Premium_Gas_Price.append(item)
						
				else:	
					Premium_Gas_Price = ['---']
					
			Premium_Gas_Price = Premium_Gas_Price[0]
			Collected_Data.append(Premium_Gas_Price)

			#DIESEL GAS PRICES
			Diesel_Gas_Price = []
			
			#BEAUTIFUL soup FINDING TABLE (<td>) WITH CLASS: 'sp_A' - Diesel
			Diesel_Gas_Prices = soup.find("td", {"class": "sp_D"})
			
			for item in Diesel_Gas_Prices:
				
				if Diesel_Gas_Prices.find("div", {"class": "sp_price"}):
					tmp = Diesel_Gas_Prices.find_all("div", {"class": "sp_p sp_ml"})
					
					for item in tmp: 
						
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL Diesel_Gas_Price LIST 
						Diesel_Gas_Price.append(item)
						
					tmp = Diesel_Gas_Prices.find_all("div", {"class": "sp_p"})
					
					for item in tmp: 
					
						#USING REGEX PATTERN TO EXTRACT ONLY DIGITS FROM GAS PRICES 
						item = re.findall(pattern, str(item))
						
						#INSERT A DECIMAL ONE INDEX FROM LEFT
						item.insert(-1, '.') 
						
						#JOINS ALL EXTRACTED DIGITS FOUND WITH SEARCH FUNCTION 
						item = ''.join(item)
						
						#APPENDS JOINED LIST TO FINAL Diesel_Gas_Price LIST 
						Diesel_Gas_Price.append(item)
						
				else:	
					Diesel_Gas_Price = ['---']
					
			Diesel_Gas_Price = Diesel_Gas_Price[0]
			Collected_Data.append(Diesel_Gas_Price)

			Collected_Data.append(now.strftime("%Y-%m-%d"))
			print Collected_Data
			
			wr = csv.writer(Gas_Price_CSV, dialect='excel')
			wr.writerow(Collected_Data)
			
			#Collected_Data = [Gas_Station_Name, Address_List, Regular_Gas_Price, Mid_Grade_Gas_Price, Premium_Gas_Price, Diesel_Gas_Price]  
		

	
	
fromaddr = '---------'
toaddr = 'travis.vanos@gmail.com'
password = str('-------')
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = ("Gas Prices" + Time_Stamp)
 
body = ("Gas Prices for" + Time_Stamp)
 
msg.attach(MIMEText(body, 'plain'))
 
filename = f
attachment = open(f, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
try:
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() # optional, called by login()
	server_ssl.login(fromaddr, password)
	#server_ssl.starttls()
	text = msg.as_string()
	server_ssl.sendmail(fromaddr, toaddr, text)
	server_ssl.close()
	print "\n\nSent the email!!"
except: 
	print "\n\nFailed to send"
	
try:
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() # optional, called by login()
	server_ssl.login(fromaddr, password)
	#server_ssl.starttls()
	text = msg.as_string()
	server_ssl.sendmail(fromaddr, "----", text)
	server_ssl.close()
	print "\n\nSent the email!!"
except: 
	print "\n\nFailed to send"	