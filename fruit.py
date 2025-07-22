#classes
class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def describe(self):
        return f"{self.name} is a {self.color} fruit that tastes {self.taste}."

apple = Fruit("Apple", "red", "sweet")
banana = Fruit("Banana", "yellow", "sweet")
cherry = Fruit("Cherry", "red", "tart")

print(apple.describe())
print(banana.describe())
print(cherry.describe())