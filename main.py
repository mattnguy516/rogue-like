#!/usr/bin/end python3
import copy

import tcod

from engine import Engine
import entity_factories
from input_handlers import EventHandler
from procgen import generate_dungeon

"""
responsible for:
    - Setting up the intial variables, like screen size and the tileset
    - Creating the entities
    - Drawing the Screen and everything on it
    - Reacting to the player's input
"""
def main():
    # defining some variables for the screen size
    screen_width = 80
    screen_height = 50
    
    map_width = 80
    map_height = 45
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    max_monsters_per_room = 2
    

    # loading values from our JSON file
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    event_handler = EventHandler()
    
    player = copy.deepcopy(entity_factories.player)
    
    game_map = generate_dungeon(
        max_rooms = max_rooms,
        room_min_size = room_min_size,
        room_max_size = room_max_size,
        map_width = map_width,
        map_height = map_height,
        max_monsters_per_room = max_monsters_per_room,
        player = player
    )
    
    engine = Engine(event_handler = event_handler, game_map = game_map, player = player)
    
    # telling tcod what font to use
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        # creates our "console" which is what we'll be drawing to
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console = root_console, context = context)
            # What actually updates the screen with what
            # we've told it to display so far
            events = tcod.event.wait()
            # Clears the console after being drawn to so we don't leave
            # a trail behind of the same character like snake
            engine.handle_events(events)
            
if __name__ == "__main__":
    main()