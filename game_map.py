import numpy as np # type: ignore
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        """
        We create a 2D array, filled with the same values, which in this case,
        is the tile_types.floor. This will fill self.tiles with floor tiles
        """
        self.tiles = np.full((width, height), fill_value = tile_types.wall, order = "F")
        
        
    # To ensure the player doesn't move out of bounds
    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]