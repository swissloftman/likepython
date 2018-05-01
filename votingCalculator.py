class VotingCalculator:

    maxMotoSteps = 512/2 # Eine Umdrehung ca. 512 Steps. Da ich nur up and down brauche die hälfts

    currentMotoPositionInPercent = 0

    currentLikeVote = 0

    currentDisLikeVote = 0


    def getMotoSteps(vote):
        if vote == "like":
            VotingCalculator.currentLikeVote = VotingCalculator.currentLikeVote + 1
        else:
            VotingCalculator.currentDisLikeVote = VotingCalculator.currentDisLikeVote + 1
        percent = VotingCalculator.currentLikeVote/(VotingCalculator.currentLikeVote+VotingCalculator.currentDisLikeVote)
        diff = VotingCalculator.currentMotoPositionInPercent - percent
        return VotingCalculator.calculateMotoSteps(diff)

    def calculateMotoSteps(gap):
        if(gap < 0):
            gap = gap*-1
            direction = "NCW"
        else:
            direction = "CW"
        return (VotingCalculator.maxMotoSteps/100*gap)+direction