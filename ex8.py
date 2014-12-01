# this names the string of r conversions formatter
formatter = "%r %r %r %r"
# this prints formatter with the fills being integers
print formatter % (1, 2, 3, 4)
#this prints formatter with the conversions being strings
print formatter % ("one", "two", "three", "four")
#this prints the formatter with the conversion fills being true and false
print formatter % (True, False, False, True)
#this prints formatter with the fills being formatter which is the 4 %rs 4 times
print formatter % (formatter, formatter, formatter, formatter)
#this prints formatter with strings filling the r conversions
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
#no idea why this^ shows up as single quotes for the first two and last one. 