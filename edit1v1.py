import pandas
from datetime import datetime
import numpy
from player import Player
from functions import *


def edit1v1(spreadsheet):
    ks = spreadsheet
    ks1v1 = ks.get_worksheet(0)
    ranks1v1 = ks.get_worksheet(2)

    data1v1 = ks1v1.get_all_records()
    df_1v1 = pandas.DataFrame.from_dict(data1v1)

    # extract unique names from the playing data
    names = list(df_1v1['Player 1']) + list(df_1v1['Player 2'])
    for i in range(len(names)):
        names[i] = names[i].strip()
    names = list(set(names))
    # create player dictionary
    d = init_players(names)

    # play elo games
    for i in range(len(df_1v1.index)):
        r = get_row(df_1v1, i)
        if r[2] > r[3]:
            result = 1
        else:
            result = 0
        d[r[0]], d[r[1]] = game(d[r[0]], d[r[1]], result)

    # create a sorted list of players
    players = sorted(list(d.values()), reverse=True)

    # update cells in the 1v1 ratings
    for i in range(len(players)):
        ranks1v1.update_cell(i + 2, 1, i + 1)
        ranks1v1.update_cell(i + 2, 2, players[i].name)
        ranks1v1.update_cell(i + 2, 3, players[i].rating)

    # output update time
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ranks1v1.update_cell(2, 5, now)
