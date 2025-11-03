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
    