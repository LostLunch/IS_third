import dynamic_parking as dp


class Agent:
    def __init__(self, id : int, graph : dp.Dynamic_graph, start : tuple[int, int, int], planner):
        self.id = id
        self.graph = graph
        self.current_node = start
        self.planner = planner
        self.path = []
        self.target = None
        self.move_count = 0
        self.total_cost = 0

    def plan(self, target : tuple[int, int, int]):
        self.target = target
        self.path, _ = self.planner(self.graph, self.current_node, self.target)

    def move(self):

        if len(self.path) > 1:

            next_node = self.path[1]

            edge = self.graph.adj_list[self.current_node][next_node]

            self.total_cost += edge.weight
            self.current_node = next_node
            self.path.pop(0)
            self.move_count += 1

    def is_parked(self):
        return self.current_node == self.target
    
    def __repr__(self):
        return (
            f"Agent("
            f"id={self.id}, "
            f"current={self.current_node}, "
            f"target={self.target}"
            f")"
        )