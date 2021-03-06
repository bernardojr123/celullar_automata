class Cell:
    
    def __init__(self, state, x, y):
        self.position = (x, y)
        self.state = state
        self.next_state = state
        self.__counter_state = 1

    def update_state(self):
        if self.next_state == self.state:
            self.__counter_state += 1
            return
        self.state = self.next_state
        self.__counter_state = 0

    def get_counter_state(self):
        return self.__counter_state