import random as rd


def player(hand):
    if hand == 1:
        stance = "rock"
        return stance
    elif hand == 2:
        stance = "paper"
        return stance
    elif hand == 3:
        stance = "scissor"
        return stance
    elif hand == 4:
        stance = rd.choice(["rock", "paper", "scissor"])
        return stance


def computer():
    stance = rd.choice(["rock", "paper", "scissor"])
    return stance


