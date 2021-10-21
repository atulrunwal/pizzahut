# exercise15.py
import random
# for i in range(3):
#     print(random.randint(10, 20))

# name = ['dog', 'deer', 'lion', 'monkey']
# member = random.choice(name)
# print(member)


class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(f'({a},{b})')


d1 = Dice()
d1.roll()
