#Base1, Base2 -> child

class Mother:
    def m_quality(self):
        print("Inside Mother's class")
        print("She's a beautiful person")
class Father:
    def quality(self):
        print("Inside Father's class")
        print("Parent is good")
        
class Son(Mother,Father):
    def job(self):
        print("Inside Son's class")
        print("Son is in Software job")
        

obj=Son()
obj.m_quality()
obj.quality()
obj.job()