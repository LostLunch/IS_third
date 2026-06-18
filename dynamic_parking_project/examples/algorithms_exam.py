from dynamic_parking.graph.dynamic_graph import Dynamic_graph
from dynamic_parking.algorithms.dstar_lite import DStarLite
from dynamic_parking.algorithms.astar import astar
from dynamic_parking.algorithms.dijkstra import dijkstra

graph = Dynamic_graph()

# 노드 생성
for x in range(3):
    for y in range(3):
        graph.add_node(x, y)

# 간선 생성 (양방향)
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

start = (0, 0, 0)
goal = (2, 2, 0)

planner = DStarLite(
    graph,
    start,
    goal
)

path1 = planner.get_path()
path2 = astar(graph, start, goal)[0]
path3 = dijkstra(graph, start, goal)[0]
print("path dstarlite:", path1)
print("path a*: ", path2)
print("path dijkstra: ", path3)