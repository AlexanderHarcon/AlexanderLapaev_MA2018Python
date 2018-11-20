import simplegui
import random

num_range = random.randrange(0,100)
num_guesse = 7

def user_input(player):
    player_choice = int(player)
    print ("\nPlayer chose the number: " + player)
    if player_choice == num_range:
        print ("**You win!**")
        range100()
    elif player_choice > num_range:
        print ("Lower!")
        user_attempt()
    else:
        print ("Higher!")
        user_attempt()

def range100():
    global num_range, num_guesse
    print("\n***New Game 0..100***" + "\nNumber of player attempts 7")
    num_guesse = 7
    num_range = random.randrange(0,100)
def range1000():
    global num_range, num_guesse
    print("\n***New Game 0..1000***" + "\nNumber of player attempts 10")
    num_guesse = 10
    num_range = random.randrange(0,1000)

def user_attempt():
    global num_guesse
    num_guesse -= 1
    if num_guesse > 0:
        print("Attempts left: " + str(num_guesse))
    else:
        print("\nGame Over..."+"\nThe number that was planned was:", num_range )
        range100()
                  
frame = simplegui.create_frame("Guess the number", 100, 180)      
frame.add_button("Range 0..100", range100, 100)
frame.add_button("Range 0..1000", range1000, 100)
inp = frame.add_input("Send", user_input, 100)