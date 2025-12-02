from Graph import Graph
from Request import Request
from RequestPool import RequestPool
from CandidateRoute import CandidateRoute
from PositionVector import PositionVector
from CandidateRoute import CandidateRoute
from ActiveFlightRoute import ActiveFlightRoute
from RequestCandidateRoute import RequestCandidateRoute
from MWIS import MWIS

num_of_RQs=2
global_time=0

G=Graph()
RQ=RequestPool()
AFR=ActiveFlightRoute()
mwis=MWIS()

for rq in RQ.RequestPool:
    if rq.start_time==global_time:
        CR=CandidateRoute(G,rq.source,rq.destination)
        cr=CR.getCandidateRoutes()
        RCR=RequestCandidateRoute()
        for path in cr:
            p=PositionVector(global_time,path)
            if p.collision_detect_with_activate(AFR):
                continue
            RCR.appendPositionVector(p)
        mwis.appendRequest(RCR)

mwis_edge=mwis.edgeListGen()
print(mwis_edge)