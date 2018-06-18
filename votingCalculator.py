class VotingCalculator:

    maxMotoSteps = 512/2
    currentMotoPositionInPercent = 50
    currentLikeVote = 0
    currentDisLikeVote = 0

    def __init__(self):
        self.maxMotoSteps = 512 / 2
        self.currentMotoPositionInPercent = 50
        self.currentLikeVote = 0
        self.currentDisLikeVote = 0

    def getMotoSteps(self, vote):
        if vote == "like":
            self.currentLikeVote = self.currentLikeVote + 1
        elif vote == "dislike":
            self.currentDisLikeVote = self.currentDisLikeVote + 1
        else:
            self.currentLikeVote = 1
            self.currentDisLikeVote = 1
        print(" NEW Current Likes : "+str(self.currentLikeVote)+" Current Dislike : "+str(self.currentDisLikeVote))
        likePercent = self.currentLikeVote*100.0/(self.currentLikeVote+self.currentDisLikeVote)
        print("Like in Percent "+str(likePercent)+"%")
        diff = self.currentMotoPositionInPercent - likePercent
        self.currentMotoPositionInPercent = likePercent
        print("Difference last Vote : "+str(diff)+"%")
        if vote == "reset":
            self.currentDisLikeVote = 0
            self.currentLikeVote = 0
            print("NEW 2 Current Likes : "+str(self.currentLikeVote)+" Current Dislike : "+str(self.currentDisLikeVote))
            print("=============================================")
        return self.calculateMotoSteps(diff)

    def calculateMotoSteps(self, gap):
        if(gap < 0):
            gap = gap*-1
            direction = "NCW"
        else:
            direction = "CW"
        return str(round((VotingCalculator.maxMotoSteps/100.0*gap),1))+direction