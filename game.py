import ranking
import hand
import mechanics


def choose():
    try:
        print("1. Rock, 2. Paper, 3. Scissor, 4. Random")
        playerInput = int(input("Choose your hand : "))
    except ValueError:
        print("Invalid input")
        choose()
    if 4 >= playerInput >= 1:
        return playerInput
    else:
        print("Invalid input")
        choose()


def game():
    print("Welcome to Competitive R,P,S")
    try:
        trophy = int(input("Enter your last Trophy  : "))
        print(f"Ok got it rank {trophy} is assigned as {ranking.title(trophy)}")
    except ValueError:
        print("Please enter a valid number.")
    while True:
        playerInput = choose()

        player_hand = hand.player(playerInput)
        computer_hand = hand.computer()

        print(f"You cast {player_hand} upon {computer_hand} ...")

        winner = mechanics.decision(player_hand, computer_hand)
        final_trophy = ranking.trophy_gain(winner, trophy)
        print(f"Your final trophy is {final_trophy} and your rank is {ranking.title(final_trophy)}")

        trophy = final_trophy


game()
