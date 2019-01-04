from Outcome import Outcome
class Bin(frozenset):
    pass




############# TESTING #############
def test_init_shared():
    outcome_1 = Outcome("00-0-1-2-3", 6)
    outcome_2 = Outcome("Split-Bet", 17)
    outcome_3 = Outcome("Any Craps", 8)
    outcome_4 = Outcome("Split-Bet", 1)
    bin_1 = Bin([Outcome("0", 35), outcome_2, outcome_3])
    bin_2 = Bin([Outcome("Straight-Bet", 12)])
    assert outcome_2 in bin_1 and outcome_3 in bin_1
    assert outcome_2 == outcome_4
