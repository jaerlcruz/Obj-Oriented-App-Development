"""PROBLEM 1"""


def hello(subject):
  # todo
  return f"Hello, {subject}!"


"""PROBLEM 2"""


class Bug:

  def __init__(self, name, position=[0, 0]):
    """
    initializes a Bug object w/ given name and position. Position defaults to (0,0) if none is provided.
    INPUT:
      - name: string type for the name
      - position: list of xy-coordinates where first element is x-coordinate, second is y-coordinate
    """
    # todo
    self.name = name
    self.position = position

  def move_up(self, units):
    """
    moves this Bug object's position up by the given number of units
    INPUT:
      - units: int type; the number of units by which the bug Bug's position is moved
    """
    self.position[1] += units
    return

  def move_down(self, units):
    self.position[1] -= units
    return

  def move_left(self, units):
    self.position[0] -= units
    return

  def move_right(self, units):
    self.position[0] += units
    return

  # todo: implement accessor and mutator methods

  def __str__(self):
    return f"Name: {self.name}\nPosition: ({self.position[0]}, {self.position[1]})"
