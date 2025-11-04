class ActiveFlightRoute():
    def __init__(self):
        self.positionVectorList=[]

    def append(self,positionVector):
        self.positionVectorList.append(positionVector.vector)

    def update(self,positionVector):
        initTime=positionVector.initTime
        for active in self.positionVectorList:
            if active.arrivedTime <= initTime:
                self.positionVectorList.remove(active)