class Node():
    def __init__(self,pos):
        self.pos = pos # [x, y]
        self.id = id   # index of nodes in Graph
        self.adj = []  # list of adjoint nodes' ID

class Graph():
    def __init__(self):
        self.nodes = []
        self.cnt = 0
        self.build()

    def build(self):
        print("===== build Graph =====")
        V, E = map(int,input("[insert] V E: ").split()) # V: # of nodes, E: # of edges
        
        print("\n[build Nodes]")
        for _ in range(V):
            self.insertNode(list(map(int, input("[insert] x y: ").split())))

        print("\n[build Edges]")
        for _ in range(E):
            i, j = map(int, input("[insert] i j: ").split())
            self.insertEdge(i, j)
        
        self.log()

    def insertNode(self, pos): # pos: nodes position in cartesian space
        newNode = Node(pos)
        newNode.id = self.cnt
        self.cnt += 1
        self.nodes.append(newNode)

    def insertEdge(self, i,j): # i,j: ID of nodes to connect
        if max(i, j) >= self.cnt:
            raise IndexError("index out of range.")
        
        self[i].append(j)
        if i != j:
            self[j].append(i)

    def cost(self, i, j): # return distance between two nodes
        if max(i, j) >= self.cnt:
            raise IndexError("index out of range.")
        
        u = self.nodes[i].pos
        v = self.nodes[j].pos
        return ((u[0] - v[0])**2 + (u[1] - v[1])**2)**0.5
    
    def __getitem__(self, key): # iter fuction. can be used as edge-list
        if key >= self.cnt:
            raise IndexError("index out of range.")
        
        return self.nodes[key].adj

    def log(self):
        print("\n===== Graph log =====")
        print("[nodes cnt]", self.cnt)
        
        print("\n[nodes position]")
        for node in self.nodes:
            print(node.id,":",node.pos)
        
        print("\n[Edges]")
        for node in self.nodes:
            for nextNodeID in node.adj:
                print(node.id, "->", nextNodeID, ":", self.cost(node.id, nextNodeID))
        print("")

    def getEdgelist(self):
        edgeList=[[] for _ in range(self.cnt)]
        for node in self.nodes:
            for nextNodeID in node.adj:
                edgeList[node.id].append([nextNodeID,self.cost(node.id,nextNodeID)])
        return edgeList

## build Input ex
# 4 4
# 0 1
# 1 1
# 2 2
# -1 1
# 0 2
# 1 1
# 1 2
# 3 0

# G.insertNode([1,0])
# G.insertNode([1,1])
# G.insertNode([1,2])
# G.insertNode([1,3])

# G.insertEdge(0,2)
# G.insertEdge(1,1)
# G.insertEdge(1,2)
# G.insertEdge(3,1)