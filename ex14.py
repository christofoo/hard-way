#imports the argv module
from sys import argv
# gives the argument names that must be entered to run script in terminal
script, user_name, questiontype = argv
# creates prompt so everything is uniform prompt-wise
prompt = 'answerhere> '
# these print a string with the conversion variables that are defined outside the string
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few %s questions." % (questiontype)
print "Do you like me %s?" % user_name
# this asks user for raw input and names it "likes". Also, it uses the 'prompt' we set up earlier
likes = raw_input(prompt)
#this prints a string with the conversion defined as whatever user_name is
print "Where do you live %s?" % user_name
# this asks user for raw input and calls it lives
lives = raw_input(prompt)
#this prints a string 
print "What kind of computer do you have?"
# this asks user for raw input and calls it 'computer'
computer = raw_input(prompt)
#this prints a long string with conversions that are pulled from variables defined outside the string
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
