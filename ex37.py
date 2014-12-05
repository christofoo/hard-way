#
#I'm going to write my explanation of what each symbol does beneath each line.
#
#KEYWORD    DESCRIPTION EXAMPLE
#and Logical and.    True and False == False

# combines two conditions or two variables. If something false is combined with it, its always false. 

#as  Part of the with-as statement.  with X as Y: pass

#had to look up... its used with with. It wraps the execution of a block with methods defined by a context manager... whatever that means

#assert  Assert (ensure) that something is true. assert False, "Error!"

# helpful for debugging. You can assert things as true to check different parts of code.

#break   Stop this loop right now.   while True: break

# stops a loop. skips else. for loops keep whatever value they were at. ends while loops. can be nested in there.

#class   Define a class. class Person(object)

#executable statement. inheritance runs first. works like a function. can be surrounded by decorators, whatever they do

#continue    Don't process more of the loop, do it again.    while True: continue

# keeps a loop going. it will go to the next cycle.

#def Define a function.  def X(): pass

# creates a new function. function can be run by calling it. Def itself doesn't run it. it can be outfitted with a decorator, whatever those do

#del Delete from dictionary. del X[Y]

#deletes from a dictionary. deleting a target's list will destroy everything in the list to the left and right of it. deleting a name removes the binding of the name from namespace

#elif    Else if condition.  if: X; elif: Y; else: J

# can be used as the next step after if is found false

#else    Else condition. if: X; elif: Y; else: J

# when a block doesn't meet the conditions of 'if', else is called to tell the app what to do next.

#except  If an exception happens, do this.   except ValueError, e: print e

# used in conjunction with 'try' statements which I haven't learned yet

#exec    Run a string as Python. exec 'print "hello"'

# converts exec statement into exec function. Executes some kind of argument

#finally Exceptions or not, finally do this no matter what.  finally: pass

# part of a "try" statement. finally does whatever after all the try crap happened

#for Loop over a collection of things.   for X in Y: pass

# creates a loop that goes through contents of the block

#from    Importing specific parts of a module.   import X from Y

# from tells what package to get the desired module from thats being imported

#global  Declare that you want a global variable.    global X

# defines what follows as being a global variable. I think that means its accessible from any file

#if  If condition.   if: X; elif: Y; else: J

# creates a conditional argument. if true, it executes next line or block below, if false, it goes to next step (elif or else)

#import  Import a module into this one to use.   import os

# followed by what module you want

#in  Part of for-loops. Also a test of X in Y.   for X in Y: pass also 1 in [1] == True

# can test if a variable is part of a collection. not in can be used too to negate

#is  Like == to test equality.   1 is 1 == True

# tests for object identity

#lambda  Create a short anonymous function.  s = lambda y: y ** y; s(3)

# a way to create an anonymous function

#not Logical not.    not True == False

# negates whatever follows

#or  Logical or. True or False == True

# combines concepts. if true is used with or at anytime, the line is true

#pass    This block is empty.    def empty(): pass

#can help a program move on by skipping an argument. maybe helpful for tests? or just having a null value for something

#print   Print this string.  print 'this string'

# string output

#raise   Raise an exception when things go wrong.    raise ValueError("No")

#has to do with exceptions. used for error messages

#return  Exit the function with a return value.  def X(): return Y

#leaves a function and provides content in the return

#try Try this block, and if exception, go to except. try: pass

#tries a block and if it doesn't work it goes to another block

#while   While loop. while X: pass

#creates a while loop that runs as long as the following variable is true

#with    With an expression as a variable do.    with X as Y: pass

#wraps a block with methods defined by context manager

#yield   Pause here and return to caller.    def X(): yield Y; X().next()

# used with generators to define a value

#
#TYPE   DESCRIPTION EXAMPLE



#True    True boolean value. True or False == True

# true allows the code to move to the next line

#False   False boolean value.    False and True == False

#boolean. 

#None    Represents "nothing" or "no value". x = None

# means no value

#strings Stores textual information. x = "hello"

# wordy words

#numbers Stores integers.    i = 100

#  integerrrss

