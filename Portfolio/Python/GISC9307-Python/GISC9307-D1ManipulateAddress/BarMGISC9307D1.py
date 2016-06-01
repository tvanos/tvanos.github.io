################################################################################################
#Title: Manipulate Street Address
#Author: Mike Bar
#Date: February 2, 2016
#GISC9308 - Python Scripting for ArcGIS
#Purpose - To separate a whole piece of mailing address into different address components, such as street number,
# street name, street suffix type, street direction, city, province, and postal code.
################################################################################################
import os, shutil, re

#Defines the direction with four possible variables.


# Step 3 Part A. 1)	Create subfolder d1ProcDataLastNameInitial subfolder within c:\temp subfolder.
# Also deletes the new subfolder if it exists before creating it. 

filePath = (r'C:\temp\d1ProcDataBarM')

#Selects input d1RawListOfFarms.txt from folder, and make new file called d1ResultListOfFarms.txt in the specific folder
if not os.path.exists(filePath):
	os.makedirs(filePath)
#Else folder structure exists so deletes folder tree and recreate contents
else:
	shutil.rmtree(filePath)
	os.makedirs(filePath)

shutil.copyfile(r'C:\temp\d1RawListOfFarms.txt', filePath + r'\d1RawListOfFarms.txt')

#Access input and output files
#Opens d1RawListOfFarms.txt for reading
infile = open(filePath + r'\d1RawListOfFarms.txt')

#Creates outfile
outfile = open(filePath + r'\FinalListOfFarms.txt', 'w')

Directions = ["N","E","S","W"]


#Creates the headings that will be used in the output file
Headings = ('FarmID\tAddress\tStreetNum\tStreetName\tSuffix\tDir\tCity\tProvince\tPostalCode\n')
outfile.write(Headings)

i = 0
for line in infile:
	if i >= 1:
		blankSpace = line.rstrip('\n')
		markerSpace = blankSpace.split('\t')
		print markerSpace
		#Creates ID number in first column and inserts it
		FarmID = markerSpace[0]
		FullAddress = markerSpace[1].split(', ')
		city = FullAddress[1]
		addressPattern = re.search("\s\d*\s\w*\s\w*\s*\w*,", line , re.IGNORECASE ) 
		#If statement for function only if pattern is found 
		if addressPattern is not None: 
			#Saves first result found of regex check 
			address = addressPattern.group(0)
			#Strips commas/whitespace matched in search
			address = address[1:-1]
		else:
			address = " "
		
		StreetNum = address.split(" ")[0]
		StreetName = address.split(" ")[1:]
		
		
		if str(address[-1]) == "N" or str(address[-1]) == "W" or str(address[-1]) == "E" or str(address[-1]) == "S":
			dir = str(address[-1])
			StreetName.pop(-1)
		else: 
			dir = ''
		
		StreetSuffix = StreetName[-1]
		StreetName.pop(-1)
		
		if len(StreetName) >= 2: 
			StreetName = StreetName[0] + ' ' + StreetName[1]
		elif len(StreetName) == 1:
			StreetName = str(StreetName[0])
			
		postalCodeCheck = re.search("[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]", line , re.IGNORECASE ) 
		#If pattern is found 
		if postalCodeCheck is not None: 
			#Saves first result found of regex check 
			PostalCode = postalCodeCheck.group(0)
		#Unmatched set to Null
		else: 
			PostalCode = ''
		
		print FarmID
		print StreetNum
		print StreetName
		print StreetSuffix
		print dir
		print city
		print PostalCode
		
		outfile.write(FarmID + '\t' + StreetNum + '\t' + StreetName + '\t'
						 + StreetSuffix + '\t' + dir + '\t' + city + '\t'
						 + 'ON' + '\t' + PostalCode + '\n')
		
	i += 1
infile.close()
outfile.close()
