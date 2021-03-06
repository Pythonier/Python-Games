# everything should be documented well enough to edit this game.
# everything handled through defined sections (functions, in a sense)
# questions? PM iBoredom_ on the Broken Legion Forums (http://brokenlegion.org/smf)
# let's, eh, begin?
# wait...Goals to Come
#1. Special ending if player has locket
#2. make it so invalid inputs reload the current menu - easy, but let's finish the story first
#3. whatever else needs to be done

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
print "The Python text game by iBoredom_ of Broken Legion."
# end of the title screen and opening stuff

# let's handle the 'start menu' here
start_menu = ""
print "\nChoose your option."
print "1. Play 4213"
print "2. Exit"
print "3. View Credits"
start_game = raw_input("> ")
""

# globalize the locket
global locket
locket = "false"

# here, let's define classes NOW and add them here as needed!
	
# front of house...obviously.
def front_of_house():
	print "\nYou're standing in front of house 4213." # let's remember to break each section to make reading easier.
	print "What would you like to do?"
	print "1. Go inside the house."
	print "2. Go around back."
	print "3. Leave the property and never come back."
	door_choice = raw_input("> ")
	if door_choice == "1":
		house_door() # quick, single documentation: these are the functions we call for the choice made. varies depending on section.
	elif door_choice == "2":
		backyard()
	elif door_choice == "3":
		leave_house()
	else:
		print "\nInvalid Choice."
		front_of_house()
		
# yeah, we need credits! -- name isn't working if errors made, so screw it, restart
def credits():
	print "\n- 4213 - Python text game by iBoredom_ of Broken Legion"
	print "- Broken Legion: http://brokenlegion.org/smf"
	print "- Idea(s) by: iBoredom_, Excellence_,"
	print "- Game written by: iBoredom_"
	print "- Code Checking: Excellence_ and iBoredom_"
	print "- Testing done by: Excellence_ and iBoredom_"
	print "- Game Copyright iBoredom_, 2012"
	print "\n- Due to menu errors, please restart to play."
		
# uh, like, you need to make a proper choice at the title too! (no name of player here)
def title_error():
	print "\nMistake has been made, game error! Closing!"
	
# aw, they left the house. farewell, {username!}!
def leave_house():
	print "\nYou leave the property..."
	print "You'll never know the secrets of house 4213, {0}.".format(name)
	
# this has become obsolete with menus reloading upon typing error - keep it anyways!
def selection_error():
	raise SystemExit("\nINPUT ERROR - Game error has occured! Report it to Excellence_ with documentation.")
	
# don't go into the storage room!
def storage_room():
	print "\nYou walk into the storage room."
	print "As you take a few steps further in, you hear the door slam shut."
	print "You can suddenly smell the faint oder of some gas."
	print "As you begin to fade, you can hear someone laughing."
	game_lost() # should we make a death box like the title? maybe...na (easy add, but i don't want to right now)
	
# hallway weird door; used in the hall instance no matter what the option chosen is.
def weird_door():
	global locket
	print "\nYou open the door at the hallway."
	print "Upon entering, you see a ladder and an old chest."
	print "What would you like to do?"
	print "1. Climb up the ladder."
	print "2. Examine the chest."
	print "3. Leave the room."
	weird_room = raw_input("> ")
	if weird_room == "1":
		print "\nYou deicde to climb up the ladder and"
		print "see where it leads."
		locked_room()
	elif weird_room == "2":
		print "\nYou see that the chest is not locked and"
		print "you decide to open it."
		print "Inside, you find a locket, which appears to be locked."
		print "You decide to keep the locket, feeling some sort"
		print "of attraction towards it."
		print "You close the chest and turn to the ladder."
		print "You now decide to climb the ladder."
		locket == "true" # this will be important for ending two; without it, the alternate ending ain't happening!
		locked_room()
	elif weird_room == "3":
		print "\nThe painting still weirds you out. You decide to stay in this room."
		weird_door()
	else:
		print "\nInvalid Choice."
		weird_door()
	
# remember that locked left room? ENTER we go!
def locked_room():
	print "\nYou climb the ladder and realize you are in the locked"
	print "left room of the upstairs."
	print "You see a single book on the floor."
	print "What do you do?"
	print "1. Pick up and read the book."
	print "2. Leave the room."
	book = raw_input("> ")
	if book == "1":
		print "\nYou pick up the book - it appears to be a diary."
		print "You sit down and begin reading it."
		read_book()
	elif book == "2":
		print "\nYou exit the room and the door slams shut."
		print "You try to open the door; it's locked from this side."
		stairs_up()
	else:
		print "\nInvalid Choice"
		locked_room()
		
