#Base -> child1, child2
class Father:
    def quality(self):
        print("Inside Father's class")
        print("Parent is good")
        
class Son(Father):
    def job(self):
        print("Inside Son's class")
        print("Son is in Software job")

class Daughter(Father):
    def aim(self):
            print("Inside Daughter's class")
            print("Daughter is in Software job")
            
obj1=Son()
obj2=Daughter()
obj1.quality()
obj1.job()
obj2.quality()
obj2.aim()