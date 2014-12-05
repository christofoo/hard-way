print "You enter a dark room with two doors. Do you go through door #1, door #2, door #3, or door #4?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jellow. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You enter a green field full of beautiful women. What do you do?"
    print "1. Cringe and mutter to yourself"
    print "2. Pretend you have somewhere very important to go and keep walking confidently."
    print "3. Start crying"
    print "4. Introduce yourself and compliment a lady"

    pickup = raw_input("> ")

    if pickup == "2" or pickup == "4":
        print "The ladies are impressed and want your pregnant."
    else: 
        print "The ladies look at you strangely and with their fingers and their thumbs make the shape of an L on their foreheads"

elif door == "4":
    print "You arrive at Sky Harbor International Airport. What do you do?"
    print "1. Take a private jet to Dubai"
    print "2. Take the next flight leaving at gate 2"
    print "3. Take the next flight elaving at gate 3"

    gate = raw_input(">")

    if gate == "1":
        print "Upon takeoff, the jet turns into a magic carpet and you are on a magic carpet ride to Dubai, my friend"
    else:
        print "The wait at the gate makes you irate because the plane is late and it would be great to have a plate but you can't sate, mate."


else:
    print "You stumble around and fall on a knife and die. Good job!"



