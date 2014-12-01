#imports the module argv from sys
from sys import argv
# asks terminal for script and filename for argv to work
script, filename = argv
#prints a string with a conversion based on variable "filename"
print "We're going to erase %r." % filename
#prints a string
print "If you don't want that, hit CTRL-C (^C)."
#prints a string
print "If you do want that, hit RETURN."
#asks user for raw input (enter or ctrl c)
raw_input("?")
#prints a string
print "Opening the file..."
#calls the function of "open" with the parameters that it will be calling the variable "filename" and using "w" for writing, which truncates file. All this is named "target"
target = open(filename, 'w')
#prints a string
print "Truncating the file. Goodbye!"
# truncate function is called on "target" with no size argument present so the size defaults to the current position whatever that means
target.truncate()
#prints a string
print "Now I'm going to ask you for three lines."
#asks for raw input with a prompt and assigns it to the variable "line1"
line1 = raw_input("line 1: ")
#asks for raw input with a prompt and assigns it to the variable "line2"
line2 = raw_input("line 2: ")
# ditto but line3
line3 = raw_input("line 3: ")
#prints a string
print "I'm going to write these to the file."
#uses the "target" function (opens test.txt with write) and uses the "write" function on it to input whatever was inputted for the variables "line1" "line2" and "line3"
target.write("%s \n %s \n %s \n" % (line1, line2, line3))
#inputs a new line in the test.txt file
#target.write("\n")
# uses the "target" function (opens test.txt with write) and uses the "write" function on it to input whatever was inputted for the variable "line2"
#target.write(line2)
#inputs a new line in the test.txt file
#target.write("\n")
#ditto from before except line 3
#target.write(line3)
#inputs a new line in test.txt file
#target.write("\n")
#prints a string in the terminal output
print "And finally, we close it."
#closes the "target" file, which in this case is test.txt
target.close()

