# ####################################### LOAD REQUIRED LIBRARIES ############################################# #
import os
import time
import datetime
import gdal
# ####################################### SET TIME-COUNT ###################################################### #
starttime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("Starting process, time:" +  starttime)
print("")
# ####################################### FUNCTIONS, FOLDER PATHS AND BASIC VARIABLES ######################### #
root_folder = "D:/baumamat/Warfare/_Variables/Forest/LossYear/"
outVRT = "D:/baumamat/Warfare/_Variables/Forest/LossYear.vrt"
outTXT = "D:/baumamat/Warfare/_Variables/Forest/fileList.txt"
epsg = 54009
# #### (1) BUILD OUTPUT TEXT FILES WITH PATHS FROM THE DIFFERENT FOLDERS
print("Build List")
finalFileList = []
file_list = os.listdir(root_folder)
for file in file_list:
    if file.endswith(".tif"):
        filepath = root_folder + file
        finalFileList.append(filepath)
# #### (2)  WRITE LIST TO OUTPUT-FILE
f_open = open(outTXT, "w")
for item in finalFileList:
    f_open.write(item + "\n")
f_open.close()
# #### (3) BUILD VRT
print("Build VRT")
command =  "gdalbuildvrt.exe -vrtnodata 0 -input_file_list " + outTXT + " " + outVRT
os.system(command)
os.remove(outTXT)

#-a_srs EPSG:" + str(epsg) + "
# ####################################### END TIME-COUNT AND PRINT TIME STATS################################## #
print("")
endtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("start: " + starttime)
print("end: " + endtime)
print("")