# into the house we went! front door of the house
def entrance():
	print "\nYou see a staircase and a room to the right. What do you do?"
	print "1. Go up the stairs."
	print "2. Go into the room on the right."
	print "3. Go outside."
	house_enter = raw_input("> ")
	if house_enter == "1":
		stairs_up()
	elif house_enter == "2":
		room_right()
	elif house_enter == "3":
		front_of_house()
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
	print "1. Go up the stairs."
	print "2. Go into the room on the right."
	print "3. Go back outside."
	house_enter = raw_input("> ")
	if house_enter == "1":
		stairs_up()
	elif house_enter == "2":
		room_right()
	elif house_enter == "3":
		front_of_house()
	else:
		print "\nInvalid Choice."
		house_door()
	
# chose to go around back
def backyard():
	print "\nYou head around back."
	print "You see a broken window you could climb through."
	print "What do you do?"
	print "1. Enter the house."
	print "2. Return to the front of the house."
	print "3. Leave and never come back."
	backyard_choice = raw_input("> ")
	if backyard_choice == "1":
		window_entrance()
	if backyard_choice == "2":
		print "You return to the front of the house."
		front_of_house()
	elif backyard_choice == "3":
		leave_house()
	else:
		print "\nInvalid Choice."
		backyard()
		
# they be climbin' up yo' windows!
def window_entrance():
	print "\nYou enter the house from the broken window."
	print "You appear to be in a bedroom - you see a bed and a door."
	print "What would you like to do?"
	print "1. Lay down on the bed."
	print "2. Go to the door and open it."
	bedroom = raw_input("> ")
	if bedroom == "1":
		bed_sleep()
	elif bedroom == "2":
		bed_to_hallway()
	else:
		print "\nInvalid Choice."
		window_entrance()
		
# sleep on the broken window room bed
def bed_sleep():
	print "\nYou lay down on the bed. It is surpisingly comfortable."
	print "You drift into a deep sleep."
	print "..."
	print "You wake to the sound of a 'thunk' outside the door."
	print "What do you do?"
	print "1. Go to the door."
	print "2. Yell at the sound."
	print "3. Leave the house."
	bed_woken = raw_input("> ")
	if bed_woken == "1":
		print "\nYou walk to the door, but find it locked."
		bed_sleep()
	elif bed_woken == "2":
		print "\nIS SOMEONE THERE!?"
		print "..."
		yelled()
	elif bed_woken == "3":
		print "\nYou climb back out the broken window."
		backyard()
	else:
		print "\nInvalid Choice."
		bed_sleep()
			
# right door of the upstairs
def up_room_right():
	print "\nYou enter the room on the right."
	print "Inside the room you see a desser and nothing more."
	print "What would you like to do?"
	print "1. Go to the dresser and open it."
	print "2. Leave the room."
	up_room_right_choice = raw_input("> ")
	if up_room_right_choice == "1":
		dresser()
	elif up_room_right_choice == "2":
		stairs_up()
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
	base_choice = raw_input("> ")
	if base_choice == "1":
		print "\nYou attempt to move around, but due to the darkness,"
		print "you walk into a low bar. As you begin to regain consciousness, you hear"
		print "someone laughing. You begin to weep as you realize..."
		print "...you are trapped and you will die in house 4213."
		game_lost()
	elif base_choice == "2":
		relax()
	else:
		print "\nInvalid Choice."
		lay_down()

# left door of the upstairs
def up_room_left():
	print "\nYou try to open the left door."
	print "It appears locked, you can't get the door to budge."
	print "You can't do anything with this door."
	stairs_up()

# let's try this for giving the locket..useless function right now, let's just make in dead.
#def locket():
	#locket == "1"

