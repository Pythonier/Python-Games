# this is version two (2) of the Python text game '4213'
# everything handled through defined sections (functions, in a sense)
# questions? PM Excellence_ on the Broken Legion Forums (http://brokenlegion.org/smf)

# handling the title screen stuff
title = """
0   0   00000   0   00000
0   0       0   0       0
00000   00000   0   00000
    0   0       0       0
    0   00000   0   00000
"""

# little opening section
print "\nThe house at the end of the street, 4213. Know one knows anything about it."
print "But you're brave, you'll enter the house."
print "But what lies within?"
print "You hope to find out."
print "\nWelcome to..."
print "--------------------------"
print title
print "--------------------------"
print "The Python text game by Excellence_ of Broken Legion."
# end of the title screen and opening stuff

# defining the name here to make everything work easier
name = raw_input("\nWhat is your name: ").capitalize()

# here, let's define classes NOW and add them here as needed!    
# commands listing
def commands():
    print "\nThe following make up possible commands:"
    print "Examine (object), Open (object), Enter (object)"
    print "Leave (exits the room), Quit (leave game), Commands"
    print "Some rooms have additional commands for you to figure out!"
    
# front of house...obviously.
def front_of_house():
    print "\nYou're standing in front of house 4213." # let's remember to break each section to make reading easier.
    print "What would you like to do?"
    door_choice = raw_input("> ").lower()
    if door_choice == "enter house":
        house_door() # quick, single documentation: these are the functions we call for the choice made. varies depending on section.
    elif door_choice == "backyard":
        backyard()
    elif door_choice == "leave":
        leave_house()
    elif door_choice == "help":
        game_help()
        front_of_house()
    elif door_choice == "commands":
        commands()
        front_of_house()
    elif door_choice == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        front_of_house()
        
# yeah, we need credits! -- name isn't working if errors made, so screw it, restart
def game_credits():
    print "\n- 4213 - Python text game by Excellence_ of Broken Legion"
    print "- Broken Legion: http://brokenlegion.org/smf"
    print "- Idea(s) by: Excellence_, iBoredom_"
    print "- Game written by: Excellence_"
    print "- Code Checking: Excellence_ and iBoredom_"
    print "- Testing done by: Excellence_ and iBoredom_"
    print "- Game Copyright Excellence_, 2012"
    start_menu()
        
# uh, like, you need to make a proper choice at the title too! (no name of player here); this is obsolete i think
def title_error():
    print "\nMistake has been made, game error! Closing!"
    
# aw, they left the house. farewell, {username}!
def leave_house():
    print "\nYou leave the property..."
    print "You'll never know the secrets of house 4213, {0}.".format(name)
    
# this has become obsolete with menus reloading upon typing error - keep it anyways!
def game_error():
    raise SystemExit("\nGAME ERROR - Game error has occurred! Report it to Excellence_ with documentation.")

# player quit mid game
def game_quit():
    raise SystemExit("\nGood bye, {0}.".format(name))
    
# don't go into the storage room!
def storage_room():
    print "\nYou walk into the storage room."
    print "As you take a few steps further in, you hear the door slam shut."
    print "You can suddenly smell the faint oder of some gas."
    print "As you begin to fade, you can hear someone laughing."
    game_lost() # should we make a death box like the title? maybe...na (easy add, but i don't want to right now)
    
# hallway weird door; used in the hall instance no matter what the option chosen is.
def weird_door():
    print "\nYou open the door at the hallway."
    print "Upon entering, you see a ladder and an old chest."
    print "What would you like to do?"
    weird_room = raw_input("> ").lower()
    if weird_room == "examine ladder":
        print "\nThe ladder appears to lead to an upstairs room."
        print "It can be climbed."
        weird_door()
    elif weird_room == "climb ladder":
        print "\nYou climb up the ladder."
        locked_room()
    elif weird_room == "examine chest":
        print "\nThis chest appears to be unlocked, it could be opened."
        weird_door()
    elif weird_room == "open chest":
        print "\nYou decide to open the chest."
        print "Inside, you find a medallion of some sort."
        print "Keep the medallion or leave it?"
        medallion = raw_input("> ").lower()
        if medallion == "keep":
            print "\nYou keep the medallion, feeling an attraction towards it."
            print "Now you decide to climb the ladder."
            locked_room()
        elif medallion == "leave":
            print "\nYou leave the medallion in the chest."
            weird_door()
        else:
            print "\nHELP: Try as keep or leave."
            weird_door()
    elif weird_room == "return":
        print "\nThe painting still weirds you out. You decide to stay in this room."
        weird_door()
    elif weird_room == "help":
        game_help()
        weird_door()
    elif weird_door == "commands":
        commands()
        weird_door()
    elif weird_door == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        weird_door()
    
