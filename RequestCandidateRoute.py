class RequestCandidateRoute:
    def __init__(self):
        self.positionVectorList = []
    
    def appendPositionVector(self, positionVector):
        self.positionVectorList.append(positionVector)
    
    def calcCost(self):
        minD = min([len(i) for i in self.positionVectorList])
        return [minD/len(i) for i in self.positionVectorList]
