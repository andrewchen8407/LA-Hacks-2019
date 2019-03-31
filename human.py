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
        self._health = int(health)
        if health > 100:
            self._health = 100
        if health < 0:
            self._health = 0
    def get_health(self):
        return self._health
    def set_entertainment(self, entertainment):
        self._entertainment = int(entertainment)
        if entertainment > 100:
            self._entertainment = 100
        if entertainment < 0:
            self._entertainment = 0
    def get_entertainment(self):
        return self._entertainment
    def set_food(self, food):
        self._food = int(food)
        if food > 100:
            self._food = 100
        if food < 0:
            self._food = 0
    def get_food(self):
        return self._food
    def set_luxury(self, luxury):
        self._luxury = int(luxury)
        if luxury > 100:
            self._luxury = 100
        if luxury < 0:
            self._luxury = 0
    def get_luxury(self):
        return self._luxury
    def set_balance(self, val):
        self._balance = val
    def get_balance(self):
        return self._balance
    def update_status(self):
        if self._balance < 0:
            self.alive = False
        elif self._health < 30:
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
