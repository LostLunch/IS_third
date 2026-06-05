from .grid import ParkingGrid
from dynamic_parking.graph.dynamic_graph import Dynamic_graph as DynamicGraph

def convert_grid_to_graph(grid : ParkingGrid) -> DynamicGraph:
    graph = DynamicGraph()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.is_accessible(x, y):
                graph.add_node(x, y)
    
    # 노드 간의 간선 추가 (상하좌우)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    z = 0
    for y in range(grid.height):
        for x in range(grid.width):
            current_id = (x, y, z)
            current_type = grid.get_type(x, y)

            if grid.is_accessible(x, y):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    nz = 0
                    next_id = (nx, ny, nz)
                    next_type = grid.get_type(nx, ny)

                    if not grid.is_accessible(nx, ny):
                        continue
                    
                    if current_type == ParkingGrid.PARKING:
                        if next_type == ParkingGrid.PARKING_DIRECTION:
                            graph.add_edge(current_id, next_id, base_weight=1.0)
                    elif current_type == ParkingGrid.STREET:
                        if next_type != ParkingGrid.PARKING:
                            graph.add_edge(current_id, next_id, base_weight=1.0)
                    else:
                        graph.add_edge(current_id, next_id, base_weight=1.0)
    return graph