class Dog(object):
    def __init__(self, breed):
        pass

    def eat(self, kibble):
        self.bowl = 'black'







doggie = Dog('collie')
otherdog = Dog('dachound')

otherdog.eat('machokibble')


bone = 'glass'


doggie.bone = 'rubber'
doggie.bowl = 'red'

print doggie.bone
print otherdog.bowl

print "now it changes"

otherdog.bowl = 'fuscia'

print otherdog.bowl

