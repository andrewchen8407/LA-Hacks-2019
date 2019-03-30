class Human:
    def __init__(self, name, id, balance, health, entertainment, food, luxury, alive = True):
        self._name = name
        self._id = id
        self._balance = balance
        self._health = health
        self._entertainment = entertainment
        self._food = food
        self._luxury = luxury
        self.alive = alive
    def set_health(self, health):
        self._health = health
    def get_health(self):
        return self._health
    def set_entertainment(self, entertainment):
        self._entertainment = entertainment
    def get_entertainment(self):
        return self._entertainment
    def set_food(self, food):
        self._food = food
    def get_food(self):
        return self._food
    def set_luxury(self, luxury):
        self._luxury = luxury
    def get_luxury(self):
        return self._luxury
    def update_status(self):
        if self._health < 30:
            self.alive = False
        elif self._entertainment < 5:
            self.alive = False
        elif self._luxury > self._health+self._food:
            self.alive = False
        elif self._food < 20:
            self.alive = False
        elif self._luxury < 2:
            self.alive = False
        elif self._entertainment > self._health+self._food:
            self.alive = False
