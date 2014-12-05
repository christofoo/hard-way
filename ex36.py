from sys import exit

print "Welcome to the Legend of Zorldo"
print "You are the hero, Lonk"
print "Make money or get the Quadforce. Your Choice."
raw_input("")
print "You wake up in your treehouse. You are Lonk. The cute elvish warrior."

def start():
    print "You see a chest, a mirror and a ladder in the treehouse"
    print "Your move, cowboy."
    has_weapons = False
    chest_open = False
    while True:
        choice = raw_input("> ")
        if "mirror" in choice:
            print "You look like shit."
        elif "chest" in choice and not chest_open:
            print "You\'re going to have to try something else on that chest, maybe unlock it first?"
        elif "unlock" in choice and not chest_open:
            print "congratulations, Lonk. You unlocked your chest. 4389327 Experience points earned."
            print "I won\'t be keeping track of your points so you better write them down."
            raw_input()
            
            chest_open = True
        elif "chest" in choice and chest_open:
            print "You open the chest and find it contains a sword and shield"
        elif "sword" in choice or "shield" in choice and chest_open:
            print "You pick up the sword and shield. Congratulations Lonk. 45098 Experience awarded"
            has_weapons = True
        elif "ladder" in choice and not has_weapons:
            print "You can\'t climb down that ladder without getting your Hypoolian sword and shield."
        elif "ladder" in choice and has_weapons:
            print "Alright. You\'ve got your shit together now, Lonk. Go save Zorldo"
            raw_input()
            front_path()
def front_path():
    print "You get to the path in front of your treehouse where you live."
    print "Your treehouse looks awesome. You\'re pretty cool, Lonk"
    print "You see the path leads west, towards a lake of fire - south, towards a stupid house, - and east, towards a haunted house"
    print "Where to, Lonk?"

    choice = raw_input("> ")
    if "west" in choice:
        print "You walk into a lake of fire and jump right in. It\'s nice and hot"
        dead("You melt right into the lake. Pretty cool, Lonk.")
    elif "stupid" in choice:
        print "You start rolling towards the stupid house saying \'Hyah! Hyah! Hyah!\' over and over like a moron."
        raw_input()
        stupid_house()
    elif "haunted" in choice:
        print "You brandish your sword and shield and start running towards the haunted house." 
        raw_input()
        haunted_house()
    else:
        print "wtf?"

def stupid_house():
    print "You are standing in front of a stupid house"
    print "You made this choice and now you are here"
    print "The house has a doorbell and no door"
    print "There is a dog door, but it's on the second floor"
    print "You see a cray dog jump up to the second floor through the door so it works I guess"
    print "There is a window 3 feet left of the doorbell"
    print "Thats it besides 4 walls and a roof. It's definitely a stupid house"
    print "Ok what do you want to accomplish here?"

choice = raw_input("> ")

def haunted_house():
    print "WoooooooooOOOooOOOhhhh SpooOOOooOOoookyyyyYYYyy"
    print "You arrive in front of an eggplant-colored house."
    print "The house has GHOSTS coming out of every orifice."
    print "You immediately sheath your sword and cower behind your shield."
    print "You think to yourself 'I am Lonk, I am a Hero, I am Lonk, I am a Hero.'"
    print "Your affirmations do nothing to calm your nerves. Those self-help books were clearly garbage."
    print "A big spooky ghost flies into your face and says:" 
    print "I am a spirit. I want to be free. I want to take your body."
    print "I don't think I'm going to write the rest of this game..."
    print "I need to get on with the rest of this book."
    print "I learned plenty from ex35, I don't need to..."
    print "Ok moving on"
    raw_input()

    dead("You die from ghost inhalation.")
    exit(0)





def dead(why):
    print why, "You\'ll never save Zorldo now!"
    exit(0)



start()


