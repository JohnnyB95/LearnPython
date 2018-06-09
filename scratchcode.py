#johnny's coding scratch pad

#IMPORT LIBRARIES
from sys import argv

#DEFINE FUNCTIONS HERE
def hello (world):
	print("input: %r") % world
	world=world+'Johnny'
	return(world)

#MAIN CODE
script, command = argv

print "welcome master"
print "SCRIPT: %r" % script
print "COMMAND: %r" % command

command = hello(command)
print command


