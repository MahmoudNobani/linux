import os
import re  # to use regex


def addSemToStudent(ID):
    token = 0
    counter = 0

    file = open("data.txt")
    contents = file.readlines()
    for k in contents:  # to check if the student is there
        temp = k.split("\n")  # temp now has the value of id
        if ID == temp[0]:
            token = 1
            print("ID found")
            print("please enter year and semester and the courses and the grades")
            print("please follow the following format")
            info = input("year-year/semester ; course((ENCS/ENEE)+(COURSEnum)) grade(two digits), course grade\n:")
            x = info.split(";")
            # using regex to check if the format is correct
            courses = x[1].split(",")
            pattern1 = '^\d\d\d\d-\d\d\d\d/[1-2]'
            pattern2 = ' EN[C/E][S/E]\d\d\d\d \d\d'
            match1 = re.search(pattern1, x[0])
            # if we have a match in the semseter part, we go to the courses
            if match1:  # now we check for a match in courses, if there is a match inc counter
                for i in range(len(courses)):
                    match2 = re.search(pattern2, courses[i])
                    if match2:
                        counter = counter + 1
                    else:
                        print("there is problem with the entered format of courses")
                        break
            else:
                print("the entered year format is false please try again")
                break
            # to check if our counter got the right values, if it did we can enter the new semester
            if counter == len(courses):
                f = ID + ".txt"
                IDfile = open(f, "a")
                filesize = os.path.getsize(f)
                if filesize != 0:
                    IDfile.write("\n" + info)
                else:
                    IDfile.write(info)
                IDfile.close()
                print("semseter added")
            else:
                print("please try again")

    if token == 0:
        print("student was not found, wrong ID entered")

    file.close()
