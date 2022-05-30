from player import Player
from game import game


def compare(p1, p2):
    S = [0, 0]
    if p1.rating >= p2.rating:
        S = [1, 0]
        print(p1.name)
        print(p2.name)
    else:
        S = [0, 1]
        print(p2.name)
        print(p1.name)
    return S


def get_rat(pl):
    return pl.rating


def conv_results(streak):  # only ones and zeros
    return list(map(bool, streak))


def init_players(names):
    itms = []
    for i in range(len(names)):
        itms.append((names[i], Player(names[i])))
    return dict(itms)


def player_in_dict(plrs: dict, name: str):
    f = False
    for i in range(len(plrs)):
        if name.lower() == list(plrs.keys())[i].lower():
            f = True
    return f


# takes user input for a player name and checks it in the dict
def input_player(plrs: dict):
    while True:
        p = input("Input 1st player's name: ")
        p = p.lower().capitalize()
        if player_in_dict(plrs, p):
            break
        else:
            print("Unknown player, try again!")
    return plrs[p]


# takes user input for game score and checks its validity
def input_goals(p1, p2):
    while True:
        try:
            g1 = input("Goals scored by " + p1.name + ": ")
            if 0 <= int(g1) <= 10:
                break
            else:
                print("Goal number must be between 0 and 10!")
        except ValueError:
            print("Not a number!")

    while True:
        try:
            g2 = input("Goals scored by " + p2.name + ": ")
            if g2 == g1:
                print("Can't have a tie!")
            elif 0 <= int(g2) <= 10:
                break
            else:
                print("Goal number must be between 0 and 10!")
        except ValueError:
            print("Not a number!")

    return g1, g2


# takes user input to play a game
def input_game(plrs: dict):

    player1 = input_player(plrs)
    player2 = input_player(plrs)

    goals1, goals2 = input_goals(player1, player2)

    if goals1 > goals2:
        result = 1
    elif goals1 < goals2:
        result = 0

    player1, player2 = game(player1, player2, result)

    itms = list(plrs.items())

    for i in range(len(plrs)):
        if itms[i][0] == player1.name:
            itms[i][1].rating = player1.rating

    for i in range(len(plrs)):
        if itms[i][0] == player2.name:
            itms[i][1].rating = player2.rating

    return plrs


def get_row(df, index):
    return list(df.iloc[index])