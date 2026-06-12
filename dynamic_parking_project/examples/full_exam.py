import dynamic_parking as dp

def main():
    matrix = dp.parse_txt("D:\\Github_repo\\IS_third\\dynamic_parking_project\\examples\\txt_map.txt")
    grid = dp.ParkingGrid(matrix)
    graph = dp.convert_grid_to_graph(grid)

    empty_pos = set()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get_type(x,y) == 2:
                empty_pos.add((x,y,0))
    start = (12,4,0)
    goal = dp.search_parking_pos(start, empty_pos, graph)
    print("탐색한 결과:", goal)

    djkstra_path = dp.dijkstra(graph, start, goal)
    print("Dijkstra 탐색 결과:", djkstra_path)

    astar_path = dp.astar(graph, start, goal)
    print("A* 탐색 결과:", astar_path)

    dstar_lite_path = dp.DStarLite(graph, start, goal).get_path()
    print("D* Lite 탐색 결과:", dstar_lite_path)

if __name__ == "__main__":
    main()
