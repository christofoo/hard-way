# -*- coding: utf-8 -*-

# this is code I pulled from a file in Trevor's repo. Its for a messaging service.
#I'm going to try and understand it and describe what each piece means
#I'm not too savvy on classes yet so this may go terribly.

# This imports "absolute_import" module from the __future__ package
from __future__ import absolute_import
# this imports 'blinker' module and does not specify a package so it will search every package I think?
import blinker
# this imports 'cached_property' from the .decorators package
from .decorators import cached_property
# this imports NSQException from the .errors package
from .errors import NSQException

#this is a class definition with the argument 'object'
class Message(object):
    #this is a message about the class... the three quote marks are significant and I cant remember why
    #they're used typically to make a large block into a string
    # in this case its different and I think they make this message accessible when a certain function
    #is called on this class. I can't remember, but I think I went over this.
    #Ok yeah you use the attribute __doc__ and that will return the docstring
    """A class representing a message received from nsqd."""
    #this is a function definition for __init__ that takes 5 arguments
    def __init__(self, timestamp, attempts, id, body):
        #I think you call these instance variables because they are referring to 'self' which in this case is the class Message I believe
        self.timestamp = timestamp
        self.attempts = attempts
        self.id = id
        self.body = body
        self._has_responded = False
#decorator on cached_property
    @cached_property
    # creates 'on_finish' function with argument self. 
    def on_finish(self):
        #documentation
        """Emitted after :meth:`finish`.

        The signal sender is the message instance.
        """
        #returns 'blinker' with the 'Signal' function modifying it and an argument about doc equaling a string 
        #which I think changes the documentation?
        return blinker.Signal(doc='Emitted after message is finished.')
# another decorator on cached_property
    @cached_property
    # this creates the function 'on_requeue' with the argument 'self'
    def on_requeue(self):
        # this is the documentation for  the function
        """Emitted after :meth:`requeue`.

        The signal sender is the message instance and sends the `timeout` as an
        argument.
        """
        #this returns blinker with the 'Signal' function altering it and an argument about doc being a string
        return blinker.Signal(doc='Emitted after message is requeued.')
#another decorator on cached_property
    @cached_property
    #this makes the 'on_touch' function with the argument 'self'
    def on_touch(self):
        """Emitted after :meth:`touch`.

        The signal sender is the message instance.
        """
        # ditto, like the others
        return blinker.Signal(doc='Emitted after message is touched.')
# this creates the function 'has_responded' with the argument 'self'
    def has_responded(self):
        # this is a documentation string
        """Returns whether or not this message has been responded to."""
        #this returns self altered by the function _has_responded
        return self._has_responded
# this makes the function 'finish' and is used on the argument 'self'
    def finish(self):
        # this is a string for documentation
        """
        Respond to nsqd that you’ve processed this message successfully
        (or would like to silently discard it).
        """
        #this is a conditional about if 'self' has been alteed by the function _has_responded
        if self._has_responded:
            #this uses the 'raise' statement and calls NSQException with an expression 'already responded'
            raise NSQException('already responded')
            #this sets an instance variable equal to true saying the class has called the function _has_responded
        self._has_responded = True
        # this says that the class calls the functions '.on_finish' and '.send' with the argument 'self'
        self.on_finish.send(self)
#this makes a function called "requeue" with arguments 'self' and 'time_ms=0'
    def requeue(self, time_ms=0):
        #documentation string
        """
        Respond to nsqd that you’ve failed to process this message successfully
        (and would like it to be requeued).
        """
        # this is a conditional saying if the class has used the function '_has_responded' 
        if self._has_responded:
            # if the condition is met, this calls the 'raise' statement NSQException with the arg string 'already responded'
            raise NSQException('already responded')
            #this sets the class variable altered by the _has_responded function to true
        self._has_responded = True
        #this uses the 'on_requeue' and 'send' function with arguments 'self' and 'timeout' on the class variable self
        self.on_requeue.send(self, timeout=time_ms)
# this makes a new function called touch with argument self
    def touch(self):
        #this is a documentation string
        """Respond to nsqd that you need more time to process the message."""
        #this is a conditional statement reliant on if _has_responded function has altered self
        if self._has_responded:
            # this says to use the raise statement NSQException with the argument string 'already responded' if condition met
            raise NSQException('already responded')
            #this says the class will use the function 'on_touch' and 'send' with argument 'self'
        self.on_touch.send(self)