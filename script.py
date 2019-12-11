import os
import time
import json
import re
from collections import namedtuple
from dotenv import load_dotenv
from icalevents.icalevents import events
from requests import request
from icalendar import cal, Calendar

load_dotenv()

with open(os.getenv("CALENDAR_PATH")) as file:
    data = file.read()

es = Calendar.from_ical(data)

events = []

for appointment in es.walk('vevent'):
    event = appointment.get('summary')
    e = event.split(' ,')
    e = e[0].split(' VO')
    e = e[0].split(' VU')
    e = e[0].split(' TT')
    e = e[0].split(' UE')
    e = e[0].split(' FA')
    e = e[0].split(' (')
    e = e[0].split(' -')
    
    if e[0].__contains__("Tutorien zu"):
        e = e[0].replace('Tutorien zu ', '')
        e = e.join(' ')

    if e[0].__contains__("MAP BM" or "MAP AM"):
        e = e[0].replace("MAP BM ", '')
        e = e[0].replace("MAP AM ", '')
        e = e.join(' ')
    if not events.__contains__(e[0]):
        events.append(e[0])

events.sort()
events = [x for x in events if len(x) > 2]

# -----------------------------------
# COURSE CREATION START
# -----------------------------------

courses = events
folderNames = ["Sonstiges", "Tutorium", "Übung", "Vorlesung"]

semesterNumber = '4.'

oneDriveFolder = ""
if os.path.isdir(os.getenv("ONEDRIVE_MAC_PATH")) :
    oneDriveFolder = os.getenv("ONEDRIVE_MAC_PATH")
else :
    oneDriveFolder = os.getenv("ONEDRIVE_MACBOOK_PATH")

if not os.path.isdir(f"{oneDriveFolder}/1. Studium{semesterNumber} Semester"):
    try:
        os.mkdir(
            f"{oneDriveFolder}/1. Studium/{semesterNumber} Semester")
    except:
        print("✖️ - OneDrive path already created")

for course in courses:
    if not os.path.isdir(f"{oneDriveFolder}/1. Studium{semesterNumber} Semester/{course}"):
        try:
            os.mkdir(
                f"{oneDriveFolder}/1. Studium/{semesterNumber} Semester/{course}")
        except:
            print("✖️ - Course folder already created.")
        for index, folder in enumerate(folderNames):
            try:
                os.mkdir(
                    f"{oneDriveFolder}/1. Studium/{semesterNumber} Semester/{course}/{folder}")
                print(
                    f"✔️ - Created {index+1}/{len(folderNames)} -> {course}/{folder}")
            except:
                print("✖️ - Course subfolders already created!")

'''
def getCurrentSemester():
    semesters = {
        "3.": {
            "dateStart": "01.10.2019",
            "dateEnd": "31.01.2019"
        },
        "4.": {
            "dateStart": "31.01.2020",
            "dateEnd": "17.07.2020"
        },
        "5.": {
            "dateStart": "18.07.2020",
            "dateEnd": "05.02.2021",
        },
        "6.": {
            "dateStart": "06.02.2021",
            "dateEnd": "23.07.2021"
        }
    }

    #semester_json = json.load(semesters)
    Struc = namedtuple(semesters)

    currentDate = time.strftime("%d.%m.%Y")
    print(currentDate)

    for semester in semesters.items():
      print(semester.dateEnd)


getCurrentSemester()
'''
