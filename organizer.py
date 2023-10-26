import os
from pathlib import Path

# If you want to have different folder for every type of files then
# this is not the right script. I'll update a script for that later.

# I only list all the files that I often download and their folders
# they are associated with

# Depends on what files you download you can add on to this list

# Get types of the files
folderName = {
    "Compressed": {'7z','zip', 'rar'},
    "Programming": {'py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'sql'},
    "Documents": {'pdf', 'doc', 'docx'},
    "Images": {'jpg', 'png', 'gif', 'svg', 'bmg'},
    "Others": {'NONE'}
}

# Extract list

# I am on windows so I use '/'. If you're on Linux or macOS, please use '\'
folderPath = r"C:/Users/natha/Downloads"

# check files whehter they are "file" or "folder"
isFiles = [os.path.join(folderPath, file)
    for file in os.listdir(folderPath)
        if os.path.isfile(os.path.join(folderPath, file))]