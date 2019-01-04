import hashlib

class Outcome:
    name = ""
    odds = 0

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def winAmount(self, amount):
        totalAmount = amount * self.odds
        return totalAmount

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        hashValue = int(hashlib.sha256(self.name.encode('utf-8')).hexdigest(), 16) % 10**8
        return hashValue

    def __str__(self):
        return "{0} ({1}:1)".format(self.name, self.odds)

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self.name, self.odds )


############# TESTING #############
def test_init_eq():
    outcome_1 = Outcome("Split-Bet", 17)
    outcome_2 = Outcome("Split-Bet", 1)
    outcome_3 = Outcome("Any Craps", 8)
    assert outcome_1 == outcome_2
    assert outcome_2 != outcome_3

def test_hash():
    outcome_1 = Outcome("Split-Bet", 17)
    outcome_2 = Outcome("Split-Bet", 1)
    outcome_3 = Outcome("Any Craps", 8)
    assert hash(outcome_1) == hash(outcome_2)

def test_winAmount():
    outcome_1 = Outcome("Split-Bet", 17)
    outcome_2 = Outcome("Split-Bet", 1)
    assert outcome_1.winAmount(2) == 34
    assert outcome_2.winAmount(3) == 3