# remember that locked left room? ENTER we go!
def locked_room():
    print "\nYou climb the ladder and realize you are in the locked"
    print "left room of the upstairs."
    print "You see a single book on the floor."
    print "What do you do?"
    book = raw_input("> ").lower()
    if book == "examine book":
        print "\nThe book looks old and interesting. Dust has settled on it, meaning"
        print "it hasn't been moved in awhile."
    elif book == "read book":
        print "\nYou pick up the book - it appears to be a diary."
        print "You sit down and begin reading it."
        read_book()
    elif book == "leave room":
        print "\nYou exit the room and the door slams shut."
        print "You try to open the door; it's locked from this side."
        stairs_up()
    elif book == "climb ladder":
        print "\nYou see no reason to return to the previous room."
        locked_room()
    elif book == "help":
        game_help()
        locked_room()
    elif book == "commands":
        commands()
        locked_room()
    elif book == "quit":
        game_quit()
    else:
        print "\nInvalid Choice"
        locked_room()
        
# into the house we went! front door of the house
def entrance():
    print "\nYou see a staircase and a room to the right. What do you do?"
    house_enter = raw_input("> ").lower()
    if house_enter == "climb stairs":
        stairs_up()
    elif house_enter == "examine stairs":
        print "\nThe stairs lead up stairs."
        entrance()
    elif house_enter == "enter right room":
        room_right()
    elif house_enter == "examine right room":
        print "\nIt appears to be a gathering room of some sort."
        print "You can see a few things from where you stand."
        entrance()
    elif house_enter == "return":
        front_of_house()
    elif house_enter == "help":
        game_help()
        entrance()
    elif house_enter == "commands":
        commands()
    elif house_enter == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        entrance()
    
# approach that door
def house_door():
    print "\nYou approach the front door."
    print "You knock on the door..."
    print "...and it slowly opens."
    print "You enter the house."
    print "You see a staircase and a room to the right. What do you do?"
    house_enter = raw_input("> ").lower()
    if house_enter == "climb stairs":
        stairs_up()
    elif house_enter == "examine stairs":
        print "\nThe stairs lead up stairs."
        entrance()
    elif house_enter == "enter right room":
        room_right()
    elif house_enter == "examine right room":
        print "\nIt appears to be a gathering room of some sort."
        print "You can see a few things from where you stand."
        entrance()
    elif house_enter == "return":
        front_of_house()
    elif house_enter == "help":
        game_help()
        entrance()
    elif house_enter == "commands":
        commands()
    elif house_enter == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        entrance()
    
# chose to go around back
def backyard():
    print "\nYou head around back."
    print "You see a broken window."
    print "What do you do?"
    backyard_choice = raw_input("> ").lower()
    if backyard_choice == "enter house":
        window_entrance()
    elif backyard_choice == "examine window":
        print "\nThe window appears to be broken; you could fit"
        print "through it and enter the house."
        backyard()
    elif backyard_choice == "return":
        print "\nYou return to the front of the house."
        front_of_house()
    elif backyard_choice == "leave":
        leave_house()
    elif backyard_choice == "help":
        game_help()
        backyard()
    elif backyard_choice == "commands":
        commands()
    elif backyard_choice == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        backyard()
        
# they be climbin' up yo' windows!
def window_entrance():
    print "\nYou enter the house from the broken window."
    print "You appear to be in a bedroom."
    print "What would you like to do?"
    bedroom = raw_input("> ").lower()
    if bedroom == "lay in bed":
        bed_sleep()
    elif bedroom == "lay down":
        bed_sleep()
    elif bedroom == "open door":
        bed_to_hallway()
    elif bedroom == "examine door":
        print "\nThe door appears to be unlocked and could be opened."
    elif bedroom == "examine room":
        print "\nYou see a bed and a door, plus the window behind you."
        window_entrance()
    elif bedroom == "return":
        backyard()
    elif bedroom == "help":
        game_help()
        window_entrance()
    elif bedroom == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        window_entrance()
        
