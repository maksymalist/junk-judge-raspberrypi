from enum import Enum

class State(Enum):
    INIT = 0
    IDLE = 1
    OPEN = 2
    ACTIVE = 3
    CONFUSED = 4
    DONE = 5