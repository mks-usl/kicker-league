import numpy
import functions


def game(player1, player2, result):
    # result: 1 => player1 won, 0 => player1 lost

    k = 80
    rat1 = player1.rating
    rat2 = player2.rating
    R = [rat1, rat2]

    # set the result
    S = numpy.zeros(2)
    if result:
        S = [1, 0]
        player1.wins += 1
        player2.losses += 1
    else:
        S = [0, 1]
        player2.wins += 1
        player1.losses += 1

    # compute the expected value
    p = (R[1] - R[0]) / 400
    E = numpy.zeros(2)
    E[0] = 1 / (1 + 10 ** p)
    E[1] = 1 - E[0]

    # compute the new ratings

    # R_new = round.(Int, R. + k. * (S. - E))

    R_new = numpy.zeros(2)
    for i in range(len(R)):
        R_new[i] = R[i] + k * (S[i] - E[i])
    R_new = list(map(round, R_new))

    player1.rating = R_new[0]
    player2.rating = R_new[1]
    return player1, player2


def games(pl1, pl2, streak):  # streak w.r.t. player_1
    s = functions.conv_results(streak)
    for i in range(len(streak)):
        pl1, pl2 = game(pl1, pl2, s[i])
    return pl1, pl2

