# Copyright:   (c) Travis Vanos @ Equilibrium Consulting
# ArcGIS Version:   10.3
# Python Version:   2.7
#--------------------------------

#Libraries required for execution
import os
from shutil import rmtree
import arcpy
import time


def SpatialJoiner (input_GDB, input_Point_FeatureClass, input_Boundary_FeatureClass, output_FeatureClass):
	start_time = time.time()
	#Folder for Submission
	folder_name = ("C:\\temp\\D3Tvanos9307")
	input_GDB = "C:\\temp\\d3RawData\\" + input_GDB
	output_GDB = "C:\\temp\\D3Tvanos9307\\d3Proc.gdb"

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
	if not os.path.exists(output_GDB):
		arcpy.CreateFileGDB_management(folder_name, "d3Proc.gdb")
	#Else folder structure exists so deletes folder tree and recreate contents
	print "Done\n"

	print "Setting Workspace.........\n"
	arcpy.env.workspace = "C:\\temp\\D3Tvanos9307\\d3Proc.gdb"
	arcpy.env.overwriteOutput = 1 
	arcpy.env.outputCoordinateSystem = 26917 	
	arcpy.CheckOutExtension("spatial")
	print "Done\n\n"

	print "Importing Shapefiles........\n"
	arcpy.FeatureClassToGeodatabase_conversion (input_GDB + "\\" + input_Point_FeatureClass, output_GDB)
	arcpy.FeatureClassToGeodatabase_conversion (input_GDB + "\\" + input_Boundary_FeatureClass, output_GDB)
	print "\nDone\n\n"

	# Setting local variables for spatial join
	FieldMap = arcpy.FieldMap()
	MappingField = arcpy.FieldMappings()
	if input_Boundary_FeatureClass == "usStates":
		FieldMap.addInputField(input_GDB + "\\" + input_Boundary_FeatureClass, 'STATE_NAME')
	else:
		FieldMap.addInputField(input_GDB + "\\" + input_Boundary_FeatureClass, 'NAME')
	MappingField.addFieldMap(FieldMap)

	print "Joining Spatial Data........."
	arcpy.SpatialJoin_analysis(input_Boundary_FeatureClass, input_Point_FeatureClass, output_GDB + "\\" + output_FeatureClass, "JOIN_ONE_TO_ONE", "KEEP_ALL", MappingField)
	print "\nDone\n\n"
	
	output_Field = "NumOf" + input_Point_FeatureClass[2:]
	print "Changing Field names..........\n"
	arcpy.AlterField_management(output_FeatureClass, 'Join_Count', output_Field, output_Field)
	arcpy.DeleteField_management(output_FeatureClass, 'TARGET_FID')
	print "Done\n\n"
	print("Process completed for" + output_FeatureClass + " in --- %s seconds ---" % int(time.time() - start_time))
	

SpatialJoiner("d3Raw.gdb", "npFarm", "npCsd", "countyFarm", )
SpatialJoiner("usa.gdb",  "usCities", "usCounties", "countyCities")
SpatialJoiner("usa.gdb",  "usCities", "usStates", "statesCities")
SpatialJoiner("usa.gdb",  "usCities_dtl", "usStates", "statesCities")