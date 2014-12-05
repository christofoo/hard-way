#makes ten_things a string
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#prints a string
print "Wait there are not 10 things in that list. Let's fix that."
#.split split all the words into individual strings from the one long one
stuff = ten_things.split(' ')
#this is a list 
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#while loop. while the number of items in list does not exceed 10. 
#the block as a whole takes an item from the end of more_stuff and adds it to stuff until it has 9 items
while len(stuff) != 10:
    #.pop removes item from list and returns it
    next_one = more_stuff.pop()
    #string and next_one
    print "Adding: ", next_one
    #adds next_one to stuff
    stuff.append(next_one)
    #string and length of stuff
    print "There are %d items now." % len(stuff)
#string and stuff equaling 9 items
print "There we go: ", stuff
#string
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #fancccyyy
print stuff.pop()
print ' '.join(stuff) # ya
print '#'.join(stuff[3:5]) #super stellar!


