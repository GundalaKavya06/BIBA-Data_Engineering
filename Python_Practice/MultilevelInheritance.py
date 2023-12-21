#base -> child1 -> child2
class GrandFather:
    def quality(self):
        print("Inside GrandFather's class")
        print("He's a honest person")
        
class Father(GrandFather):
    def f_quality(self):
        print("Inside Father's class")
        print("He's a good person")
        
class Son(Father):
    def job(self):
        print("Inside Son's class")
        print("Son is in Software job")
        
obj= Son()
obj.quality()
obj.f_quality()
obj.job()
