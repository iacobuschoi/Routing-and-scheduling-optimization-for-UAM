from Request import Request
from queue import PriorityQueue

class RequestPool:
    def __init__(self):
        self.RequestPool=[]    # [ID, Source, Destination, Start time, Latest time]
        self.getRequest()

    def getRequest(self):
        self.insertRequest(0,0,3,0,None)
        self.insertRequest(1,1,2,0,None)
        
    def insertRequest(self, id, source, destination, start_time, latest_time):
        rq=Request(id,source,destination,start_time,latest_time)
        self.RequestPool.append(rq)