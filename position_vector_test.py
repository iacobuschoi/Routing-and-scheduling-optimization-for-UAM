from candidate_routes_gen import Dijkstra
from graph import Graph, Node
from path_to_posvec import path_to_posvec

G = Graph()
dijkstra = Dijkstra(G,0,5)

print("===== candidate routes =====")
candidateRoutes = dijkstra.getCandidateRoutes()
for routes in candidateRoutes:
    for i in range(len(routes)-1):
        print(routes[i].pos, end = ' ->')
    print(routes[-1].pos)
print("")

print("===== candidate routes position vector =====")
for i, routes in enumerate(candidateRoutes):
    print(f"[candidate {i+1}]")
    pos_vec = path_to_posvec(routes, 0.0)
    for t, x, y in pos_vec:
        print(f"t={t:.2f}: ({x:.2f}, {y:.2f})")
    print("")

# Input EX
# 6 8
# 0 0
# 0 13
# 11 0
# 15 10
# 12 21
# 22 14
# 0 1
# 0 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 5
# 4 5