# go into the room right of the entrance
def room_right():
	global locket
	print "\nYou go into the room on the right."
	print "It appears to be the living room of the house."
	print "You see an old couch, a closed door, and an old walk-in storage room."
	print "What would you like to do?"
	print "1. Lay down on the couch."
	print "2. Examine the closed door."
	print "3. Enter the storage room."
	print "4. Return to the entrance."
	room_right_choice = raw_input("> ")
	if room_right_choice == "1":
		lay_down()
	elif room_right_choice == "2": # this is not needed right now (and locket == "0":)
		if locket == "true":
			special_win()
		else:
			print "\nThis door is bolted shut, nothing you can do."
			room_right()
	elif room_right_choice == "3":
		storage_room()
	elif room_right_choice == "4":
		entrance()
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
	upstairs_room_choice = raw_input("> ")
	if upstairs_room_choice == "1":
		up_room_left()
	elif upstairs_room_choice == "2":
		up_room_right()
	elif upstairs_room_choice == "3":
		entrance()
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
	hallway = raw_input("> ")
	if hallway == "1":
		print "\nYou head down the hallway towards the door."
		print "You swear you hear a sound beyond it."
		weird_door()
	elif hallway == "2":
		print "\nYou examine the painting. It appears to be of..."
		print "YOU!"
		print "You run towards to door at the end of the hallway."
		weird_door()
	else:
		print "\nInvalid Choice."
		bed_to_hallway()

# open bedroom dresser
def dresser():
	print "\nYou open the dresser and find a note."
	print "What would you like to do?"
	print "1. Read the note."
	print "2. Ignore the note and leave the room."
	dresser_choice = raw_input("> ")
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
	base_door = raw_input("> ")
	if base_door == "1":
		print "\nYou push on the door, but it doesn't move."
		print "You try again and again, finally managing to open it."
		print "The door is now open; you decide to enter."
		room_in_basement()
	elif base_door == "2":
		print "\nYou continue searching for a staircase, but you do not find one."
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
	yourself = raw_input("> ")
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
	else:
		print "\nInvalid Choice."
		room_in_basement()
		
# image created a door - gogogo!
def image_door():
	print "The room beyond the image reveals an alter and a door."
	print "What would you like to do?"
	print "1. Examine the alter."
	print "2. Open the door."
	alter_room = raw_input("> ")
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
	print "his face covered. What do you do?"
	print "1. Speak to the man."
	print "2. Run back towards the trap door."
	old_man = raw_input("> ")
	if old_man == "1":
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
	elif old_man == "2":
		print "You have no idea where you are. There appears to be no exit."
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
	question_one = raw_input("> ")
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
	print "\nAfter some time, you finish reading the book - which turned out to be a diary."
	print "You read about a door in the basement which requires a special key."
	print "You should attempt to find the key...if you want the secrets of 4213."
	print "You leave the room, the door slaming shut behind you and locking."
	stairs_up()
	
# hopefully this works...with locket: ending two; without: ending one, since you found the door
# this function is useless right now...i won't fully comment out though
def special_door(): 
		print "\nYou insert the locket and the door opens."
		print "You enter the room...in front of you is..."
		print "YOURSELF!"
		print "You look down and examine the locket."
		print "Inside, you see a picture of your family."
		print "Suddenly, you are hit with a chill."
		print "....."
		print "....."
		print "You wake up in your bed, the secrets of 4213 revealed."
		print "4213 never existed, but was a dream...a living nightmare."
		print "You hope to never again enter house 4213...but will you?"
		special_win()
		
# player chose to exit the game.
def title_leave():
	print "\nGoodbye, player."
	
# er, player lost, let's eventually reload the start menu
def game_lost():
	print "\nYou have died, {0}...better luck next time!".format(name)
	raise SystemExit("Game Closed")

# er, player won
def game_won():
	print "\nYou've uncovered the secrets of 4213, {0}! Congratulations!".format(name)
	raise SystemExit("Player won, game closed.")
	
# they had the locket, special win! NOTE: currently unused
def special_win():
		print "\nCongratulations, {0}! You know the true secrets of 4213, but is something".format(name)
		print "left hidden? Play again to find out!"
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

# let's attempt to play, eh? 
# this, eh, starts the story.
if start_game == "1":
	name = raw_input("What is your name, player: ")
	print "\nWelcome to 4213, {0}.".format(name)
	print "Prepare to approach the house, {0}.".format(name)
	print "Goodluck...you'll need it."
	front_of_house()
elif start_game == "2": # player chose to quit
	title_leave()
elif start_game == "3":
	credits()
else:
	title_error() # title error, used when player types invalid choice at the title (title only, read this documentation)