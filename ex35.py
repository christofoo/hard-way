from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
#Haven't dealt with this yet but it probably means while the above content is True
    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")
# this is new. I think 'in' does a search of the raw input string from choice for the word 'flee' in this case
    if "flee" in choice:    
        start()
        #same as before except 'head'
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def space_room():
    print "YOU CLIMB TO OUTER SPACE"
    print "You see all sorts of aliens"
    print "One of the aliens is alf"
    print "Alf is about to eat a cat"
    print "What do you do?"

    choice = raw_input("> ")
    if "save" in choice:
        print "You saved the cat from certain doom. Alf dies of hunger."
        print "Now you get to go to the bear room"
        bear_room()
    if "eat" in choice:
        print "You sit down and eat Alf as he eats the cat."
        print "Alf is delicious. You leave outer space"
        start()
    else:
        print "I don\'t know what you mean!"


def hell():
    print "You climb into the depths of hell"
    print "You see Satan and a demon child"
    print "Satan asks you if you like what he's done with the place"
    print "You notice that it\'s pretty nice, there's a fountain and some house plants"
    print "what do you do next?"
    satan_pleased = False
    while True: 
        choice = raw_input("> ")
        if "compliment" in choice and not satan_pleased:
            print "Satan smiles and then starts crying. He then says thank you and allows you to leave"
            print "Go up now, boy while you have a chance"
            satan_pleased = True
        elif "up" in choice and satan_pleased:
            start()
        elif "kick" in choice and satan_pleased:
            print "Hey I gave you a chance. Now you get to be my slave"
            dead("you die from slavery")
        elif "kick" in choice: 
            print "Satan stabs you in the face with his eyes"
            dead("you are dead from face-stabbings")
        else:
            print "Whatchu sayy?"
            

def dead(why):
    print why, "Good job!"
    #this is probably from the module exit that we imported. It exits the program I guess
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left. Also there's a trapdoor beneath you (down) and a ladder up"
    print "Which way you gonna go, son?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "up":
        space_room()
    elif choice == "down":
        hell()
    else:
        dead("You stumble around the room until you starve.")

start()


#Draw a map of the game and how you flow through it.
#
#Fix all of your mistakes, including spelling mistakes.
# I DON'T MAKE MISTAKES
#Write comments for the functions you do not understand.
# in or and exit were new. but its not that i don't understand them, I found them to be self-explanatory
#Add more to the game. What can you do to both simplify and expand it?
#
#The gold_room has a weird way of getting you to type a number. What are all the 
#bugs in this way of doing it? Can you make it better than what I've written? Look at how int() 
#works for clues.
