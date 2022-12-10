class Tables:
    def __init__(self,legs,color,price,height,width):
        self.legs=legs
        self.color=color
        self.price=price
        self.height=height
        self.width=width
    def describe(self):
        text1= f"you have choosen the worst choice with {self.legs} numer of legs in a table, {self.color} color, a high price of {self.price} and height and width of {self.height, self.width}"
        text2= f"you have choosen one the best in our collection sir with {self.legs} no of legs, {self.color} colour, a premium price of {self.price} and height and width of {self.height, self.width}"
        if self.legs == 3:
            return print(text1)
        return print(text2)
        
        
        
tbl1=Tables(3,"white",12000,120,360)
tbl1.describe()
tbl2=Tables(4,"black",21000,129,443)
tbl2.describe()
