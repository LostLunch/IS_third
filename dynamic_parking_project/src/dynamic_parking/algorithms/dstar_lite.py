import heapq
from math import inf

class DStarLite:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

        # g: 실제 측정된 경로 비용, rhs: 주변 정보를 통해 예측된 기대 비용
        self.g = {node: inf for node in graph.nodes}
        self.rhs = {node: inf for node in graph.nodes}
        self.rhs[goal] = 0  # 목적지에서 시작하므로 목적지의 기대 비용은 0

        self.U = {}  # 큐 내부 노드의 유효성 상태 저장 (중복 방지 및 최신화 체크)
        self.pq = [] # 우선순위 큐 (가장 수선이 시급한 노드부터 추출)
        self.counter = 0 # 가중치가 같을 때 노드 이름 대신 들어온 순서로 비교하기 위한 카운터

        self.insert(goal) # 목적지부터 역으로 탐색하기 위해 큐에 삽입

    def heuristic(self, node, next_node):
        x, y, _ = node
        next_x, next_y, _ = next_node
        return abs(x - next_x) + abs(y - next_y)

    def calculate_key(self, u):
        k = min(self.g[u], self.rhs[u])
        return (k + self.heuristic(u, self.start), k)

    def insert(self, u):
        # 기존에 큐에 있던 데이터는 무효화
        if u in self.U:
            self.U[u] = False

        key = self.calculate_key(u)
        # (우선순위, 카운터, 노드이름) 순으로 큐에 삽입
        heapq.heappush(self.pq, (key, self.counter, u))
        self.U[u] = True # 현재 노드가 큐에서 '유효함'을 표시
        self.counter += 1

    def update_vertex(self, u):
        # 노드 u의 상태가 변했을 때(주변 가중치 변경 등) rhs 값을 다시 계산
        if u != self.goal:
            min_rhs = inf
            # 모든 이웃 노드(v)를 확인하여 'v까지의 거리 + 연결 가중치(w)'의 최솟값 계산
            for v, w in self.graph.get_neighbors(u):
                if self.g[v] + w < min_rhs:
                    min_rhs = self.g[v] + w
            self.rhs[u] = min_rhs # 새로운 기대 비용 저장

        # 기존 큐에 있던 정보는 낡은 것이므로 무효화
        if u in self.U and self.U[u]:
            self.U[u] = False

        # g(실제)와 rhs(기대)가 다르면 정보가 불일치하므로, 수선을 위해 큐에 삽입
        if self.g[u] != self.rhs[u]:
            self.insert(u)

    def compute_shortest_path(self, current_pos, max_iter=200):
        #에이전트의 현재 위치까지의 경로가 안정화될 때까지 반복적으로 수선 작업 진행
        count = 0
        while self.pq and count < max_iter:
            # 큐의 맨 앞(가장 우선순위가 높은) 노드의 키값 확인
            key, _, u = self.pq[0]

            # 종료 조건: 현재 위치의 비용이 안정화(g==rhs)되었고, 더 이상 확인할 유망한 노드가 없을 때
            if key >= self.calculate_key(current_pos) and self.rhs[current_pos] == self.g[current_pos]:
                break

            key, _, u = heapq.heappop(self.pq) # 수선할 노드 추출

            # 이미 무효화된(최신 데이터가 아닌) 노드라면 무시하고 다음으로 진행
            if not self.U.get(u, False):
                continue

            self.U[u] = False # 추출된 노드는 이제 큐에 없음
            count += 1

            if self.g[u] > self.rhs[u]:
                # 1. 지름길 발견: 실제 비용을 기대 비용으로 맞춤
                self.g[u] = self.rhs[u]
                # 영향을 받는 주변 노드들도 업데이트 대상에 포함
                for pred in self.graph.get_predecessors(u):
                    self.update_vertex(pred)
            else:
                # 2. 길이 막힘: 실제 비용을 무한대로 돌리고 재계산
                self.g[u] = inf
                for pred in self.graph.get_predecessors(u):
                    self.update_vertex(pred)
                self.update_vertex(u) # 자기 자신도 다시 계산

    def get_next(self, current):
        # 현재 위치에서 목적지까지 가기 위한 최적의 다음 노드 결정
        if current == self.goal:
            return current

        best_next = None
        min_cost = inf

        # 모든 이웃을 살펴보고 '이웃까지의 가중치 + 이웃에서 목적지까지의 g값'이 최소인 곳 선택
        for neighbor, weight in self.graph.get_neighbors(current):
            cost = weight + self.g[neighbor]
            if cost < min_cost:
                min_cost = cost
                best_next = neighbor

        return best_next if best_next else current
    
    def get_path(self):
        self.compute_shortest_path(self.start)

        current = self.start
        path = [current]

        while current != self.goal:

            next_node = self.get_next(current)

            if next_node == current:
                return []

            path.append(next_node)
            current = next_node

        return path
    
    def dstar_lite_search(self,graph, start, goal):
        planner = DStarLite(graph, start, goal)

        path = planner.get_path()

        cost = planner.get_cost()

        return path, cost