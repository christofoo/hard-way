# imports argv as a module for this script
from sys import argv
# names the variable entries for the argv
script, first, second, third = argv

#prints a prompt message
print "first variable?"
# requests the raw_input for the first variable. I don't know why I cannot print the message in the parentheses
first = raw_input()
# prints prompt question
print "second variable?"
# requests the raw_input for the second variable.
second = raw_input()
# prints prompt message
print "third variable?"
# requests the raw_input for the third variable.
third = raw_input()

#prints results of raw input
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
