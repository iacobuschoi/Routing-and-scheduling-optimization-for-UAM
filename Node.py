class Node():
    def __init__(self,pos):
        self.pos = pos # [x, y]
        self.id = id   # index of nodes in Graph
        self.adj = []  # list of adjoint nodes' ID

