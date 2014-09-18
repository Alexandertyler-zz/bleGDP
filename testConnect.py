#!/usr/bin/env python
# Michael Saunby. April 2013
#
# Notes.
# pexpect uses regular expression so characters that have special meaning
# in regular expressions, e.g. [ and ] must be escaped with a backslash.
#
#   Copyright 2013 Michael Saunby
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import pexpect
import sys
import time
from sensor_calcs import *
import json
import select
import gdpAccess

gdp = gdpAccess.GDP("test", "/home/alex/Cs/Swarm/ble/gdp/")


con = pexpect.spawn('gatttool -b ' + sys.argv[1] + ' --interactive')
result = con.expect('\[   \]\[34:B1:F7:D5:10:81\]\[LE\]>', timeout=600)
print "Result is: ",result

con.sendline('connect');
#result = con.expect( 
con.sendline('disconnect')
print "Disconnected"
con.sendline('exit')
print "Exited"

