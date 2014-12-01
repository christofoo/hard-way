# this sets the variable "cars" to mean 100 when called
cars = 100
# this sets the variable "space_in_a_car" to mean the float number 4.0 when called
space_in_a_car = 4.0
#this sets the variable "drivers" to mean 30 when called
drivers = 30
# this sets the variable "passengers" to mean 90 when called
passengers = 90
# this sets the name of "cars - drivers" to be "cars_not_driven"
cars_not_driven = cars - drivers
# this sets the name of "drivers" to be "cars_driven"
cars_driven = drivers
# this sets the name of "cars_driven * space_in_a_car" to be "carpool_capacity"
carpool_capacity = cars_driven * space_in_a_car
# this means that average_passengers_per_car is the name of "passengers / cars_driven"
average_passengers_per_car = passengers / cars_driven

# this line prints text and then a variable and then text again
print "there are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
