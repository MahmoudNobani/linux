ID = input("please enter the student ID u desire to add a semester to:")
file = open("data.txt")
fileEncs = open("ENCS.txt")
ReqCourses = fileEncs.readlines()
ReqClist = ReqCourses[0].split(",")
contents = file.readlines()
token = 0
hours = 0  # hours remaining
RemainCourses = []  # courses remaining
PassedCourses = []  # courses passed
AvgPerSemester = []  # avg per semester
AvgHoursPerSemester = []  # avg hour per semester
dictAvgPerSem = {}  # dict semester
dictAvgHourPerSem = {}
tempAvgSem = 0
tempAvgHoursSemester = 0
totalHours = 0
SemList = []

for i in contents:
   # print(ID+ " " + i + " " + str(counter))
    temp = i.split("\n")
    if ID == temp[0]:
        token = 1
        print("student was found")
        f = ID + ".txt"
        fID = open(f, 'r+')
        semesters = fID.readlines()
        sem=len(semesters)+1
        for j in semesters: #lines
            x = j.split(";")
            SemList.append(x[0]) #keeping count of the semesters
            y = x[1].split(",")
            cor = len(y)
            #print(y)
            for k in y: #courses in the lines
                z = k.split() #gives courses in z[0] and mark in z[1]
                #print(z[0][5])
                # avg per sem
                temp1=z[1].split("\n")
                tempAvgSem = tempAvgSem + int(temp1[0])
                tempAvgHoursSemester = tempAvgHoursSemester + int(z[0][5])
                # ----------
                #print(z[0] + " " + z[1])
                for l in ReqClist:
                    #print(l+" "+z[0])
                    if l == z[0]:
                        PassedCourses.append(l)
                        break
            #avg per semester
            AvgPerSemester.append(tempAvgSem/cor)
            #avg hours per sem
            AvgHoursPerSemester.append(tempAvgHoursSemester/cor)
            totalHours = totalHours + tempAvgHoursSemester
            tempAvgSem = 0
            tempAvgHoursSemester = 0
            #------------------




#print("hey")
#whole avg 77.625
#avg per sem

if token == 0:
    print("student was not found, wrong ID entered")
else:
    for ll in ReqClist:
        if ll not in PassedCourses:
            RemainCourses.append(ll)
    # print(RemainCourses)
     # print(PassedCourses)
    iii=0
    #-------------avg per semester, overall avg avgper sem (sum)/num
    for ii in SemList:
        dictAvgPerSem[ii]=AvgPerSemester[iii]
        iii=iii+1
    print(dictAvgPerSem)
    #-------------------------
    totalAvg = 0
    tempAvg = 0
    for ix in SemList:
        tempAvg = tempAvg + float(dictAvgPerSem[ix])
    totalAvg=tempAvg/len(dictAvgPerSem)
    print(totalAvg)
    #---------------avg hours per semester
    lll = 0
    for ll in SemList:
        dictAvgHourPerSem[ll]=AvgHoursPerSemester[lll]
        lll = lll+1
    print(dictAvgHourPerSem)
    print(totalHours)


