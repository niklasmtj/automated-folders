# automated-folders

This script automatically create the folders I need in my OneDrive folder for a new semester at university. The module names are pulled out of an ICS Calendar file.

## .ENV file

This script needs a .env file to run with the following variables
``` 
ONEDRIVE_MAC_PATH="/path/to/uni/folder"
CALENDAR_PATH="path/to/icsCalendar"
```

The reason of the third ENV `ONEDRIVE_MACBOOK_PATH` is because I use two different Mac machines and so different Paths.

## Foldernames

The folder names are set in the script in the folderNames variable.

## Semester number

The number of the current semester is at the moment set in the semesterNumber variable.