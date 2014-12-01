#names string thats tabbed
tabby_cat = "\tI'm tabbed in."
#names a string thats split on a line
persian_cat = "I'm split\non a line."
#names a string that has slashes in it
backslash_cat = "I'm \\ a \\ cat."
#names a long string that has stars in it and uses a \t for some reason. probably because * usually means multiply
fat_cat = '''
I'll do a list:
\t* "Cat" food 
\t* Fishies
\t* Catnip\n\t* Grass
'''
# line I wrote that escapes for the double quotes to be within double quotes
dead_cat = "I am \"un\"dead"
# line I wrote to see how escape single quotes work within single quotes that also have conversions in them
angel_cat = ' I am \' %r \' neither alive \'nor\' \' %s \' dead' 
#prints tabby_cat contents etc.
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print dead_cat 
print angel_cat % ("totally lying here", "don't believe my cat lies")


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
