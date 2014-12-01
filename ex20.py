# this imprts argv module from system
from sys import argv
#this asks terminal for two pieces, script and input_file based on argv functionality
script, input_file = argv
#this creates a function called "print_all" with the argument "f" that prints the contents of f
def print_all(f):
    #prints contents of f
    print f.read()
#creates a function called "rewind" that asks for the argument "f"
def rewind(f):
    #this utilizes the "seek" function on arg f and harkens to read from the top of the file again 0 absolute file positioning
    f.seek(0)
#this creates a function called "print_a_line" that takes the arguments line_count and f
def print_a_line(line_count, f):
    #this prints the contents of line count argument entered and a specified line of variable f
    print line_count, f.readline()
#this defines the variable "current_file" as the function open being applied to the variable input_file
current_file = open(input_file)
#thie prints a string and a new line
print "First let's print the whole file: \n"
#this calls the function "print_all" and applies it to the contents of the variable "current_file"
print_all(current_file)
#this prints a string
print "Now let's rewind, kind of like a tape"
#this uses our function "rewind" on the variable "current_file" which starts reading the file from the top again
rewind(current_file)
#this prints a string
print "Let's print three lines:"
#this defines the variable "current_line" as 1
current_line = 1
#this calls the function "print_a_line" to print the contents of "current_line" as the first argument and the contents of the specified line in variable-file "current_file"
print_a_line(current_line, current_file)
#this redefines current_line to be the name of the existing "current_line" plus 1. in this case 2. 
current_line += 1
#this calls our function "print_a_line" with the newly defined current_line and uses that line to print the other argument, the second line of "current_file"
print_a_line(current_line, current_file)
#this redefines current_line to be the name of the existing "current_line" plus 1. in this case 3.
current_line += 1
#this calls our function "print_a_line" using the new "current_line" and that place in "current_file"
print_a_line(current_line, current_file)