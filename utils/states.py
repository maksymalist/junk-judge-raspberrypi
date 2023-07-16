from enum import Enum

class State(Enum):
    INIT = 0
    IDLE = 1
    ACTIVE = 2
    CONFUSED = 3
    DONE = 4