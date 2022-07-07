from option4 import *

def statProxy(ID):
    r = stati(ID)
    if r[0] == 1:
        print("Avg per semester:")
        print(r[1])
        print("total avg:")
        print(r[2])
        print("avg hours per semester:")
        print(r[3])
        print("total hours:")
        print(r[4])
        print("remaining courses:")
        print(r[5])
        print("passed courses:")
        print(r[6])
