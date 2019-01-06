from Outcome import Outcome
from Bin import Bin
from Wheel import Wheel

class BinBuilder:
    wheel = Wheel()
    def __init__(self):
        pass

    def buildBins(self, wheel):
        pass

    def straightBet(self):
        for number in range(1, 37):
             bin = Bin([Outcome(str(number), 35)])
             self.wheel.addOutcomes(number, bin)

        self.wheel.addOutcomes(0, Outcome(str(0), 35))
        self.wheel.addOutcomes(37, Outcome(str(00), 35))

        return self.wheel.bins

    def splitBet(self):
        #left-right pairs which has form {n, n +1}
        for rows in range(0, 12):
            colFirst = 3 * rows + 1
            bin_1 = Bin([Outcome("Split " + str(colFirst) + "-" + str(colFirst+1), 17)])
            bin_2 = Bin([Outcome("Split " + str(colFirst) + "-" + str(colFirst+1), 17)])
            self.wheel.addOutcomes(rows, bin_1)
            self.wheel.addOutcomes(rows+1, bin_2)
            colSecond = 3 * rows + 2
            bin_3 = Bin([Outcome("Split " + str(colSecond) + "-" + str(colSecond+1), 17)])
            bin_4 = Bin([Outcome("Split " + str(colSecond) + "-" + str(colSecond+1), 17)])
            self.wheel.addOutcomes(rows, bin_3)
            self.wheel.addOutcomes(rows+1, bin_4)

        #up-down pairs which has for {n, n+3}
        for cols in range(1, 34):
            bin_1 = Bin([Outcome("Split " + str(cols) + "-" + str(cols+3), 17)])
            bin_2 = Bin([Outcome("Split " + str(cols) + "-" + str(cols+3), 17)])
            self.wheel.addOutcomes(cols, bin_1)
            self.wheel.addOutcomes(cols+3, bin_2)

        #114 pairs in total
        return self.wheel.bins


    def streetBet(self):
        for rows in (0, 12):
            colFirst = 3 * rows + 1
            bin_1 = Bin([Outcome("Street " + str(colFirst) + "-" + str(colFirst+1) + "-" + str(colFirst+2), 11)])
            bin_2 = Bin([Outcome("Street " + str(colFirst) + "-" + str(colFirst+1) + "-" + str(colFirst+2), 11)])
            bin_3 = Bin([Outcome("Street " + str(colFirst) + "-" + str(colFirst+1) + "-" + str(colFirst+2), 11)])
            self.wheel.addOutcomes(rows, bin_1)
            self.wheel.addOutcomes(rows+1, bin_2)
            self.wheel.addOutcomes(rows+2, bin_3)

        return self.wheel.bins
