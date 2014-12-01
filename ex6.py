# this is a string with an integer conversion that is defined outside the string as 10
x = "There are %d types of people." % 10
# this is a string that is named binary
binary = "binary"
# this is a string named do_not
do_not = "don't"
# this is a string with two string conversions in it that mean binary and do_not, respectively
y = "Those who know %s and those who %s." % (binary, do_not)
# this is a command to print the contents of the variable x
print x
# this is a command to print the contents of the variable y
print y
# this is a command to print a string with an r conversion defined as the contents of x
print "I said: %r." % x
# this is a command to print a string with a string conversion that is defined as the contents of y outside said string
print "I also said: '%s'." % y
# this is a line that gives False the name hilarious
hilarious = False
# this is a line that gives a string phrase with an r conversion the name "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! %r"
# this is a command that prints the contents of joke_evaluation with the r conversion defined as the contents of the variable name hilarious
print joke_evaluation % hilarious
# this is a string that is named the variable w
w = "This is the left side of..."
# this is a string that is named the variable e
e = "a string with a right side."
# this is a command to print the contents of both the variable w and e
print w + e