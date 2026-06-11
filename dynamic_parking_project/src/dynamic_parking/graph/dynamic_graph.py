from typing import Tuple, Dict, List
from .edge import Edge
from .node import Node

coordinate = tuple[int,int,int]

class Dynamic_graph:
    def __init__(self) -> None:
        self.nodes : Dict[coordinate,Node] = {}
        self.adj_list : Dict[coordinate, Dict[coordinate, Edge]] = {} #이중 딕셔너리

    def add_node(self, x : int, y : int, z : int = 0) -> Node:
        node = Node(x,y,z)
        if node.id not in self.nodes: #중복 방지
            self.nodes[node.id] = node
            self.adj_list[node.id] = {}
        return self.nodes[node.id] #사용자의 작업 편의성을 위해 return을 함
    
    def add_edge(self, u_id : coordinate, v_id : coordinate, base_weight : float = 1.0):
        if u_id not in self.nodes or v_id not in self.nodes:
            raise ValueError("그래프에 존재하지 않는 노드 간의 간선은 생성할 수 없습니다.")
        
        u_node = self.nodes[u_id]
        v_node = self.nodes[v_id]
        edge = Edge(u_node,v_node,base_weight)

        self.adj_list[u_id][v_id] = edge
    
    def get_neighbors(self,node_id : coordinate) -> list[Tuple[coordinate, float]]:
        neighbors = []

        for v_id, edge in self.adj_list[node_id].items():
            neighbors.append((v_id, edge.weight))
        return neighbors
    
    def get_predecessors(self, node_id):
        predecessors = []

        for u_id, neighbors in self.adj_list.items():

            if node_id in neighbors:
                predecessors.append(u_id)

        return predecessors
        
    def update_edge_weight(self, u_id : coordinate, v_id : coordinate, add_weight : float):
        if u_id in self.adj_list and v_id in self.adj_list[u_id]:
            self.adj_list[u_id][v_id].update_dynamic_weight(add_weight)