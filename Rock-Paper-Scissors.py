while True:
    player1 = str(input ("Choose rock, paper or scissors "))
    if player1 != "rock" or "paper" or "scissors":
        print ("Put valid value")
    player2 = str(input ("Choose rock, paper or scissors "))
    if player1 != "rock" or "paper" or "scissors":
        print ("Put valid value")
    
    
    game_dict = {"rock" : 1, "paper" : 2, "scissors" : 3}   #our own dictionary which assign every word a number
    A = game_dict.get(player1)
    B = game_dict.get(player2)
    dif = A-B

    if dif in [-2,1]:
        print ("Player A wins")
        if str(input("Do you want to play another game?")) == "yes":
            continue
        else:
            print("game over")
            break
    elif dif in [-1,2]:
        print ("Player B wins")
        if str(input("Do you want to play another game?")) == "yes":
            continue
        else:
            print("game over")
            break
    else:
        print ("Draw")
        if str(input("Do you want to play another game?")) == "yes":
            continue
        else:
            print("game over")
            break


