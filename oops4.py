#sngle inheritance
class Furnitures:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def describe(self):
        return print(f"Sir you have bought {self.name} at a price of {self.cost}")
class Chair(Furnitures):
    def __init__(self,name,cost,type,color):
        super().__init__(name,cost)
        self.type=type
        self.color=color
    def describe_chair(self):
        print(f'You have purchased a {self.name} at cost {self.cost} and it is {self.type} prioritized chair with {self.color}')
gaming_chair=Chair("chair",12000,"gaming","black,red color")
gaming_chair.describe()
gaming_chair.describe_chair()