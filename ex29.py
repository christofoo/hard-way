people = 20 
cats = 30
dogs = 15


if people < cats: 
    print "Too many cats! The world is doomed!"

if people > cats: 
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs: 
    print "The world is dry!"
#the one I added for the exercise
if people != dogs:
    print "Dog-people equality does not exist!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs: 
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# Study Drill
#What do you think the if does to the code under it?
# if runs the code below if the condition is true
#Why does the code under the if need to be indented four spaces?
# because it is reliant on the if condition
#What happens if it isn't indented?
# an error saying it expects an indent
#Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
# yes. I tried it. line 18.
#What happens if you change the initial values for people, cats, and dogs?
# different strings will print dependant on the values in the variables based on the conditions in the if statement