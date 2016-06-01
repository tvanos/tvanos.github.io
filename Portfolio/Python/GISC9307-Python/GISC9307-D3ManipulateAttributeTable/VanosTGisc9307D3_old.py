# Copyright:   (c) Travis Vanos @ Equilibrium Consulting
# ArcGIS Version:   10.3
# Python Version:   2.7
#--------------------------------

#Libraries required for execution
import os
from shutil import rmtree
import arcpy
import time

#Start time for excecution time
start_time = time.time()
#Folder for Submission
folder_name = (r'C:\temp\D3Tvanos9307')
gdb = (r'C:\temp\D3Tvanos9307\d3Proc.gdb')

print "Preparing Files......\n"
#If path does not exist the folder is created proper structure
if not os.path.exists(folder_name):
	os.makedirs(folder_name)
#Else folder structure exists so deletes folder tree and recreate contents
else:
	print ("Remove existing files.......\n")
	rmtree(folder_name)
	os.makedirs(folder_name)
print "Done\n"

print "Creating Geodatabase.............\n "	
if not os.path.exists(gdb):
	arcpy.CreateFileGDB_management(folder_name, "d3Proc.gdb")
#Else folder structure exists so deletes folder tree and recreate contents
print "Done\n"

print "Setting Workspace.........\n"
arcpy.env.workspace = r'C:\temp\D3Tvanos9307\d3Proc.gdb'
arcpy.env.overwriteOutput = 1 
arcpy.env.outputCoordinateSystem = 26917 	
arcpy.CheckOutExtension("spatial")
print "Done\n\n"

print "Importing Shapefiles........\n"
arcpy.FeatureClassToGeodatabase_conversion ("C:\\temp\d3RawData\\d3Raw.gdb\\npCsd", gdb)
arcpy.FeatureClassToGeodatabase_conversion ("C:\\temp\\d3RawData\\d3Raw.gdb\\npFarm", gdb)
print "\nDone\n\n"

# Setting local variables for spatial join
countyFarm = "countyFarm"
FieldMap = arcpy.FieldMap()
MappingField = arcpy.FieldMappings()
FieldMap.addInputField("C:\\temp\d3RawData\\d3Raw.gdb\\npCsd", 'NAME')
MappingField.addFieldMap(FieldMap)

print "Joining Spatial Data........."
arcpy.SpatialJoin_analysis("npCsd", "npFarm", gdb + "\\" + countyFarm, "JOIN_ONE_TO_ONE", "KEEP_ALL", MappingField)
print "\nDone\n\n"

print "Changing Field names..........\n"
arcpy.AlterField_management(countyFarm, 'Join_Count', 'NumOfFarm', 'NumOfFarm')
arcpy.DeleteField_management(countyFarm, 'TARGET_FID')
print "Done\n\n"
print("Process completed in --- %s seconds ---" % int(time.time() - start_time))
'''
# Set local variables
out_path = gdb
out_name = "countyFarm.shp"
geometry_type = "POLYGON"
template = ''
has_m = "DISABLED"
has_z = "DISABLED"

spatial_reference = arcpy.Describe("C:\temp\d3RawData\d3Raw.gdb\npFarm.shp").spatialReference

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)

# Set local variables
inFeatures = "countyFarm.shp"
fieldName1 = "CountyName"
fieldLength = 70
fieldAlias = "refcode"
fieldName2 = "NumOfFarm"
fieldLength = 10

#Create First Field
arcpy.AddField_management(inFeatures, fieldName1, "TEXT", "", "", fieldLength,
                          "NAME", "NULLABLE")
						  
#Create Second Field 
arcpy.AddField_management(inFeatures, fieldName2, "LONG", "", "", "", "", "NULLABLE")


print 'Calculating Points in Polygons...'

print("--- %s seconds ---" % (time.time() - start_time))
'''