# sleep on the broken window room bed
def bed_sleep():
    print "\nYou lay down on the bed. It is surprisingly comfortable."
    print "You drift into a deep sleep."
    print "..."
    print "You wake to the sound of a 'thunk' outside the door."
    print "What do you do?"
    bed_woken = raw_input("> ").lower()
    if bed_woken == "open door":
        print "\nYou walk to the door, but find it locked."
        bed_sleep()
    elif bed_woken == "examine door":
        print "\nThe door appears locked at the moment."
        print "However, you can hear something beyond it."
    elif bed_woken == "yell":
        print "\nIS SOMEONE THERE!?"
        print "..."
        yelled()
    elif bed_woken == "leave room":
        print "\nYou climb back out the broken window."
        backyard()
    elif bed_woken == "return":
        print "\nYou climb out the broken window."
        backyard()
    elif bed_woken == "help":
        game_help()
        bed_sleep()
    elif bed_woken == "commands":
        commands()
        bed_sleep()
    elif bed_woken == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        bed_sleep()
            
# right door of the upstairs
def up_room_right():
    print "\nYou enter the room on the right."
    print "What would you like to do?"
    up_room_right_choice = raw_input("> ").lower()
    if up_room_right_choice == "open dresser":
        print "\nYou open the dresser and see a note."
        dresser_choice = raw_input("> ").lower()
        if dresser_choice == "take note":
            print "\nThe note says:"
            print "\n\t'Forever alone in this house, I am."
            print "\tBut the house is me and myself."
            print "\tNo one shall enter my house and live."
            print "\tMy house shall be mine and my own.'"
            print "\nThe note is rather weird; you return it to the dresser."
            print "You leave the room."
            stairs_up()
        elif dresser_choice == "leave note":
            up_room_right()
        else:
            print "\nHint: try take note or leave note!"
            up_room_right()
    elif up_room_right_choice == "leave":
        stairs_up()
    elif up_room_right == "examine room":
        print "\nInside the room you see a desser and nothing more."
        up_room_right()
    elif up_room_right_choice == "help":
        game_help()
        up_room_right()
    elif up_room_right == "commands":
        commands()
        up_room_right()
    elif up_room_right == "quit":
        game_quit()
    else:
        print "\nInvalid Choice."
        up_room_right()
        
# chose to sleep on the living room couch
def lay_down():
    print "\nYou lay down on the couch and drift into a deep sleep."
    print "..."
    print "You wake sometime later, but not on the couch."
    print "Based on how cool it is, you think you are in a basement."
    print "It is dark, what would you like to do?"
    print "1. Stumble around and try to find an exit."
    print "2. Stay put and think of something else."
    base_choice = raw_input("> ").lower()
    if base_choice == "1":
        print "\nYou attempt to move around, but due to the darkness,"
        print "you walk into a low bar. As you begin to regain consciousness, you hear"
        print "someone laughing. You begin to weep as you realize..."
        print "...you are trapped and you will die in house 4213."
        game_lost()
    elif base_choice == "2":
        relax()
    elif base_choice == "help":
        game_help()
        lay_down()
    else:
        print "\nInvalid Choice."
        lay_down()

# left door of the upstairs
def up_room_left():
    print "\nYou try to open the left door."
    print "It appears locked, you can't get the door to budge."
    print "You can't do anything with this door."
    stairs_up()

# go into the room right of the entrance
def room_right():
    print "\nYou go into the room on the right."
    print "It appears to be the living room of the house."
    print "You see an old couch, a closed door, and an old walk-in storage room."
    print "What would you like to do?"
    print "1. Lay down on the couch."
    print "2. Examine the closed door."
    print "3. Enter the storage room."
    print "4. Return to the entrance."
    room_right_choice = raw_input("> ").lower()
    if room_right_choice == "1":
        lay_down()
    elif room_right_choice == "2": 
        print "\nThis door is bolted shut, nothing you can do."
        room_right()
    elif room_right_choice == "3":
        storage_room()
    elif room_right_choice == "4":
        entrance()
    elif room_right_choice == "help":
        game_help()
        room_right()
    else:
        print "\nInvalid Choice."
        room_right()

# up the stairs we go!
def stairs_up():
    print "\nYou head up the stairs and come to a fork."
    print "There is a room to the left and to the right."
    print "What would you like to do?"
    print "1. Go into the left room."
    print "2. Go into the room on the right."
    print "3. Go back downstairs."
    upstairs_room_choice = raw_input("> ").lower()
    if upstairs_room_choice == "1":
        up_room_left()
    elif upstairs_room_choice == "2":
        up_room_right()
    elif upstairs_room_choice == "3":
        entrance()
    elif upstairs_room_choice == "help":
        game_help()
        stairs_up()
    else:
        print "\nInvalid Choice."
        stairs_up()
        
# yell at the sound!
def yelled():
    print "You hear a key being inserted into the door."
    print "The door slowly opens..."
    print "You see a shadow enter the room."
    print "You back into a corner and scream..."
    print "\n...but no one will hear you."
    game_lost()
    