#floats  Stores decimals.    i = 10.389

#decimalllllls

#lists   Stores a list of things.    j = [1,2,3,4]

#lissts in a loooonnng or short bracket set

#dicts   Stores a key=value mapping of things.   e = {'x': 1, 'y': 2}

#pulls a dictionary based on the arguments. positional arguments or keyword

#ESCAPE  DESCRIPTION EXAMPLE



#%d  Decimal integers (not floating point).  "%d" % 45 == '45'

# decimal integers. replaces with the called integer on the outside of the string

#%i  Same as %d. "%i" % 45 == '45'

# same as d... huh thats repetetive

#%o  Octal number.   "%o" % 1000 == '1750'

# uhhh makes an octal number... wtf...... computer sciencey shit goin on here

#%u  Unsigned decimal.   "%u" % -1000 == '-1000'

# unsigned decimal.... makes shit a string?

#%x  Hexadecimal lowercase.  "%x" % 1000 == '3e8'

# hexadecimal.... i think people use this for passwordy computer sciencey shit.

#%X  Hexadecimal uppercase.  "%X" % 1000 == '3E8'

# same shit but uppercase

#%e  Exponential notation, lowercase 'e'.    "%e" % 1000 == '1.000000e+03'

# turns a thing into exponential notation. now that I understand...

#%E  Exponential notation, uppercase 'E'.    "%E" % 1000 == '1.000000E+03'

# same shit but uppercase

#%f  Floating point real number. "%f" % 10.34 == '10.340000'

#turns shit into floating point which adds  a bunch of digits after decimal point

#%F  Same as %f. "%F" % 10.34 == '10.340000'

# same shit

#%g  Either %f or %e, whichever is shorter.  "%g" % 10.34 == '10.34'

# makes a smug little number

#%G  Same as %g but uppercase.   "%G" % 10.34 == '10.34'

# sams shiiiiiiiit

#%c  Character format.   "%c" % 34 == '"'

# uhh wtf

#%r  Repr format (debugging format). "%r" % int == "<type 'int'>"

# debug shit

#%s  String format.  "%s there" % 'hi' == 'hi there'

# stringgggg

#%%  A percent sign. "%g%%" % 10.34 == '10.34%'

#two percent signs is one percent sign

#OPERATOR    DESCRIPTION EXAMPLE



#+   Addition    2 + 4 == 6

# adding  blaaahhh i'm skipping this shit

#-   Subtraction 2 - 4 == -2



#*   Multiplication  2 * 4 == 8



#**  Power of    2 ** 4 == 16



#/   Division    2 / 4.0 == 0.5



#//  Floor division  2 // 4.0 == 0.0



#%   String interpolate or modulus   2 % 4 == 2



#<   Less than   4 < 4 == False



#>   Greater than    4 > 4 == False



#<=  Less than equal 4 <= 4 == True



#>=  Greater than equal  4 >= 4 == True



#==  Equal   4 == 5 == False



#!=  Not equal   4 != 5 == True



#<>  Not equal   4 <> 5 == True



#( ) Parenthesis len('hi') == 2



#[ ] List brackets   [1,3,4]



#{ } Dict curly braces   {'x': 5, 'y': 10}



#@   At (decorators) @classmethod

# have read the pydoc for this so many times but it never makes sense

#,   Comma   range(0, 10)



#:   Colon   def X():



#.   Dot self.x = 10



#=   Assign equal    x = 10



#;   semi-colon  print "hi"; print "there"



#+=  Add and assign  x = 1; x += 2



#-=  Subtract and assign x = 1; x -= 2



# *=  Multiply and assign x = 1; x *= 2



# /=  Divide and assign   x = 1; x /= 2



# //= Floor divide and assign x = 1; x //= 2

#floor divide? wtf

# %=  Modulus assign  x = 1; x %= 2

#yeah wtf..... idk what this means: Modulus AND assignment operator, It takes modulus using two operands and assigns the result to left operand
# is it just the remainder shit again but with the assignment operator? I guess I get it....



# **= Power assign    x = 1; x **= 2

#power assign!

