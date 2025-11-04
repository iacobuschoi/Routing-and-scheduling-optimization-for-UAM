class MWIS:
    def __init__(self):
        self.requestList = [] 

    def appendRequest(self, request):
        self.requestList.append(request)
    
    def calcCost(self):
        costList = []
        for request in self.requestList:
            costList += request.calcCost()
        
        return costList

    def edgeListGen(self): # edgeList[k] = [i,j] : i and j is connected
        positionVectorList = []
        for request in self.requestList:
            positionVectorList += request.positionVectorList

        n = len(positionVectorList)
        edgeList = []

        for i in range(n-1):
            for j in range(i+1,n):
                if positionVectorList[i].collisionDetect(positionVectorList[j]):
                    edgeList.append([i,j])

        return edgeList

#1