# broken window room into hallway
def bed_to_hallway():
    print "\nYou go to the door and open in."
    print "You step into the hallway and look around."
    print "To your left is a long hallway with a single door."
    print "To the right is a painting."
    print "1. Head to the doorway."
    print "2. Examine the painting."
    hallway = raw_input("> ").lower()
    if hallway == "1":
        print "\nYou head down the hallway towards the door."
        print "You swear you hear a sound beyond it."
        weird_door()
    elif hallway == "2":
        print "\nYou examine the painting. It appears to be of..."
        print "YOU!"
        print "You run towards to door at the end of the hallway."
        weird_door()
    elif hallway == "help":
        game_help()
        bed_to_hallway()
    else:
        print "\nInvalid Choice."
        bed_to_hallway()

# open bedroom dresser
def dresser():
    print "\nYou open the dresser and find a note."
    print "What would you like to do?"
    print "1. Read the note."
    print "2. Ignore the note and leave the room."
    dresser_choice = raw_input("> ").lower()
    if dresser_choice == "1":
        print "\nThe note says:"
        print "\n\t'Forever alone in this house, I am."
        print "\tBut the house is me and myself."
        print "\tNo one shall enter my house and live."
        print "\tMy house shall be mine and my own.'"
        print "\nThe note is rather weird; you return it to the dresser."
        print "You leave the room."
        stairs_up()
    elif dresser_choice == "2":
        stairs_up()
    elif dresser_choice == "help":
        game_help()
        dresser()
    else:
        print "\nInvalid Choice."
        dresser()
        
# they chose to not stumble around the basement
def relax():
    print "\nYou sit down on the cold, hard floor."
    print "You try to think about how you could escape the dark room."
    print "After awhile, you realize you're eyes have adjusted to the dark."
    print "You attempt to now find an exit."
    leave_basement()

# alright, they can leave the basement now
def leave_basement():
    print "\nYou run your hands along the wall, trying to find a staircase."
    print "After some time, you find what appears to be a door."
    print "What would you like to do?"
    print "1. Open the door."
    print "2. Continue searching for a staircase."
    base_door = raw_input("> ").lower()
    if base_door == "1":
        print "\nYou push on the door, but it doesn't move."
        print "You try again and again, finally managing to open it."
        print "The door is now open; you decide to enter."
        room_in_basement()
    elif base_door == "2":
        print "\nYou continue searching for a staircase, but you do not find one."
        leave_basement()
    elif base_door == "help":
        game_help()
        leave_basement()
    else:
        print "\nInvalid Choice."
        leave_basement()
        
# found that room in the basement..hmmmmmmm?
def room_in_basement():
    print "\nYou enter the room, the door shutting behind you."
    print "Suddenly, the room lights up and you are face to face with"
    print "an image of yourself, but it is not a mirror."
    print "What would you like to do?"
    print "1. Attempt to speak to the image."
    print "2. Punch at the image."
    print "3. Attempt to leave the room."
    yourself = raw_input("> ").lower()
    if yourself == "1":
        print "\nYou begin speaking to the image, but it doesn't appear"
        print "to understand.  You try again; but this time, the image"
        print "appears to understand and disappears, leaving behind a"
        print "key.  You are unsure of what it goes to yet."
        print "A door suddenly opens behind the now gone image."
        image_door()
    elif yourself == "2":
        print "\nYou attempt to punch the image, but it disappears and"
        print "the room goes dark. You feel a sharp pain in your back"
        print "and fall over. The lights suddenly go back on, just in time"
        print "for you to see a shadow bring a knife down upon you."
        game_lost()
    elif yourself == "3":
        print "\nYou attempt to open the door, but you come out"
        print "into the house entrance, apparently through the"
        print "front door. You are confused."
        entrance()
    elif yourself == "help":
        game_help()
        room_in_basement()
    else:
        print "\nInvalid Choice."
        room_in_basement()
        
# image created a door - gogogo!
def image_door():
    print "The room beyond the image reveals an alter and a door."
    print "What would you like to do?"
    print "1. Examine the alter."
    print "2. Open the door."
    alter_room = raw_input("> ").lower()
    if alter_room == "1":
        print "You step forward to examine the alter."
        print "You see a small keyhole, and you insert the key"
        print "left by the image."
        print "You hear a small click and a trap door opens beneath you."
        trap_door()
    elif alter_room == "2":
        print "You go to the door and open it."
        print "You walk out into the living room, somehow."
        room_right()
    elif alter_room == "help":
        game_help()
        image_door()
    else:
        print "\nInvalid Choice."
        image_door()
        
