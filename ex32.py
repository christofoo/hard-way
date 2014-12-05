#hairs = ['brown', 'blond', 'red']
#eyes = ['brown', 'blue', 'green']
#weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type %s" % fruit

#also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i 

# we can also build lists, first start with an empty one
elements = []


#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i 
    # append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print "Element was: %d" % i 

#1. Take a look at how you used range. Look up the range function to understand it.
# Range asks for a stop argument or both start and stop or start, stop and a multiple. (they call multiple 'step')
# Range: If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0
#Range: it will return a list up to the highest number available before the designated "stop" point
# Range: it does not inlude the "stop" number. That is why our range (0, 6) does not include 6. 
#2. Could you have avoided that for-loop entirely on line 26 and just assigned range(0,6) directly to elements?
#I tried doing this by commenting out the whole block and adding .range(0, 6) as a function to elements
#tried a new variable value for elements
#tried adding elements.append(i) to line 34. Basically if it's possible, I wasn't able to do it.
#3. Find the Python documentation on lists and read about them. What other operations 
#>can you do to lists besides append?

# .extend(L) appends all the items in the given list 
# list.insert(i,x) inserts an item at a specific position
# .remove(x) removes the first instance of x in a list. error if no x present
# .pop([i]) removes the (optional) i from the list and returns it. If i not chosen it will remove the last item
# and return that
#.index(x) returns the index in the list of the first item whose value is x
#.count(x) return the number of times x appears in the list
# .sort(cmp=None, key=None, reverse=False) sort the items of the list in place( the arguments can be used for sort 
#customization, see sorted() for their explanation).
#.reverse() revesrse the elements of the list, in place. 

#explanation of sorted():
# sorted(iterable[,cmp[,key[,reverse]]])
# return a new sorted list from the items in iterable
#the optional arguments cmp, key, and reverse have the same meaning as those for the list.sort() method
# cmp specifies a custom comparison function of two arguments (list items) which should return a negative
# , zero, or positive number depending on whether the first argument is considered smaller than, equal to, or larger
# than the second argument: cmp=lambda x,y: cmp(x.lower(), y.lower()). The default value is None.
#key specifies a function of one argument that is used to extract a comparison key from each list element:
# key=str.lower. the default value is None
# reverse is a boolean value. if set to True, then the list elements are sorted as if each comparison were reversed. 
