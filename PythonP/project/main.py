#1180729 mahmoud
#1190279 basel
import os

from option1 import *
from option2 import *
from option3 import *
from option4 import *
from option4proxy import *
import matplotlib.pyplot as plt
import numpy as np


#we made 3 classes, 1 parent and 2 childs, each class inherted attributes
# and we added some new ones
class person:
    def __init__(self, ID):
        self.ID = ID

    def statistics(self):
        print("undefiend")


class admin(person):
    def __init__(self, ID,):
        self.ID = ID

    def addStudent(self,file):
        addStudentRecord(file)

    def addSemster(self,x):
        addSemToStudent(x)

    def update(self):
        updateMark()

    def statistics(self):
        ID = input("please enter the student ID:")
        statProxy(ID)

class student(person):

    dictAvgPerSem = 0
    totalAvg = 0
    dictAvgHourPerSem = 0
    totalHours = 0
    RemainCourses = 0
    PassedCourses = 0
    #def __int__
    def __init__(self, ID):
        self.ID = ID
    def statistics(self):
        r = stati(self.ID);
        #statProxy(self.ID)
        self.dictAvgPerSem = r[1]
        self.totalAvg = r[2]
        self.dictAvgHourPerSem = r[3]
        self.totalHours = r[4]
        self.RemainCourses = r[5]
        self.PassedCourses = r[6]

    def PrintStatistics(self):
        print("Avg per semester:")
        print(self.dictAvgPerSem)
        print("total avg:")
        print(self.totalAvg)
        print("avg hours per semester:")
        print(self.dictAvgHourPerSem)
        print("total hours:")
        print(self.totalHours)
        print("remaining courses:")
        print(self.RemainCourses)
        print("passed courses:")
        print(self.PassedCourses)


#function to keep track of the students obj, total avg and hours
def getAllStudents(StudentAll):
    FStudents = open("data.txt")
    IDstudents = FStudents.readlines();
    #print(IDstudents)
    tempG = 0
    tempH1 = 0
    tempH2 = 0
    cG = 0
    cH = 0
    global globalAvg
    global globalHours
    global globalHoursP
    for k in IDstudents:
        #print(k)
        temp = k.split("\n")
        a = student(temp[0])
        StudentAll.append(a)
        a.statistics()
        tempG = tempG + a.totalAvg
        tempH2 = tempH2 + a.totalHours
        cG = cG + 1
        for j in a.dictAvgHourPerSem:
            tempH1 = tempH1 + a.dictAvgHourPerSem[j]
            cH = cH + 1
    if cG != '0' or cH != '0':
        globalAvg = tempG / (cG)
        globalHours = tempH1 / (cH)
        globalHoursP = tempH2 / (cG)

    FStudents.close()

tokenP = 0;
tokenS = 0;
FStudents = open("data.txt")
FProf = open("prof.txt")
IDstudents = FStudents.readlines();
IDprof = FProf.readlines();
StudentAll = []
while True:
    StudentAll.clear()# to track the students
    getAllStudents(StudentAll)
    login = input("please enter ur ID, if u want to quit enter q:")
    if login == 'q':
        exit()
    for k in IDprof:
        temp = k.split("\n")
        if login == temp[0]:
            while True:
                a = admin(login)
                tokenP = 1
                print("admin is logged in:")
                print("please choose one of the following options:")
                print("1) add a new student.")
                print("2) add a new semester for a student.")
                print("3) update a student record.")
                print("4) find a student statistics.")
                print("5) global statistics.")
                print("6) search.")
                print("anything else to logout.")
                print()
                option = input("please enter ur choice:")
                if option == '1':
                    file = input("student id: ")  # take the new id
                    a.addStudent(file)
                    while True:
                        print("please enter a semester, a student without a semester is not acceptable:")
                        a.addSemster(file)
                        f = file + ".txt"  # make it a string
                        filesize = os.path.getsize(f)
                        if filesize != 0:
                            break
                elif option == '2':
                    ID = input("please enter the student ID u desire to add a semester to:")
                    a.addSemster(ID)
                    StudentAll.clear()  # to track the students
                    getAllStudents(StudentAll)
                elif option == '3':
                    a.update()
                    StudentAll.clear()  # to track the students
                    getAllStudents(StudentAll)
                elif option == '4':
                    a.statistics()
                elif option == '5':
                    print("global students Avg:"+str(globalAvg))
                    print("global students hours per semester:"+str(globalHours))
                    dict = []
                    for obj in StudentAll:
                        dict.append(obj.totalAvg)
                    plt.hist(dict)
                    plt.show()
                elif option == '6':
                    print("you want to search based on what?")
                    print("1) Avg.")
                    print("2) hours passed")
                    criteria = input("please enter the criteria:")
                    print("and the search should follow which formula?")
                    print("1) greater, 2) less, 3) equal")
                    gle = input("what is the search formula?")
                    if criteria == '1':
                        inputA = input ("please enter the grade")
                        if gle == '1':
                            for obj in StudentAll:
                                if int(inputA) < int(obj.totalAvg):
                                    print(obj.ID)
                        elif gle == '2':
                            for obj in StudentAll:
                                if int(inputA) > int(obj.totalAvg):
                                    print(obj.ID)
                        elif gle == '3':
                            for obj in StudentAll:
                                if int(inputA) == int(obj.totalAvg):
                                    print(obj.ID)
                        else:
                            print("wrong input in formula")
                    elif criteria == '2':
                        inputB = input("please enter the grade")
                        if gle == '1':
                            if int(inputB) < int(obj.totalHours):
                                print(obj.ID)
                        elif gle == '2':
                            if int(inputB) > int(obj.totalHours):
                                print(obj.ID)
                        elif gle == '3':
                            if int(inputB) == int(obj.totalHours):
                                print(obj.ID)
                        else:
                            print("wrong input in formula")
                    else:
                        print("wring input in criteria")
                else:
                    break
            if tokenP == 1:
                break
    for k in IDstudents:
        temp = k.split("\n")
        if login == temp[0]:
            while True:
                a = student(login)
                tokenS = 1
                print("student login")
                print("please choose one of the following options:")
                print("1) student statistics.")
                print("2) global statistics.")
                print("anything else to logout.")
                option = input("please enter ur choice:")
                if option == '1':
                    a.statistics()
                    a.PrintStatistics()
                elif option == '2':
                    print("global students Avg:" + str(globalAvg))
                    print("global students hours per semester:" + str(globalHours))
                    dict = []
                    for obj in StudentAll:
                        dict.append(obj.totalAvg)
                    plt.hist(dict)
                    plt.show()
                else:
                    break
            if tokenS == 1:
                break

    if tokenS == 0 and tokenP == 0:
        print("unknown entry plz try again")
    tokenS = 0
    tokenP = 0


FStudents.close()
FProf.close()


