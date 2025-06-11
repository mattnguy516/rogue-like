class Action:
    pass

# when we hit the "Esc" key to exit the game
class EscapeAction(Action):
    pass

# Player movement actions
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        
        self.dx = dx
        self.dy = dy