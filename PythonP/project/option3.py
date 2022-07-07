from lib2to3.pgen2.grammar import line
import re


def updateMark():
    r1 = ""
    token = 0
    ID = input("please enter the student ID u desire to edit his marks:")
    file = open("data.txt")
    contents = file.readlines()
    for k in contents:  # to check if the student is there
        temp = k.split("\n")  # temp now has the value of id
        if ID == temp[0]:
            token = 1
            print("ID was found:")
            temp = input("please enter the course name, all caps:")
            course = temp.upper()
            pattern = 'EN[C/E][S/E]\d\d\d\d'
            match = re.search(pattern, course)
            if not match:
                print("the format of the entered course is wrong, please try again")
                return
            mark = input("please enter the new mark:")
            f = ID + ".txt"
            fID = open(f, 'r+')
            courses = fID.readlines()  # now we have all the lines in the file
            fID.seek(0)  # so we delete it
            fID.truncate(0)
            for i in courses:
                if course in i:  # we check were the course is
                    x = i.split(";")  # if found we split the course from the mark
                    y = x[1].split(",")
                    for j in y:
                        z = j.split()
                        if z[0] == course:  # now if we found the course
                            r1 = course + " " + z[1]  # we take the first string we will replace
                            z[1] = mark
                            break
                    r2 = course + " " + mark  # second string to replace
                    # replace
                    fID.write(i.replace(r1, r2))
                else:
                    fID.write(i)

    if token == 0:
        print("ID not found please try again")

