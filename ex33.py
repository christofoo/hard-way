#creates an empty list called numbers
numbers = []
#prints a string
print "what number do you wanna start at?"
#asks for user input with prompt
startat = raw_input("> ")
#string that prints
print "pick a number you want to end at"
#variable hi set to raw input from user
hi = raw_input("> ")
#string that prints
print "pick the increment you want it to go up by"
#variable set to raw input
upby = raw_input("> ")
#creates new function hi_loop
def hi_loop(a, b):
    #defines value of i as 0
    i = 0
    #condition for i in while loop
    while i < a:
        #prints a string with a conversion
        print "At the top i is %d" % i 
        #adds the value 'i' to the tail end of the list
        numbers.append(i)
#increments i by the variable argument b
        i += b
        #prints the list
        print "Numbers now: ", numbers
        #prints a string and the value of i
        print "At the bottom i is %d" % i
#creates a new function
def alt_loop(a, b, c):
    #makes i zero
    i = 0
    #for loop with range conditions a,b,c based on function arguments
    for i in range(a, b, c):
        #string with a conversion that prints i
        print "At the top i is %d" % i 
        #appends the list with the new i value
        numbers.append(i)
        # prints a string and the list 'numbers'
        print "Numbers now: ", numbers
        #prints a string and the value of i 
        print "At the bottom i is %d" % i

#runs the function alt_loop with the raw_input strings converted to integers
alt_loop(int(startat), int(hi), int(upby))
#runs the function hi_loop
#hi_loop(int(hi), int(upby))
#prints a string
print "The numbers: "
#for loop that creates variable num that names the numbers in the numbers list
for num in numbers: 
    #prints the list
    print num


#1Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
#2Use this function to rewrite the script to try different numbers.
#3Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
#4Rewrite the script again to use this function to see what effect that has.
#5Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?