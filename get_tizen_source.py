# This is a python script to download all source code from the git on webpage.  
# Commandline "git" must be installed.
#
# Usage:   $ python test.py URL
# Example: $ python test.py source.tizen.org/git/

import httplib
import sys
import re
import subprocess

# Check if git is installed
if (subprocess.check_call(['git', '--version']) != 0):
	print "Commandline 'git' isn't installed"
	exit()

# Check argument
argvs =  sys.argv
if (len(argvs) < 2):
	print 'Usage:   $ python', argvs[0], 'URL'
	print 'Example: $ python', argvs[0], 'source.tizen.org/git/'
	exit()

# Check connection to web
host = argvs[1][0:argvs[1].find("/")]
path = argvs[1][argvs[1].find("/"):]

if (path[0] != '/'):
	print "Given URL is invalid."
	exit()

print 'Connecting to', host, '...'

conn = httplib.HTTPConnection(host)
conn.request("GET", path)
res = conn.getresponse()

if (res.status != 200):
	print 'The server returns \"', res.status, res.reason, '\"'
	print 'Please check URL.'
	exit()

# Get all git repositories on page
pagesource = res.read()
pattern = re.compile(">[a-z|/].*\.git<")
repos = pattern.findall(pagesource)
conn.close()

if (len(repos) < 1):
	print "No git repository found."
	exit()

print len(repos), "git repositories found."

for l in repos:
	print "Executing 'git clone", "git://" + host + "/" + l[1:-1] + "'"
	subprocess.call(['git', 'clone', 'git://' + host + "/" + l[1:-1]])

