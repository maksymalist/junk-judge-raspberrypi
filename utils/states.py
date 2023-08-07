from enum import Enum

class State(Enum):
    INIT = "Initializing"
    IDLE = "Idle"
    ACTIVE = "Active"
    CONFUSED = "Confused"
    DONE = "Done"
    
    def __str__(self):
        return self.value