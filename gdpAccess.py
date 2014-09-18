import pexpect
import sys
import time
from subprocess import call

class GDP:

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def start(self):
        call(['/home/alex/Cs/Swarm/ble/startGDP'])

    def stream(self):
        gdpCon = pexpect.spawn(self.path + 'apps/writer-test ' + self.name)
        return gdpCon
