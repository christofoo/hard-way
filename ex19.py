# this makes a function called "cheese_and_crackers" that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #this prints a string with the d conversion format which is typically a number
    print "You have %d cheeses!" % cheese_count
    #this prints a string with d conversion format for a number defined by the "boxes_of_crackers variable"
    print "you have %d boxes of crackers!" % boxes_of_crackers
    #this prints a string
    print "Man that's enough for a party!"
    #this prints a string and new line
    print "Get a blanket. \n"

#this prints a string
print "We can just give the function numbers directly:"
#this prints a block string based on the function "cheese_and_crackers" created above
cheese_and_crackers(20, 20)

#this prints a string
print "OR, we can use variables from our script:"
#this defines a variable setting it as 10
amount_of_cheese = 10
# names a variable
amount_of_crackers = 50

#uses the variables from the script as the numbers for the "cheese_and_crackers" function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#this prints a string
print "We can even do math inside too:"
#this uses equations for the number arguments in the "cheese_and_crackers" function
cheese_and_crackers(10+20, 5+6)

#this prints a string
print "And we can combine the two, variables and math:"
#this uses an equation combining variables and integers to fill the arguments for our "cheese_and_crackers" function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

