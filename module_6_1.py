class Animal:
    alive = True    # (живой)
    fed = False     # (накормленный)
    def __init__(self, name):
        self.name = name

# Создаём  родительский класс растений
class Plant:
    edible = False  # (съедобность)
    def __init__(self, name):
        self.name = name

# Создаём унаследованный класс животных - Травоядные
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

# Создаём унаследованный класс животных - Хищники
class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

# Унаследованный класс растений - Цветы
class Flower(Plant):
    pass
 # edible = True

# Унаследованный класс растений - Фрукты
class Fruit(Plant):
    edible = True


# Ввод названий животных и растений
animal1 = Predator('Lion')
animal2 = Mammal('Cow')
plant1 = Plant('Lily')
plant2 = Fruit('Orange')

# Вывод результата
print(animal1.name)
print(plant1.name)

print(animal1.alive, f'- {animal1.name} живой')
print(animal2.fed, f'- {animal2.name} голоден')

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive, f'- {animal1.name} помер')
print(animal2.fed, f'- {animal2.name} сыт')