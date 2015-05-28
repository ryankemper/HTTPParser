#!/usr/bin/env python3

import sys
from HTTPRequest import HTTPRequest

reqList = []
path = "../resources/sdsc-http.txt" # Default file location

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " filename.txt")
    print("Proceeding with default file location of " + path + "\n")
else:
    path = sys.argv[1]
    print("File set to: ", path)

try:
    fobj = open(path, "r")
except IOError:
    print("IO Error: ", sys.exc_info()[0])
except:
    print("Unexpected error: ", sys.exc_info()[0])

for line in fobj:
    reqList.append(HTTPRequest(line))

reqsByHour = {"00" : 0, "01" : 0, "02" : 0, "03" : 0, "04" : 0, "05" : 0, "06" : 0, "07" : 0, "08" : 0, "09" : 0,
              "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0,
              "20" : 0, "21" : 0, "22" : 0, "23" : 0}

for req in reqList:
    if req.isValidRequest():
        reqsByHour[req.getHour()] += 1

for x in range (0,3):
    for y in range (0, 10):
        if x >= 2 and y > 3:
            break
        hour = str(x) + str(y)
        print("Hour " + hour + ":  " + str(reqsByHour[hour]) + " requests")
print("Total Requests: " + str(len(reqList)))
fobj.close()