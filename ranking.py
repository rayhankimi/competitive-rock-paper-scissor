def title(trophy):
    if trophy < 200:
        rank = "Bronze Brawler"
        return rank
    elif trophy < 400:
        rank = "Crystal Crusader"
        return rank
    elif trophy < 600:
        rank = "Dark Duelist"
        return rank
    elif trophy < 800:
        rank = "Enigmatic Elysium"
        return rank
    elif trophy < 1000:
        rank = "Ferocious Fantasia"
        return rank
    elif trophy < 1500:
        rank = "Glorious Goldenia"
        return rank
    elif trophy < 2000:
        rank = "Heavenly Harbringer"
        return rank
    elif trophy < 3000:
        rank = "Impermenance Incarnation"
        return rank
    elif trophy < 4000:
        rank = "Jesterous Jackalope"
        return rank
    elif trophy < 5000:
        rank = "Kingslayer of Kings"
        return rank
    elif trophy > 5000:
        rank = "Last Lord"
        return rank
    else:
        rank = "???"
        return rank


def trophy_gain(winner, trophy):
    if winner == "Player":
        finalTrophy = trophy + 50
        return finalTrophy
    elif winner == "Computer":
        finalTrophy = trophy - 30
        return finalTrophy
    elif winner == "DRAW":
        finalTrophy = trophy
        return finalTrophy
