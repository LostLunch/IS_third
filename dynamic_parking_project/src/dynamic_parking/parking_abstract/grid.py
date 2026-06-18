class ParkingGrid:
    STREET = 0
    WALL = 1
    PARKING = 2
    PARKING_DIRECTION = 3

    def __init__(self, grid_map: list[list[int]]):
        self.grid_map = grid_map
        self.height = len(grid_map)
        self.width = len(grid_map[0]) if self.height > 0 else 0

    def get_type(self,x : int, y : int) -> int:
        if not (0 <= x < self.width and 0 <= y < self.height):
            return self.WALL
        
        return self.grid_map[y][x]
    
    def is_accessible(self,x : int, y : int) -> bool:
        return self.get_type(x, y) != self.WALL