import re

class HTTPRequest:

    timeRegex = '\d\d:\d\d:\d\d'
    defaultTime = '00:00:00'

    def __init__(self, reqString):
        self.reqString = reqString
        self.reqTime = self.defaultTime
        self.validRequest = self.parseHTTPReqTime(reqString)

    def parseHTTPReqTime(self, line):
        result = re.search(self.timeRegex, line)
        if result:
            self.reqTime = result.group(0)
            return True
        else:
            print("Invalid HTTP Request - no time found for " + self.reqString)
            return False

    def getHour(self):
        return self.reqTime.split(":")[0]

    def getReqString(self):
        return self.reqString

    def isValidRequest(self):
        return self.validRequest
