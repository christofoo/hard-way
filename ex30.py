# means the integer 90 is called people
people = 90
#means the integer 10 is called cars
cars = 10
# means the integer 12 is called trucks
trucks = 12

#means if the variable cars is greater than people it will follow logic on the next line
if cars > people:
    #means a string will be printed
    print "We should take the cars."
    #means if the above conditional was not met and the variable cars is less than people then the next line of logic will run
elif cars < people:
    #means a string will print
    print "We should not take the cars."
    #means if the above 2 conditionals are not met the next line of logic will run
else:
    #means print the following string
    print "We can't decide."
#means if the variable trucks is greater than cars, follow the next line of logic
if trucks > cars:
    #means print the following string
    print "That's too many trucks."
    #means if the above conditional was not met, to try the new one, if the variable trucks is less than the value of variable cars, follow the next line's logic
elif trucks < cars: 
    #means print the string
    print "Maybe we could take the trucks."
    #means if the above 2 conditions were not met, then follow the logic on the next line
else:
    #means print the following string
    print "We still can't decide."
# means if the variable people is less than the value of the variable trucks, follow the next line's logic
if people > trucks:
    #means print the following string
    print "Alright, let's just take the trucks."
    #means if the conditional was not met, follow the next line of logic
else:
    #means print the string
    print "Fine, let's stay home then."
#means if cars variable is greater than people variable ORRR trucks variable is less than cars variable, follow next line of logic
if cars > people or trucks < cars:
    #means print the following string
    print "Ok there are either more cars than people or friggen less trucks than cars or both. I'm havin trouble keepin' this all straight in my \'ead"
# means if cars variable is less than the value of people variable or trucks var is more than the value of cars variable, follow next line of logic
elif cars < people or trucks > cars:
    #means print the string
    print "alright hold up everybody. We got less cars than people or there are more trucks than there are cars. either one of those. which... I can't tell ya. I'm a simple manputer"
#means if the conditions above are not met, follow next line of logic
else: 
    #means print the following string
    print "I'm not sure how its anything else"

# STUDY DRILLS
#Try to guess what elif and else are doing.
# elif means if the condition is different than the original if, try this new condition. Else means just run whatever it says if conditions from if and elif aren't met.
#Change the numbers of cars, people, and trucks and then trace through each if-statement to see what will be printed.
# did that and saw new strings printed based on the boolean logic
#Try some more complex boolean expressions like cars > people or trucks < cars.
#done
#Above each line write an English description of what the line does.
# WOOHOO