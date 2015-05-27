import re

class HTTPRequest:

    timeRegex = '\d\d:\d\d:\d\d'
    reqTime = '00:00:00'

    def __init__(self, reqString):
        self.reqString = reqString
        self.parseHTTPReqTime(reqString)

    def parseHTTPReqTime(self, line):
        result = re.search(self.timeRegex, line)
        if result:
            self.reqTime = result.group(0)
        else:
            print("Invalid HTTP Request - no time found")

    def getHour(self):
        return self.reqTime.split(":")[0]