class College:
    def __init__(self,clg_name):
        self.clg_name=clg_name
    def name_college(self):
        return print(f"College name is {self.clg_name}")
class Grades(College):
    def __init__(self, clg_name,grade,faculty):
        super().__init__(clg_name)
        self.grade=grade
        self.faculty=faculty
    def info_grade(self):
        return print(f'The students grade is {self.grade} and faculty is {self.faculty}')
class Students(Grades,College):
    def __init__(self, clg_name, grade, faculty,std_name,roll_no,gender):
        super().__init__(clg_name, grade, faculty)
        self.std_name=std_name
        self.roll_no=roll_no
        self.gender=gender
    def student_description(self):
        if self.gender =='male':
            std_gender = 'boy'
        elif self.gender=="female":
            std_gender = 'girl'
        text=f"Student's College name {self.clg_name}, \n {std_gender} reads in {self.grade} in {self.faculty}. \n {std_gender} name is {self.std_name}. {std_gender}'s roll no is {self.roll_no}"
        return print(text)
samir=Students("Hetauda City College",12,"science","Sameer Rai","6","male")
samir.student_description()
