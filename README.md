# Files Organizer
A python script that helps organization your folder, putting your files into different (sub)folders based their extensions.

## Choose a folder you want to be organized
Set up the path of the folder
``` python
mainPath = r"c:/Users/user_name/destination_1/..."
```
For example: I want to organize my Desktop
``` python
mainPath = r"c:/Users/Nathan/Desktop"
```
## Set up folders and type of files that will be arranged
Depends on how you want to organized your files/folders, you set up the way you like based on this template
``` python
folderName = {
  "folder_1": {'type_of_file_1', 'type_of_file_2'},
  "folder_2": {'type_of_file_1', 'type_of_file_2'},
  ...
}
```
For example: I only have code, compressed files, images, and document need to be organized. So I made 4 main folders and 'Others' for files that are not accounted for
``` python
folderNames = {
  "Compressed": {'7z','zip', 'rar'},
  "Programming": {'py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'sql'},
  "Documents": {'pdf', 'doc', 'docx'},
  "Images": {'jpg', 'png', 'gif', 'svg', 'bmg'},
  "Others": {'NONE'}
}
```
If you are someone who has music, video, etc. You can add something like:
``` python
"Music": {'mp3','mpa','wav'},
'Videos':{'avi','flv','mkv','mov','mp4','wmv'}
```
## Run the script on your terminal!
``` bash
python organizer.py
```
### Author
<li><a href="https://github.com/nateng98">Nước Mắm Code</a></li>
