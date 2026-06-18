import dynamic_parking as dp

def main():
    matrix,car_pos = dp.parse_txt("dynamic_parking_project/examples/map_example/map3.txt")
    grid = dp.ParkingGrid(matrix)
    graph = dp.convert_grid_to_graph(grid)

    #planner = dp.dijkstra
    planner = dp.astar
    #planner = dp.DStarLite.dstar_lite_search

    empty_pos = set()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get_type(x,y) == 2:
                empty_pos.add((x,y,0))
    start_1 = car_pos[0]
    start_2 = car_pos[1]

    agent_1 = dp.Agent(1, graph, start_1, planner)
    agent_2 = dp.Agent(2, graph, start_2, planner)

    env = dp.Environment(graph, [agent_1,agent_2], congestion_radius=1, congestion_weight=1.0)

    reserved = set()
    
    print(agent_1)
    print(agent_2)
    print("-----")

    while not (agent_1.is_parked() and agent_2.is_parked()):
        if not empty_pos:
            print("주차 공간이 부족합니다!")
            break
        env.update()

        if agent_1.is_parked():
            empty_pos.discard(agent_1.current_node)
        if agent_2.is_parked():
            empty_pos.discard(agent_2.current_node)

        if not agent_1.is_parked():
            target_1 = dp.search_parking_pos(agent_1.current_node, empty_pos - reserved, graph)

            if target_1 is not None:
                reserved.add(target_1)
                agent_1.plan(target_1)

        if not agent_2.is_parked():
            target_2 = dp.search_parking_pos(agent_2.current_node, empty_pos - reserved, graph)

            if target_2 is not None:
                reserved.add(target_2)
                agent_2.plan(target_2)

        agent_1.move()
        agent_2.move()

        print(agent_1)
        print(agent_2)
        print("-----")

    print("도착 완료!")
    print(f"Agent 1 총 이동 횟수: {agent_1.move_count}, 총 비용: {agent_1.total_cost}, 최종 위치: {agent_1.current_node}")
    print(f"Agent 2 총 이동 횟수: {agent_2.move_count}, 총 비용: {agent_2.total_cost}, 최종 위치: {agent_2.current_node}")

if __name__ == "__main__":
    main()