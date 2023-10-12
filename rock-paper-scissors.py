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
    player_visual = move_visual(player)
    comp_visual = move_visual(comp)
    if result != "DRAW" :
        print(f"PLAYER : {player_visual} \n COMP : {comp_visual} \n RESULT : {result} WON")
    else :
        print(f"PLAYER : {player_visual} \n COMP : {comp_visual} \n RESULT : DRAW")
    
def comp_move () :
    comp = random.choice(selections)
    return comp

def player_move () :
    player = input("MOVE : ").upper()
    while player not in selections :
        player = input("MOVE : ").upper()

    return player

def move_visual (move) :
    if move == "ROCK" :
        result_visual = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        """
    elif move == "SCISSORS" :
        result_visual = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """
    elif move == "PAPER" :
        result_visual = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
        """
    
    return result_visual
main()
