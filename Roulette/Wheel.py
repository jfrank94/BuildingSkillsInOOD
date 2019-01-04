from Outcome import Outcome
from Bin import Bin
import random
class Wheel:
    bins = tuple(Bin() for i in range(38))
    binArr = []
    rng = random

    def __init__(self):
        pass

    def addOutcomes(self, number, outcome):
        self.binArr.append([number, outcome])
        self.bins = self.binArr

    def next(self):
        return(random.choice(self.bins))

    def get(self, bin):
        return self.bins[bin]

###### Testing #####
def test_init():
    wheel_1 = Wheel()
    outcome_1 = Outcome("Split-Bet", 17)
    outcome_2 = Outcome("Split-Bet", 1)
    outcome_3 = Outcome("Any Craps", 8)
    bin_1 = Bin([Outcome("0", 35), outcome_2, outcome_3])
    bin_2 = Bin([Outcome("Straight-Bet", 12)])
    assert outcome_1 == outcome_2
    assert outcome_2 in bin_1 and outcome_3 in bin_1

def test_add_bins_to_wheel():
    wheel_1 = Wheel()
    outcome_1 = Outcome("Split-Bet", 17)
    outcome_2 = Outcome("Split-Bet", 1)
    outcome_3 = Outcome("Any Craps", 8)
    bin_1 = Bin([Outcome("0", 35), outcome_2, outcome_3])
    bin_2 = Bin([Outcome("Straight-Bet", 12)])
    wheel_1.addOutcomes(1, bin_1)
    wheel_1.addOutcomes(2, bin_2)
    assert bin_1 in wheel_1.bins[0]

def test_random_values():
    wheel_1 = Wheel()
    wheel_1.rng.seed(1)
    random_values = [wheel_1.rng.randint(0, 37) for i in range(10)]
    assert 8 in random_values
