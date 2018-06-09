#add module
from sys import argv

#assign variables to the inputs
script, filename = argv

#open file
txt = open (filename)

#print
#print "Here's your file %r:" % filename
#print txt.read() #print file contents

#ask for the file again and print
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print txt_again.fileno()
print txt_again.close()