# that alter trap door thing...yeah
def trap_door():
    print "\nYou climb down through the trap door."
    print "As you reach the bottom, you see that you have"
    print "entered a long tunnel. You can make the faint glow"
    print "of a light from the end."
    print "You follow the tunnel towards the light."
    print "\nYou reach the end, and the light begins glowing very brightly."
    print "You can finally see again, now standing before a man in a cloak,"
    print "his face covered. What would you like to do?"
    hidden_man = raw_input("> ").lower()
    if hidden_man == "speak":
        print "\nHello, {0}. I've been waiting for you.".format(name)
        print "Would you like the secrets of 4213?"
        print "Yes or No"
        play_riddle = raw_input("> ").lower() # miniature plot within the class? okay, fun! play to know the secrets now!
        if play_riddle == "yes":
            print "\nThen we shall play a little game."
            game()
        elif play_riddle == "no":
            print "\nThan you shall die!"
            game_lost()
        else:
            print "\nInvalid Choice."
            trap_door()
    elif hidden_man == "look around":
        print "\nYou have no idea where you are. There appears to be no exit."
        trap_door()
    elif hidden_man == "return":
        print "\nYou have no idea where you are. There appears to be no exit."
        trap_door()
    elif hidden_man == "examine man":
        print "\nHe is wearing a cloak, nothing much to see."
        trap_door()
    elif hidden_man == "attack man":
        print "\nYou dare to attack ME? You shall die here!"
        game_lost()
    elif hidden_man == "help":
        game_help()
        trap_door()
    elif hidden_man == "commands":
        commands()
        trap_door()
    else:
        print "\nInvalid Choice."
        trap_door()

# old man's game, leggo!
# should we handle it all in this one class? why the hell not?
def game():
    print "\nYou shall answer my questions if you wish to"
    print "to know the secrets of this place. Let's play."
    print "What is the address of this place?"
    question_one = raw_input("> ").lower()
    if question_one == "4213":
        print "\nCorrect, but tis' was easy question."
        print "What has four legs in the morning, two legs"
        print "in the afternoon, and three legs in the evening?"
        question_two = raw_input("> ").lower()
        if question_two == "man":
            print "\nHmph, lucky. Again!"
            print "Final question: A Person walked Parallel to a Legion of Elephants."
            final_question = raw_input(" >").lower()
            if final_question == "apple":
                print "\nThe answers await."
                final_room()
            else:
                print "\nGoodbye, {0}.".format(name)
                game_lost()
        else:
            print "\nGoodbye, {0}.".format(name)
            game_lost()
    else:
        print "\nGoodbye, {0}.".format(name)
        game_lost()
        
# read the diary
def read_book():
    print "\nAfter some time, you finish reading the diary."
    print "You read about a door in the basement which is hidden."
    print "You leave the room, the door slaming shut behind you and locking."
    stairs_up()
        
# player chose to exit the game.
def title_leave():
    print "\nGoodbye, {0}.".format(name)
    
# er, player lost, let's eventually reload the start menu
def game_lost():
    print "\nYou have died, {0}...better luck next time!".format(name)
    raise SystemExit("Game Closed")

# er, player won
def game_won():
    print "\nYou've uncovered the secrets of 4213, {0}! Congratulations!".format(name)
    raise SystemExit("Player won, game closed.")
        
# let's create that final eff'ing room
def final_room():
    print "\nThe man disappears, and the room around you changes."
    print "Suddenly, a bolt of light hits you in the head."
    print "Images beginning flashing through your mind, revealing"
    print "the secrets of 4213 - a living nightmare designed"
    print "to trap and kill those who sleep - unless they can"
    print "uncover the secrets."
    game_won()
    
# little help menu thingy mo-jigger
def game_help():
    print "\n4213 - Help"
    print "Type 'commands' to view commands allowed to be used."
    print "Each room contains multiple choices to be made."
    print "Read the dialogue given to you and continue playing!"
    print "Have fun!"
    
# callable start menu class? yes please. also starts the game
def start_menu():
    print "\nWelcome to 4213, {0}.".format(name)
    print "Choose your option."
    print "Play 4213"
    print "Exit"
    print "View Credits"
    start_game = raw_input("> ").lower()
    if start_game == "play":
        print "\nGood luck {0}...you'll need it!".format(name)
        print "Prepare to approach the house."
        front_of_house()
    elif start_game == "exit": # player chose to quit
        title_leave()
    elif start_game == "credits":
        game_credits()
    elif start_game == "help":
        game_help()
        start_menu()
    else:
        print "\nInvalid Choice."
        start_menu()
# let's play
start_menu()