import os
import time
import json
from collections import namedtuple
from dotenv import load_dotenv
from icalevents.icalevents import events
from requests import request

load_dotenv()

courses = ["Programmierpraktikum", "SCM", "CGV"]
folderNames = ["Vorlesung", "Übung", "Tutorium", "Sonstiges"]

semesterNumber = '4.'

oneDriveFolder = ""

if os.path.isdir(os.getenv("METIMAC_PATH")) :
    oneDriveFolder = os.getenv("METIMAC_PATH")
else :
    oneDriveFolder = os.getenv("METMAC_PATH")

if not os.path.isdir(f"{oneDriveFolder}/1. Studium{semesterNumber} Semester"):
    os.mkdir(
        f"{oneDriveFolder}/1. Studium/{semesterNumber} Semester")

for course in courses:
    if not os.path.isdir(f"{oneDriveFolder}/1. Studium{semesterNumber} Semester/{course}"):
        os.mkdir(
            f"{oneDriveFolder}/1. Studium/{semesterNumber} Semester/{course}")
        for index, folder in enumerate(folderNames):
            os.mkdir(
                f"{oneDriveFolder}/1. Studium/{semesterNumber} Semester/{course}/{folder}")
            print(
                f"Created {index+1}/{len(folderNames)} -> {semesterNumber} Semester/{course}/{folder}")

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
