from game.actor import Actor
class Player:
def __init__(self):
        """Constructs a player."""
        self._text = ""
        self._font_size = 15
        self._color = WHITE
        self._position = Point(0, 0)

  def get_color(self):
      """Gets the player's color which is WHITE."""
      return self._color

  def get_font_size(self):
      """Gets the player's font size."""
      return self._font_size

  def get_position(self):
      """Gets the players's position."""
      return self._position

  def get_text(self):
      """Creates the player as the "#" symbol."""
      return self._text

  def move_next(self, max_x, max_y):
      """Moves the player according to the keys that are pressed.
      Args:
          max_x (int): The maximum x value.
          max_y (int): The maximum y value.
      """
      x = self._position.get_x() % max_x
      y = self._position.get_y() % max_y
      self._position = Point(x, y)
