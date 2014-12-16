class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):
#this is the key piece in this mo'fugga
    def __init__(self):
        #see that smooth ass shit? 
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()
