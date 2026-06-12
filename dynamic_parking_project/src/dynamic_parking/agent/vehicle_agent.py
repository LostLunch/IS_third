import dynamic_parking as dp


class Agent:
    def __init__(self, id : int, graph : dp.Dynamic_graph, start : tuple[int, int, int], planner):
        self.id = id
        self.graph = graph
        self.start = start
        self.current_node = start
        self.planner = planner
        self.path = []
        self.target = None
        self.move_count = 0
        self.total_cost = 0

    def plan(self, target : tuple[int, int, int]):
        self.target = target
        self.path, self.total_cost = self.planner(self.graph, self.start, self.target)

    def move(self):

        if len(self.path) > 1:

            next_node = self.path[1]

            edge = self.graph.get_edge(self.current_node, next_node)

            self.total_cost += edge.weight
            self.current_node = next_node
            self.path.pop(0)
            self.move_count += 1

    def is_parked(self):
        return self.current_node == self.target