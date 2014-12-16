class Song(object):
    def __init__(self, cock):
        self.lyrics = cock

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def fuck_up_song(self):
        for line in self.lyrics:
            #I got this from stackoverflow. it's a slice. surprised it worked.
            print line[::-1]



# happy_bday = Song(["Happy birthday to you",
#                     "I don't want to get sued",
#                     "So I'll stop right there"])

# bulls_on_parade = Song(["They rally around tha family",
#                         "With pockets full of shells"])

# warewolves_of_london = Song(["Awoooooooooo!",
#                              "Warewolves of london"])

#cats_cradle = Song(["The cat's in the cradle",
#                     "with the silver spoon",])


# cats = """The cat's in the cradle
#         with the silver spoon"""

been_a_while = "It's been a while", "since I had cock"


# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

# warewolves_of_london.sing_me_a_song()

# cats_cradle.sing_me_a_song()

thing = Song(been_a_while)
thing.fuck_up_song()