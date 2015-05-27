import sys
import urllib
from HTTPRequest import HTTPRequest

reqList = []
fileURL = "C:/Users/Ryan/Desktop/sdsc-http.txt" #Default URL

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " filename.txt\n")
else:
    fileURL = sys.argv[1]
    print("File set to: ", sys.argv[1])

fobj = open(fileURL, "r")
for line in fobj:
    reqList.append(HTTPRequest(line))

currentHour = "00"
currentHourReqCount = 0

for req in reqList:
    if req.getHour() == currentHour:
        currentHourReqCount += 1
    else:
        print("Hour " + str(currentHour) + ": " + str(currentHourReqCount) + " requests")
        currentHour = req.getHour()
        currentHourReqCount = 1
print("Hour " + str(currentHour) + ": " + str(currentHourReqCount) + " requests")

print("Total Requests: " + str(len(reqList)))

fobj.close()

