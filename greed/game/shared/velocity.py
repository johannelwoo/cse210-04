class Velocity:
    """
    Velocity Class - handles moving object movement
    """
    def __init__(self):
        """
        Sets up initial values for speed(dx) and direction(dy) of the moving object
        """
        self.dx = 0.0  # Starting speed of 0
        self.dy = -1.0  # Starting speed of -1 (falling)
       
