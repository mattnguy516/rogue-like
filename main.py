#!/usr/bin/end python3
import tcod

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
            
            # Waits for some input from the user
            # aka us hitting the x button on the window
            # to exit the current running program
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()
    
if __name__ == "__main__":
    main()