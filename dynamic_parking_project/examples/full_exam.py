from dynamic_parking.graph.dynamic_graph import Dynamic_graph

from dynamic_parking.algorithms.dijkstra import dijkstra
from dynamic_parking.algorithms.astar import astar
from dynamic_parking.algorithms.dstar_lite import DStarLite

print("=== Dynamic Parking Library Test ===")

# --------------------------
# 그래프 생성
# --------------------------

graph = Dynamic_graph()

for x in range(3):
    for y in range(3):
        graph.add_node(x, y)

print(f"노드 수 : {len(graph.nodes)}")

# --------------------------
# 간선 생성
# --------------------------

for x in range(3):
    for y in range(3):

        current = (x, y, 0)

        if x < 2:

            right = (x + 1, y, 0)

            graph.add_edge(current, right, 1)
            graph.add_edge(right, current, 1)

        if y < 2:

            down = (x, y + 1, 0)

            graph.add_edge(current, down, 1)
            graph.add_edge(down, current, 1)

print("간선 생성 완료")

# --------------------------
# 이웃 조회
# --------------------------

print("\n=== Neighbor Test ===")

neighbors = graph.get_neighbors((1, 1, 0))

for node, weight in neighbors:
    print(node, weight)

# --------------------------
# 다익스트라
# --------------------------

start = (0, 0, 0)
goal = (2, 2, 0)

print("\n=== Dijkstra ===")

path = dijkstra(
    graph.adj_list,
    start,
    goal
)

print(path)

# --------------------------
# A*
# --------------------------

print("\n=== A* ===")

path, cost = astar(
    graph,
    start,
    goal
)

print("path =", path)
print("cost =", cost)

# --------------------------
# 가중치 변경
# --------------------------

print("\n=== Weight Update ===")

graph.update_edge_weight(
    (1, 0, 0),
    (2, 0, 0),
    100
)

print(
    graph.get_neighbors(
        (1, 0, 0)
    )
)

# --------------------------
# D* Lite
# --------------------------

print("\n=== D* Lite ===")

planner = DStarLite(
    graph,
    start,
    goal
)

path = planner.get_path()

print(path)

print("\n=== Test Finished ===")