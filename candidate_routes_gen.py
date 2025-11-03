from queue import PriorityQueue

class Dijkstra:
    def __init__(self, G, startID, destID):
        # dijkstra parameters
        self.G = G
        self.INF = 1e9
        self.V = G.cnt
        self.edgeList = G.getEdgelist()
        self.dist = []
        self.parent = [] # parent table for path backtracking
        self.dvis = []   # visit table for path backtracking dfs
        self.vis = []    # visit table for Dijkstra
        self.pq = PriorityQueue()    # priority queue for Dijkstra

        self.s = startID
        self.e = destID

        self.candidateRoutes = None
        self.costIncreaseConstant = 5  # cost(i->j) *= costIncreaseConstant for all (i->j) in min path
        self.candidatesNum = 5         # # of candidate routes

        print("===== edge list =====")
        for i in range(self.V):
            for v in self.edgeList[i]:
                print(v, end=',')
            print("")
        print("")

    def initDijkstra(self):
        self.dist = [self.INF] * self.V
        self.parent = [-1] * self.V
        self.vis = [0] * self.V
        self.dvis = [0] * self.V
        self.pq = PriorityQueue()

        self.dist[self.s] = 0
        self.pq.put([0, self.s])

    def updateEdgeCosts(self, path):
        for i in range(len(path) - 1):
            v = path[i]
            u = path[i+1]

            for j in range(len(self.edgeList[v])):
                if self.edgeList[v][j][0] == u:
                    self.edgeList[v][j][1] *= self.costIncreaseConstant
                    break

            for j in range(len(self.edgeList[u])):
                if self.edgeList[u][j][0] == v:
                    self.edgeList[u][j][1] *= self.costIncreaseConstant
                    break

    def dijkstra(self):
        path = []
        while not self.pq.empty():
            curr=self.pq.get()[1]
            if self.vis[curr]:
                continue
            self.vis[curr] = 1

            for next in self.edgeList[curr]:
                ndist = self.dist[curr] + next[1]
                if ndist < self.dist[next[0]]:
                    self.dist[next[0]] = ndist
                    self.parent[next[0]] = curr
                    self.pq.put([ndist, next[0]])

        curr = self.e
        while curr != self.s:
            path.append(curr)
            curr = self.parent[curr]
        path.append(self.s)
        return path 
    
    def getPath(self):
        self.initDijkstra()
        path = self.dijkstra()
        self.updateEdgeCosts(path)
        path.reverse()
        pathByNode = [self.G.nodes[id] for id in path]
        return pathByNode
    
    def getCandidateRoutes(self):
        if self.candidateRoutes != None:
            return self.candidateRoutes
        
        self.candidateRoutes = []
        for _ in range(self.candidatesNum):
            self.candidateRoutes.append(self.getPath())
        return self.candidateRoutes
    
    # def requestGeneration(self):
        # 구현 필요

        
# G = Graph()
# dijkstra = Dijkstra(G,0,5)

# print("===== candidate routes =====")
# for routes in dijkstra.getCandidateRoutes():
#     for i in range(len(routes)-1):
#         print(routes[i].pos, end = ' ->')
#     print(routes[-1].pos)
# print("")

# Input EX
# 6 8
# 0 0
# 0 1
# 1 0
# 1 1
# 1 2
# 2 1
# 0 1
# 0 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 5
# 4 5

