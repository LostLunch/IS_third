from pickletools import read_unicodestring1
from .node import Node

class Edge:
    def __init__(self, u : Node, v: Node, base_weight : float = 1.0):
        self.u = u #출발 노드
        self.v = v #도착 노드
        self.base_weight = base_weight
        self.dynamic_weight = 0
    
    @property
    def weight(self) -> float:
        return self.base_weight + self.dynamic_weight

    def update_dynamic_weight(self, add_weight : float):
        self.dynamic_weight = max(0.0,add_weight) #가중치 음수 방지지
    
    def __repr__(self):
        return f"Edge({self.u.id} -> {self.v.id}, weight={self.weight})"