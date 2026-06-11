from dynamic_parking.parking_abstract.parse import parse_txt
from dynamic_parking.parking_abstract.grid import ParkingGrid
from dynamic_parking.parking_abstract.converter import convert_grid_to_graph


def main():

    print("=" * 50)
    print("1. TXT -> 2차원 배열")
    print("=" * 50)

    matrix = parse_txt(r"D:\Github_repo\IS_third\dynamic_parking_project\examples\txt_map.txt")

    for row in matrix:
        print(row)

    print()

    print("=" * 50)
    print("2. ParkingGrid")
    print("=" * 50)

    grid = ParkingGrid(matrix)

    print(f"width  : {grid.width}")
    print(f"height : {grid.height}")

    print()

    print("좌표 타입 확인")

    for y in range(grid.height):
        for x in range(grid.width):
            print(f"({x},{y}) -> {grid.get_type(x,y)}")

    print()

    print("=" * 50)
    print("3. Grid -> Graph")
    print("=" * 50)

    graph = convert_grid_to_graph(grid)

    print(f"노드 개수 : {len(graph.nodes)}")

    edge_count = 0

    for u_id in graph.adj_list:
        edge_count += len(graph.adj_list[u_id])

    print(f"간선 개수 : {edge_count}")

    print("\n=== 노드 목록 ===")
    for node_id in graph.nodes:
        print(node_id)

    print("\n=== 간선 목록 ===")
    for u_id in graph.adj_list:
        for v_id, edge in graph.adj_list[u_id].items():
            print(
                f"{u_id} -> {v_id} "
                f"(base={edge.base_weight}, "
                f"dynamic={edge.dynamic_weight}, "
                f"total={edge.weight})"
        )

    print()

    print("=" * 50)
    print("4. 이웃 관계 확인")
    print("=" * 50)

    for node_id in graph.nodes:

        neighbors = graph.get_neighbors(node_id)

        print(f"\n노드 {node_id}")

        if not neighbors:
            print("  연결 없음")
            continue

        for next_id, weight in neighbors:
            print(f"  -> {next_id} (weight={weight})")

    print()

    print("=" * 50)
    print("5. 특정 규칙 확인")
    print("=" * 50)

    parking_space = (0, 1, 0)
    parking_neighbors = graph.get_neighbors(parking_space)

    print("주차 공간 이웃")
    print(parking_neighbors)

    print("=" * 50)


if __name__ == "__main__":
    main()