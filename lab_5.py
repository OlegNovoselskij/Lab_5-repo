"""module providing const classes"""
from enum import Enum
import random


class Topping(Enum):
    """
    class which contains top of teste
    """
    SWEET = 1
    SOUR = 3
    NEUTRAL = 2

class Fruit(list):
    """
    class for making ekzemplars of fruits
    """
    SWEET = 0
    SOUR = 0
    NEUTRAL = 0

apple = Fruit(['apple', 'medium', 'green','SWEET'])
banana = Fruit(['banana', 'medium', 'yellow', 'SWEET'])
kiwi = Fruit(['kiwi', 'small', 'green', 'SOUR'])
grapefruit = Fruit(['grapefruit', 'large', 'orange', 'SOUR'])
avocado = Fruit(['avocado', 'small', 'green', 'NEUTRAL'])

list_of_fruits = [apple, banana, kiwi, grapefruit, avocado]
class FruitSalad():
    """
    class for choosing topping and for mixing salad
    """
    def __init__(self, fruits):
        self.fruits = fruits
        self.top = None
    def choose_topping(self):
        """
        chooose best topping for fruits
        """
        sweet_count = 0
        sour_count = 0
        neutral_count = 0
        for fruit in self.fruits:
            if fruit[-1] == Fruit.SWEET:
                sweet_count += 1
            elif fruit[-1] == Fruit.SOUR:
                sour_count += 1
            else:
                neutral_count += 1
        if sweet_count > sour_count and sweet_count > neutral_count:
            self.top = Topping.SWEET
        elif sour_count > sweet_count and sour_count > neutral_count:
            self.top = Topping.SOUR
        else:
            self.top = Topping.NEUTRAL

    def mix_ingredients(self):
        """
        mix fruits in list and delete a random fruit
        """
        num_of_deleted_fruit = random.randint(0, len(self.fruits))
        self.fruits.pop(num_of_deleted_fruit - 1)
        random.shuffle(self.fruits)
    def __str__(self):
        return f"Fruit Salad with {self.top.name} topping: {self.fruits}"

fruit_salad = FruitSalad(list_of_fruits)
fruit_salad.choose_topping()
print(fruit_salad)
print()
fruit_salad.mix_ingredients()
print(f"After mixing:\n {fruit_salad}")
