# умная копилка
class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        if self.capacity >= v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v
            self.money += v


box = MoneyBox(100)
box.add(10)
print('capacity:', box.capacity)
print('money:', box.money)
print()
box.add(50)
print('capacity:', box.capacity)
print('money:', box.money)
print()
box.add(40)
print('capacity:', box.capacity)
print('money:', box.money)
print()
box.add(10)
print('capacity:', box.capacity)
print('money:', box.money)
