# this imports the module argv from sys file
from sys import argv
# this asks the terminal for script and filename in that order before it can run this script as a result of argv
script, filename = argv
#stupid strings
print "OK YIPEE WE're GOING TO READ %r IN A SCRIPT I WROTE FROM SCRATCH" % filename
print "If you are morally opposed, please press CTRL-C"
print "If thats totes cool wit u, then just press ENTER!"
#asks for raw input... just enter or ctrl c in this case
raw_input("????")
#stupid string
print "LET's READ TOGETHER"
#creates variable "target" that uses the function "open" on the variable "filename" defined earlier
target = open(filename)
#bunch of dumb strings that mimic what ex16.py had jus because
print "I chose not to use truncate because we're not writing anything fool! We're just reading!"
print "I'm not going to ask for three lines because we're not writing!"
print "i'm not writing anything to a file, I'm just using read() without specifying a specific line or anything"
# i'm so happy I figured this one out. just had to set it to a variable since target.read on its own wont print anything
read = target.read()
#this prints the "read" variable contents
print read
#dumb string
print "and now we close it I guess"
#closed fo business. sexy job on this. splendid. smooshy gets a cookie
target.close()