import os
from pathlib import Path

# If you want to have different folder for every type of files then
# this is not the right script. I'll update a script for that later.

# I only list all the files that I often download and their folders
# they are associated with

# Depends on what files you download you can add on to this list

# Get types of the files
folderNames = {
  "Compressed": {'7z','zip', 'rar'},
  "Programming": {'py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'sql'},
  "Documents": {'pdf', 'doc', 'docx'},
  "Images": {'jpg', 'png', 'gif', 'svg', 'bmg'},
  "Others": {'NONE'}
}

# path to the folder you want to sort
mainPath = r"c:/Users/Nathan/Desktop/COMP3380Ass2NguyenNhatAnh"

# Extract list
# check files whether they are "file" or "folder", then sort into 
# the proper list
fileList = [os.path.join(mainPath, file)
  for file in os.listdir(mainPath)
    if os.path.isfile(os.path.join(mainPath, file))]
#print(fileList)

foldeList = [os.path.join(mainPath, file)
  for file in os.listdir(mainPath)
    if not os.path.isfile(os.path.join(mainPath, file))]
#print(foldeList)

# mapping file extensions with associated folders
fileExtensionMapping = {extension: fileType
  for fileType, extensions in folderNames.items() #e.g: Programming - py
    for extension in extensions}
#print(fileExtensionMapping)

# Make a list of folderNames 
folderPaths = [os.path.join(mainPath, folderName)
  for folderName in folderNames.keys()]
#print(folderPaths)
# make folders that don't exist
[os.mkdir(folderPath)
  for folderPath in folderPaths
    if not os.path.exists(folderPath)]

# Sorting