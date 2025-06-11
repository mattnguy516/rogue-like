#!/usr/bin/end python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main():
    # defining some variables for the screen size
    screen_width = 80
    screen_height = 50
    
    player_x = int (screen_width / 2)
    player_y = int(screen_width / 2)
    
    # loading values from our JSON file
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    event_handler = EventHandler()
    
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
            root_console.print(x=player_x, y=player_y, string="@")
            # What actually updates the screen with what
            # we've told it to display so far
            context.present(root_console)
            # Clears the console after being drawn to so we don't leave
            # a trail behind of the same character like snake
            root_console.clear()
            
            # Waits for some input from the user
            # aka us hitting the x button on the window
            # to exit the current running program
            for event in tcod.event.wait():
                # Creating an instance of our EventHandler class
                # we'll use it to receive events and process them
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                    
                elif isinstance(action, EscapeAction):
                    raise SystemExit()
if __name__ == "__main__":
    main()