from .actions import *
from openpyxl import load_workbook

class Lecture:
    def __init__(self, row_list):
        self.id = ""

        self.classification = row_list[0]
        self.courseNumber = row_list[1]
        self.courseName = row_list[2]
        self.profName = row_list[3]
        self.grades = row_list[4]
        self.seats = str(row_list[5])
        self.hoursClassroom = row_list[6]
        self.course = row_list[7]
        self.prerequisite = row_list[8]
        self.courseTarget = row_list[9]


    def printObject(self):
        print("이수구분: " + self.classification)
        print("과목번호: " + self.courseNumber)
        print("교과목명: " + self.courseName)
        print("교수명: " + self.profName)
        print("학점/이론/실습" + self.grades)
        print("여석: " + self.seats)
        print("강의시간(강의실): " + self.hoursClassroom)
        print("과정: " + self.course)
        print("선이수: " + self.prerequisite)
        print("수강대상: " + self.courseTarget)

    
    def setid(self, year, semester):
        self.id = year + semester + "_" + self.courseNumber


def lectureList(year, semester, string):
    ret_list = []

    file_location = "./export.xlsx"

    get_file(year, semester, string, file_location)
    load_wb = load_workbook(file_location, data_only=True)
    load_ws = load_wb['Data']

    for row in load_ws.rows:
        row_value = []
        for cell in row:
            row_value.append(cell.value)
        lec = Lecture(row_value)
        ret_list.append(lec)

    return ret_list[1:]
