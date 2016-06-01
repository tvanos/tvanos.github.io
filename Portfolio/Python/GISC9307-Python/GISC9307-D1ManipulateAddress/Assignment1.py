#!/usr/bin/env python
"""
DESCRIPTION

    This script is for reorganizing and sorting given addresses and postal codes and sorting the strings into a more visual appealing format.  
	
AUTHOR

    Travis Vanos <Travis.vanos@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.
	The script is for EDUCATIONAL PURPOSES ONLY 

VERSION

	Version: 1.1
"""

#Libraries required for execution
import sys, os
import re
import shutil

#Folder for Submission
folder_name = (r'C:\temp\Tvanos9307D1\d1ProcData')

#If path does not exist the folder is created proper structure
if not os.path.exists(folder_name):
	os.makedirs(folder_name)
#Else folder structure exists so deletes folder tree and recreate contents
else:
	shutil.rmtree(folder_name)
	os.makedirs(folder_name)

#Copying the data from d1RawListOfFarms.txt into new text file for reading in C:\temp\Tvanos9307D1\d1ProcData folder
shutil.copyfile(r'C:\temp\d1RawListOfFarms.txt', folder_name + r'\d1RawListOfFarms.txt')

#Opens created text file, populated with data, for reading
farm_data = open(folder_name + r'\d1RawListOfFarms.txt', 'r')

#Creates a text file ready to populate with final output of values 
f = open(folder_name + r'\Final_List_Of_Farms.txt', 'w')

#String list to write headers to output file
header_list = ["FarmID\t", "Street #\t", "Street\t", "Suffix\t", "Dir\t", "City\t", "Province\t", "Postal Code\t\n"]

#For Loop to write header_list to output file
for item in header_list:
	f.write(item)
f.close()

#Logical counter for number of records in d1RawListOfFarms.txt raw data
farm_ID = 0
#Sorted_data will be final list of sorted lines
sorted_data = []
#Loops through each line of the input file and preforms search for each line 
for eachline in farm_data: 
	#Defines the regex search pattern used for string check & Validation 
	province_check = re.search ("\s\w\w\s", eachline)
	#If statement for function only if pattern is found 
	if province_check is not None:
		#Saves first result found of regex check 
		x = province_check.group(0)
		if x == " AB " or x == " BC " or x == " MB " or x == " NB " or x == " NL " or x == " NS " or x == " NT " or x == " NU " or x == " ON " or x == " PE " or x == " QC " or x == " SK " or x == " YT ":
			#Province saved as first item found in pattern check is saved as province
			province = province_check.group(0)
			#strips whitespace and commas
			province = province[1:-1]
	#If unmatched set to Null
	else:
		province = ''
	
	#Defines the regex search pattern used for string check & Validation 
	postal_code_check = re.search("[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]", eachline , re.IGNORECASE ) 
	#If statement for function only if pattern is found 
	if postal_code_check is not None: 
		#Saves first result found of regex check 
		postal_code = postal_code_check.group(0)
	#If unmatched set to Null
	else: 
		postal_code = ''
	
	#Defines the regex search pattern used for string check & Validation 
	address_check = re.search("\s\d*\s\w*\s\w*\s*\w*,", eachline , re.IGNORECASE ) 
	#If statement for function only if pattern is found 
	if address_check is not None: 
		#Saves first result found of regex check 
		address = address_check.group(0)
		#Strips commas/whitespace matched in search
		address = address[1:-1]
	#If unmatched set to Null
	else: 
		address = ''
	
	#Defines the regex search pattern used for string check & Validation 
	city_check = re.search(",\s*\S*(\.?\s*)?\w*," , eachline , re.IGNORECASE | re.DOTALL)
	#If statement for function only if pattern is found 
	if city_check is not None: 
		#Saves first result found of regex check 
		city = city_check.group(0)
		city = city[2:-1]
	#If unmatched set to Null
	else: 
		city = ''
	
	#Sorted data into list of results of regex searches
	sorted_data = [farm_ID, address, city, province, postal_code]
	#Splits address into a list of elements seperated on whitespace characters
	address = sorted_data[1].split()
	#If address list has three elements and no directional value
	
	#Concatenate Roads that have spaces
	if farm_ID >= 1 and len(address) == 4 and str(address[-1]) != "N" and str(address[-1]) != "W" and str(address[-1]) != "E" and str(address[-1]) != "S":
		address[1] = address[1] + ' ' + address[2]
		address.pop(2)

	if len(address) == 3: 
		#Adding null value for lack of direction
		address.append('')
	#Removes element from sorted_data and reinserts new address list with [4] elements
	sorted_data.pop(1)
	
	
	#Logical counter for loop iterations
	i = 0
	#Sperate address string 
	for item in address:
		i += 1
		#Inserts list elements in the proper order from address list 
		sorted_data.insert(i, item)
		
	print sorted_data
	
	#Does not write first line of input file
	if farm_ID >= 1:
		#Open file for appending
		f = open(folder_name + r'\Final_List_Of_Farms.txt', 'a')
		#Write each element to file appending a tab character to each element
		for item in sorted_data:	
			f.write(str(item))
			f.write('\t')
		f.write('\n')
	#Increase Farm_ID by one to for counting farm identifies in output file	
	farm_ID += 1		
