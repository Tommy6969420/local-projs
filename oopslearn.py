from turtle import color


class Table:
    def legs(self,legs=4):
        self.legs=legs
    def show_legs(self):
        return print(self.legs)
    def color(self,color):
        self.color=color
    def show_color(self):
        return print(self.color)
    def showColLegs(self):
        return print(self.legs,self.color)
    def describe(self):
        return print(f"you have choosen a fuckin {self.color} colored table with fucking {self.legs} no of legs")
tbl=Table()
tbl.legs(5)
tbl.color("blue")
tbl.show_legs()
tbl.show_color()
tbl.showColLegs()
tbl.describe()

tbl2= Table()
tbl2.legs(3)
tbl2.color("Pink")
tbl2.describe()
