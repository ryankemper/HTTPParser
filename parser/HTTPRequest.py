import re

class HTTPRequest:

    timeRegex = '\d\d:\d\d:\d\d'
    reqString = ""
    reqTime = '00:00:00'
    validRequest = False

    def __init__(self, reqString):
        self.reqString = reqString
        self.parseHTTPReqTime(reqString)

    def parseHTTPReqTime(self, line):
        result = re.search(self.timeRegex, line)
        if result:
            self.reqTime = result.group(0)
            self.validRequest = True
        else:
            print("Invalid HTTP Request - no time found for " + self.reqString)

    def getHour(self):
        return self.reqTime.split(":")[0]

    def getReqString(self):
        return self.reqString

    def isValidRequest(self):
        return self.validRequest