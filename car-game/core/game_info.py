import time

class GameInfo:
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    @property
    def game_finished(self):
        return self.level > GameInfo.LEVELS

    @property
    def level_time(self):
        if not self.started:
            return 0
        current_time = time.time()
        return round(current_time - self.level_start_time)
