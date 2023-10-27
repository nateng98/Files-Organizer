import os
from pathlib import Path

# path to the folder you want to sort
mainPath = r"c:/Users/Nathan/Desktop"

# I only list all the files that I often download and their folders
# they are associated with
# Get types of the files
folderNames = {
  "Compressed": {'7z','zip', 'rar'},
  "Programming": {'py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'sql'},
  "Documents": {'pdf', 'doc', 'docx'},
  "Images": {'jpg', 'png', 'gif', 'svg', 'bmg'},
  "Others": {'NONE'}
}

# Extract list
# check files whether they are "file" or "folder", then sort into the proper list
fileList = [os.path.join(mainPath, file)
  for file in os.listdir(mainPath)
    if os.path.isfile(os.path.join(mainPath, file))]
#print(fileList)

folderList = [os.path.join(mainPath, file)
  for file in os.listdir(mainPath)
    if not os.path.isfile(os.path.join(mainPath, file))]
#print(foldeList)

# mapping file extensions with associated folders
fileExtensionMapping = {extension: fileType
  for fileType, extensions in folderNames.items() #e.g: py: Programming, jpg: Images
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
# Basic concept: 
# - split each file by '.' to get extension
# - knowing extension, we will check which folder that extension maps to
# - if the extension doesn't map to anything, throw it to Others folder
# - then make a new path :\mainPath\newFolder\theFile.extension
def sortingFile(theFile):
  extension = str(theFile).split('.')[-1] # 1 generally still works but -1 will always make sure that we check the end of string (the extension)
  newFolder = fileExtensionMapping[extension] if extension in fileExtensionMapping.keys() else 'Others'
  newPath = os.path.join(mainPath, newFolder, str(theFile).split('\\')[-1]) # '\\' == '\'
  return newPath
# Move files into their associated folders by changing their paths (rename it with newPath)
[Path(eachFile).rename(sortingFile(eachFile)) for eachFile in fileList]

# Do the same to others (Same concept with a few tweaks)
[Path(folder).rename(os.path.join(mainPath, 'Others', str(folder).split('\\')[-1]))
  for folder in folderList
    if str(folder).split('\\')[-1] not in folderNames.keys()]