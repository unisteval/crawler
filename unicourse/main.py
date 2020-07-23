from actions import *

if __name__ == "__main__":
    sapid, contextid = initaction()
    search = Search(sapid, contextid)

    year = int(input("Year: "))
    semester = int(input("Semester: "))

    search.set_period(year,semester)

    string = input("Search: ")

    search.search_string(string)

    search.get_excel()
    

