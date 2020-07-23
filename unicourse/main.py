from actions import *

if __name__ == "__main__":
    sapid, contextid = initaction()
    search = Search(sapid, contextid)

    year = int(input("Year: "))
    semester = int(input("Semester: "))

    #year = 2019
    #semester = 90

    search.set_period(year,semester)

    string = input("Search: ")

    #string = 'CSE'

    search.search_string(string)

    search.get_excel()
   
    print(search.get_text())
    

