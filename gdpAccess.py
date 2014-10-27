import pexpect
import sys
import time
import urllib
import urllib2
import json
from subprocess import call

class GCL:
    baseURI = "http://localhost:8008/gdp/v1/gcl"
    gdpPath = ""
    gcl_name = ""

    def __init__(self, gcl_name):
        self.gcl_name = gcl_name

    """def __init__(self, gcl_name, baseURI):
        self.gcl_name = gcl_name
        self.baseURI = baseURI
"""
    #only need this while running from a local machine
    def startServer(self):
        call(['/home/alex/Cs/Swarm/ble/startGDP'])

    #sets up a shell for using writer-test, not needed
    #returns a pexpect object
    def writerTest(self):
        gdpCon = pexpect.spawn(self.gdpPath + 'apps/writer-test ' + self.devName)
        return gdpCon

    def getGCL(self):
        #if (self.gcl_name is not ""):
            #print "GCL is already initialized."
            #return
        req = urllib2.Request(self.baseURI)
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, "")
        returnJson = response.read()
        decoded = json.loads(returnJson)
        print "GCL_name is " + decoded["gcl_name"]
        #self.gcl_name = decoded["gcl_name"]
        return decoded["gcl_name"]


    #value must be a string
    def gdpPOST(self, value):
        print "Posting"
        url = self.baseURI + "/" + self.gcl_name
        data = { "value" : value }
        print url
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(data))
        print response
        return response 
