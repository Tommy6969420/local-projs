#multi level inheritance
class parent1:
    def assign1(self,str1):
        self.str1=str1
    def show1(self):
        print(self.str1)
class parent2:
    def assign2(self,str2):
        self.str2=str2
    def show2(self):
        print(self.str2)
class child1(parent1,parent2):
    def assign_child(self,str_child):
        self.str_child=str_child
    def show_child(self):
        return print(self.str_child)

baccha=child1()
baccha.assign1("parent")
baccha.assign2("parent2")
baccha.assign_child("I am child")
baccha.show1()
baccha.show2()
baccha.show_child()
# print(dir(child1))
