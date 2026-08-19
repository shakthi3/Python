


class teacher:

    def detail(self):

        self.tech_name=input("enter your mentor name : ")

    def question(self):

        self.ques=input("enter the question : ")

class student(teacher):
    
    def data(self):


        teacher.detail(self)
        teacher.question(self)
        self.name=input("enter your name : ")
        self.cls=input("enter your cls : ")
        self.answer=input("enter the answer : ")

        
        
        print(self.name)
        print(self.cls)
        print(self.tech_name)
        print(self.ques)
        print(self.answer)


s1=student()
s2=student()

s1.data()
s2.data()

