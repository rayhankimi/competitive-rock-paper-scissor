
def decision(playerhand, computerhand):
    if playerhand == computerhand:
        winner = "DRAW"
        print("The same guardian powers cancel each other... DRAW")
        return winner
    elif playerhand == "rock" and computerhand == "scissor":
        winner = "Player"
        print("Mighty earth calls for their supreme control!")
        return winner
    elif playerhand == "paper" and computerhand == "rock":
        winner = "Player"
        print("Even the strongest will fear the power of knowledge!")
        return winner
    elif playerhand == "scissor" and computerhand == "paper":
        winner = "Player"
        print("The cut that none ever witness before!")
        return winner
    else:
        winner = "Computer"
        print("You choose the wrong stance...")
        return winner