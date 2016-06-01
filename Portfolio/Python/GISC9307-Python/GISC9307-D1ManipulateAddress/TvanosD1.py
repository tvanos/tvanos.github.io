import sys, os
import re
import shutil
import csv


folder_name = (r'C:\temp\Tvanos8307D1\d1ProcData')

if not os.path.exists(folder_name):
	os.makedirs(folder_name)
else:
	shutil.rmtree(folder_name)
	os.makedirs(folder_name)

shutil.copyfile(r'X:\GIS Resources\GIS - Second Semester\gisc9307 - PythonScriptingForArcGis\assignments\d1ManipulateAddress\d1RawData\d1RawListOfFarms.txt', folder_name + r'\d1RawListOfFarms.txt')
farm_data = open(folder_name + r'\d1RawListOfFarms.txt', 'r')


f = open(folder_name + r'\Final_List_Of_Farms.txt', 'w')
f.close()


farm_ID = 0
sorted_data = []
for eachline in farm_data: 
	
	province_check = re.search ("\s\w\w\s", eachline)
	if province_check is not None:
		x = province_check.group(0)
		if x == " AB " or x == " BC " or x == " MB " or x == " NB " or x == " NL " or x == " NS " or x == " NT " or x == " NU " or x == " ON " or x == " PE " or x == " QC " or x == " SK " or x == " YT ":
			province = province_check.group(0)
			province = province[1:-1]
	else:
		province = "N/A"
			
	postal_code_check = re.search("[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]", eachline , re.IGNORECASE ) 
	if postal_code_check is not None: 
		print postal_code_check.group(0)
		postal_code = postal_code_check.group(0)
	else: 
		postal_code = "N/A"
	
	address_check = re.search("\s\d*\s\w*\s\w*\s*\w*,", eachline , re.IGNORECASE ) 
	if address_check is not None: 
		print address 
		address = address_check.group(0)
		address = address[1:-1]
	else: 
		address = "N/A"
		
	city_check = re.search(",\s\S*,", eachline , re.IGNORECASE ) 
	if city_check is not None: 
		print city
		city = city_check.group(0)
		city = city[2:-1]
		print city
	else: 
		city = "N/A"
	
	sorted_data = [farm_ID, address, city, province, postal_code]
	address = sorted_data[1].split()
	if len(address) == 3: 
		address.append("---")
	print address	
	sorted_data.pop(1)
	
	#Logical counter for loop iterations
	i = 0
	#Sperate address string 
	for item in address:
		i += 1
		#Inserts list elements in the proper order from address list 
		sorted_data.insert(i, item)
	print sorted_data
	
	if farm_ID >= 1:
		f = open(folder_name + r'\Final_List_Of_Farms.txt', 'a')
		for item in sorted_data:	
			f.write(str(item)