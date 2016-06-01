# Copyright:   (c) Travis Vanos
# ArcGIS Version:   10.3
# Python Version:   2.7
#--------------------------------

#Libraries required for execution
import sys, os
import re
import shutil
import arcpy
from arcpy import env

#Folder for Submission
folder_name = (r'C:\temp\D2Tvanos9307')


#If path does not exist the folder is created proper structure
if not os.path.exists(folder_name):
	os.makedirs(folder_name)
#Else folder structure exists so deletes folder tree and recreate contents
else:
	shutil.rmtree(folder_name)
	os.makedirs(folder_name)

#Copying the data from Farms.txt and Winery.txt into new text files for reading in C:\temp\Tvanos9307D2 folder
shutil.copyfile(r'C:\temp\Farm.txt', folder_name + r'\Farm.txt')
shutil.copyfile(r'C:\temp\Winery.txt', folder_name + r'\Winery.txt')

#Opens created text file, populated with data, for reading
farm_data = open(folder_name + r'\Farm.txt', 'r')
winery_data = open(folder_name + r'\Winery.txt', 'r')

# Set workspace
arcpy.env.workspace = (r'C:\temp\D2Tvanos9307')

for file in os.listdir(folder_name):
    if file[-4:] == '.txt':
		try:
			
			shape_file_list = []
			in_file = os.path.splitext(file)
			xCoord = 'EastingM'
			yCoord= 'NorthingM'
			spRef = r'Coordinate Systems\Projected Coordinate Systems\Utm\Nad 1983\NAD 1983 UTM Zone 17N.prj'
			out_name = in_file[0]
			saved_Layer = in_file[0] + r'.shp'
			
			if arcpy.Exists(saved_Layer):
				arcpy.Delete_management(saved_Layer)
				
			# Make the XY event layer
			arcpy.MakeXYEventLayer_management(file, xCoord, yCoord, out_name, spRef, '')
			shape_file_location = folder_name
			arcpy.FeatureClassToShapefile_conversion(out_name, shape_file_location)
			# Print the total rows
			print arcpy.GetCount_management(saved_Layer)
			shape_file_list.append(saved_Layer)
		except Exception as e:
			# If an error occurred print the message to the screen
			print e.message
			arcpy.AddError(e.message) 


XMin = 610000
YMin = 4760000
XMax = 660000
YMax = 4780000
arcpy.env.extent = arcpy.Extent(XMin, YMin, XMax, YMax)

merged_data = 'npFarm.shp'
in_file = ';'.join(shape_file_list)
arcpy.Merge_management(in_file, merged_data, "FarmID \"FarmID\" true true false 10 Long 0 10 ,First,#,winery.shp,FarmID,-1,-1,farm.shp,FarmID,-1,-1;Name \"Name\" true true false 254 Text 0 0 ,First,#,winery.shp,Name,-1,-1,farm.shp,Name,-1,-1;FarmType \"FarmType\" true true false 254 Text 0 0 ,First,#,winery.shp,FarmType,-1,-1,farm.shp,FarmType,-1,-1;EastingM \"EastingM\" true true false 19 Double 0 0 ,First,#,winery.shp,EastingM,-1,-1,farm.shp,EastingM,-1,-1;NorthingM \"NorthingM\" true true false 19 Double 0 0 ,First,#,winery.shp,NorthingM,-1,-1,farm.shp,NorthingM,-1,-1")
			

Result = arcpy.GetCount_management(merged_data)
result_of_farms = int(Result.getOutput(0))
print("----------------------------------\n " + str(result_of_farms) + " Farms Within Extent\n----------------------------------")

	
	
#fcList = arcpy.ListFeatureClasses()	
#print fcList
#for file in os.listdir(folder_name):
#Execute CopyFeatures for each input shapefile
#	for shapefile in fcList:
		# Determine the new output feature class path and name
#		outFeatureClass = folder_name + r'\npFarm.shp'
#		arcpy.CopyFeatures_management(shapefile, outFeatureClass)