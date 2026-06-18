from dynamic_parking.graph.dynamic_graph import Dynamic_graph
from heapq import heappop, heappush

def search_parking_pos(current_node, empty_pos : set, graph : Dynamic_graph) -> tuple[int, int, int] | None:
    dist = {}
    origin ={}

    pq = []
    for parking in empty_pos:
        dist[parking] = 0
        origin[parking] = parking
        heappush(pq, (0, parking))
    
    while pq:
        cost, node = heappop(pq)
        if node == current_node:
            return origin[node]
        for v_id, edge in graph.adj_list.get(node,{}).items():
            new_cost = cost + edge.weight

            if new_cost < dist.get(v_id,float("inf")):
                dist[v_id] = new_cost
                origin[v_id] = origin[node]
                heappush(pq, (new_cost, v_id))

    return None