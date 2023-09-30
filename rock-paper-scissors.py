import random

selections = ["ROCK", "SCISSORS", "PAPER"]

def main () :
    again = "Y"
    while again == "Y" :
    
        player_score = 0
        comp_score = 0

        comp = comp_move()
        player = player_move()

        # circle check
            # if player == selection[i] and comp == selection[i+1]

        # lineer check
        if player == "ROCK" :
            if comp == "ROCK" :
                result = "DRAW"

            elif comp == "SCISSORS" :
                result = "PLAYER"
                player_score += 1

            else :
                result = "COMP"
                comp_score += 1

    #################
        if player == "SCISSORS" :
            if comp == "ROCK" :
                result = "COMP"
                comp_score += 1
                
            elif comp == "SCISSORS" :
                result = "DRAW"
            else :
                result = "PLAYER"
                player_score += 1
    #################
        if player == "PAPER" : 
            if comp == "ROCK" :
                result = "PLAYER"
            elif comp == "SCISSORS" :
                result = "COMP"
            else :
                result = "DRAW"

        result_text(player, comp, result)
        again = input("DO YOU WANT TO PLAY AGAIN (Y/N) :\n").upper()

    print(f"SCORES : \n PLAYER : {player_score} \n COMP : {comp_score}")

def result_text (player, comp, result) :
    if result != "DRAW" :
        print(f"PLAYER : {player} \n COMP : {comp} \n RESULT : {result} WON")
    else :
        print(f"PLAYER : {player} \n COMP : {comp} \n RESULT : DRAW")
    
def comp_move () :
    comp = random.choice(selections)

    return comp

def player_move () :
    player = input("MOVE : ").upper()
    while player not in selections :
        player = input("MOVE : ").upper()

    return player

main()