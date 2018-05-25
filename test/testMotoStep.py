#only 4 test

from random import randint
from votingCalculator import VotingCalculator

import time

if __name__ == '__main__':
    calc = VotingCalculator()
    for i in range(1,1000):
        value = randint(0, 999)
        time.sleep(10)
        like = value%2
        if(like == 1):
            print("LIKE")
            print("Steps "+calc.getMotoSteps("like"))
        else:
            print("DISLIKE")
            print("Steps "+calc.getMotoSteps("dislike"))