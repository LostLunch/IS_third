import dynamic_parking as dp

class Environment:
    def __init__(self, graph : dp.Dynamic_graph, agents : list[dp.Agent],congestion_radius : int = 1, congestion_weight : float = 1.0):
        self.graph = graph
        self.agents = agents

        self.congestion_radius = congestion_radius
        self.congestion_weight = congestion_weight
    
    def reset_congestion(self):
        for u_id, edges in self.graph.adj_list.items():
            for v_id, edge in edges.items():
                edge.update_dynamic_weight(0.0)
    
    def apply_congestion(self):
        radius = self.congestion_radius

        affected = set()

        for agent in self.agents:
            x, y, _ = agent.current_node

            for dx in range(-radius, radius+1):
                for dy in range(-radius, radius+1):
                    node = (x+dx, y+dy, 0)
                    if node in self.graph.nodes:
                        affected.add(node)
            
            for u in affected:
                for v_id in self.graph.adj_list[u]:
                    if v_id in affected:
                        self.graph.update_edge_weight(u,v_id,self.congestion_weight)
    
    def update(self):
        self.reset_congestion()
        self.apply_congestion()
                    