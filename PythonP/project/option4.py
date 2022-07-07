

def stati(ID):

    result = []
    # a list that will have the results, r[0] is avg per sem dict
    # r[1] will have the total avg
    # r[2] will have avg hour per semester
    # r[3] will have total hours
    # r[4] will have remaining courses
    # r[5] will have passed courses
    ID = str(ID)
    file = open("data.txt")  # open the data file to check if the student is there
    fileEncs = open("ENCS.txt")  # open the file for all courses in the student plan
    ReqCourses = fileEncs.readlines()  # read the courses
    ReqClist = ReqCourses[0].split(",")  # split the courses and put them in a a list
    contents = file.readlines()  # get all the ids in data file
    token = 0  # used to check the ids
    RemainCourses = []  # courses remaining, a list with all the courses remaining
    PassedCourses = []  # courses passed, a list with all the passed courses
    AvgPerSemester = []  # avg marks per semester, for each entered semester
    AvgHoursPerSemester = []  # avg hour per semester, for each entered semester
    dictAvgPerSem = {}  # dict semesters, to keep track of the semesters and the corresponding avg
    dictAvgHourPerSem = {}  # to keep track of the semesters and the corresponding hours
    tempAvgSem = 0
    tempAvgHoursSemester = 0
    totalHours = 0  # total hours passed
    SemList = []  # to keep a track of semesters

    for i in contents:
        temp = i.split("\n")  # temp now has the value of id
        if ID == temp[0]:  # if id is there
            token = 1  # token 1
            #print("student was found")
            f = ID + ".txt"
            fID = open(f, 'r+')
            semesters = fID.readlines()  # open the student file and get its contents
            sem = len(semesters) + 1
            for j in semesters:  # lines in the students file
                x = j.split(";")
                SemList.append(x[0])  # keeping count of the semesters
                y = x[1].split(",")  # take the each course and the mark alone
                cor = len(y)  # number of courses for avg
                for k in y:  # courses in the lines
                    z = k.split()  # gives courses in z[0] and mark in z[1]
                    # to calculate avg per sem and avg hour per sem
                    temp1 = z[1].split("\n")
                    tempAvgSem = tempAvgSem + int(temp1[0])
                    tempAvgHoursSemester = tempAvgHoursSemester + int(z[0][5])
                    # ----------
                    # to get the passed courses
                    for l in ReqClist:
                        if l == z[0]:
                            PassedCourses.append(l)
                            break
                # avg per semester
                AvgPerSemester.append(tempAvgSem / cor)
                # avg hours per sem
                AvgHoursPerSemester.append(tempAvgHoursSemester / cor)
                totalHours = totalHours + tempAvgHoursSemester
                tempAvgSem = 0
                tempAvgHoursSemester = 0
                # ------------------

    if token == 0:
        print("student was not found, wrong ID entered")
        result.append(token)
        return result
    else:  # we have student, we can return now
        result.append(token)
        # gives the remaining courses
        for ll in ReqClist:
            if ll not in PassedCourses:
                RemainCourses.append(ll)
        # print(RemainCourses)
        # print(PassedCourses)
        iii = 0
        #  -------------avg per semester, overall avg avgper sem (sum)/num
        #  to get semester:Avg
        for ii in SemList:
            dictAvgPerSem[ii] = AvgPerSemester[iii]
            iii = iii + 1
        #  print(dictAvgPerSem)
        #  -------------------------
        #  to get total avg
        totalAvg = 0
        tempAvg = 0
        for ix in SemList:
            tempAvg = tempAvg + float(dictAvgPerSem[ix])
        totalAvg = tempAvg / len(dictAvgPerSem)
        #print(totalAvg)
        #  ---------------avg hours per semester
        lll = 0
        for ll in SemList:
            dictAvgHourPerSem[ll] = AvgHoursPerSemester[lll]
            lll = lll + 1
        #  print(dictAvgHourPerSem)
        #  print(totalHours)

        dictc1 = dictAvgPerSem.copy()
        result.append(dictc1)
        result.append(totalAvg)
        dictc2 = dictAvgHourPerSem.copy()
        result.append(dictc2)
        result.append(totalHours)
        result.append(RemainCourses)
        result.append(PassedCourses)

    return result



