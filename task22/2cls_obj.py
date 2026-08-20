


class teacher:

    def detail(self):

        self.tech_name=input("enter your mentor name : ")

    def question(self):

        self.ques=input("Question: create your own project")
        self.answer=input("enter the answer : ")

class student(teacher):
    
    def data(self):

        self.name=input("enter your name : ")
        self.cls=input("enter your cls : ")
        teacher.detail(self)
        teacher.question(self)
        

        
        
        print(self.name)
        print(self.cls)
        print(self.tech_name)
        print(self.answer)
        


s1=student()
s2=student()

s1.data()
s2.data()

