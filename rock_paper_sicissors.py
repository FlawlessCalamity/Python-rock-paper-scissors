import random

points = 0
player_input=''
comp = "as yet unused"
player = ""
playable = False
outcome=""
diceroll=0
win_point = 2
lose_point = -4
draw_point = 1

def print_game_start():
    print_space(3)
    print ("##############################################################")
    print ("Welcome to Rock Paper Scissors")
    print ("##############################################################")
    print_space(3)

def print_game(comp,play,score,outcome):
    print_space(3)
    print_headers()
    print_space(2)
    print ("\t\t\t\t\t\t\t" + "Score: " + str(score))
    print ("Computer throws: " + comp)
    print ("Player throws: " + play)
    print ("")
    print ("Result: " + outcome)
    print_space(2)
    print_headers()
    print_space(3)    

def game(choice):
    global points, win_point, lose_point, draw_point
    diceroll=(random.randint(1,3))
    if diceroll == 1:
        comp_input = "Rock"
        if choice == 'rock':
            points = points+draw_point
            return ("draw",comp_input)
        elif choice == 'paper':
            points = points+win_point
            return ("win",comp_input)
        else: 
            points=points+lose_point
            return ("lose",comp_input)
    elif diceroll == 2:
        comp_input = "Paper"
        if choice == 'rock':
            points = points+lose_point
            return ("lose",comp_input)
        elif choice == 'paper':
            points = points+draw_point
            return ("draw",comp_input)
        else: 
            points = points+win_point
            return ("win",comp_input)
    else:
        comp_input = "Scissors"
        if choice == 'rock':
            points = points+win_point
            return ("win",comp_input)
        elif choice == 'paper':
            points = points+lose_point
            return ("lose",comp_input)
        else:    
            points = points+draw_point
            return ("draw",comp_input) 

def game_end():
    global points
    print_space(4)
    print_headers()
    print ("Conratulations your final score is: " + str(points))
    print_headers()

def print_space(numOfLines):
    for _ in range(numOfLines):
        print ("")  

def print_headers():
    print ("#################################################################")
    print ("#################################################################")              


print_game_start()
 

while playable == False:

    player_input = input (("What you feeling? Press 'r' for Rock, 'p' for Paper or 's' for Scissors"))

    if player_input == '0':
        playable = True
    elif player_input == 'r':
        outcome = game('rock')
        player = "Rock"
        comp = outcome[1]
        print_game (comp,player,points,outcome[0])
        
    elif player_input == 'p':
        outcome = game('paper')
        player = "Paper"
        comp = outcome[1]
        print_game (comp,player,points,outcome[0])
        
    elif player_input == 's': 
        outcome = game('scissors')
        player = "Scissors"
        comp = outcome[1]
        print_game (comp,player,points,outcome[0])

game_end()            

                   
