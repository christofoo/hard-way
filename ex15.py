# this line pulls the module argv from sys
from sys import argv
#this line tells what pieces are needed to enter on the terminal for argv
script, filename = argv
#this line names the function of opening the 'filename' we entered in the terminal for use later in printing
#txt = open(filename)
#this line prints a string with the conversion based on the filename entered in the terminal
#print "Here's your file %r:" % filename
#this line prints the txt variable with the read command given which tells the system to print whatever is in the text file without parameters
#print txt.read()
# this prints a new message to the user automatically that is a string
print "Type the filename again:"
# this is a variable that asks for a user's raw input and provides a prompt
file_again = raw_input("> ")
# this is a variable that is defined based on on the input from the previous line file_again, which it uses the open function on
txt_again = open(file_again)
#this line prints the contents of the previous line using the read command so the text comes with no parameters
print txt_again.read()

