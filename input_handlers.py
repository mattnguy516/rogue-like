from typing import Optional

import tcod.event

# importing over the contents of actions.py
from actions import Action, BumpAction, EscapeAction

# subclass of tcod's EventDispatch class
# Allows us to send event to methods based on the type of event
class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    # This method will receive a key press events, and return either 
    # an Action subclass, or None, if no valid key was pressed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        
        key = event.sym
        
        if key == tcod.event.K_UP:
            action = BumpAction(dx = 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx = 0, dy = 1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx = -1, dy = 0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx = 1, dy = 0)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
            
        # no valid key was pressed
        return action