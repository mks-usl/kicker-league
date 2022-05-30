class Player:
    name = None
    rating = None
    wins = None
    losses = None

    def __init__(self, name):
        self.name = name
        self.rating = 1200
        self.wins = 0
        self.losses = 0

    def __repr__(self):
        return self.name + " (" + str(self.rating) + ")"

    def __lt__(self, other):
        return self.rating < other.rating

    def reset(self):
        self.name = None

