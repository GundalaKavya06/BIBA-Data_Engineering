#base -> child
class Father:
    def quality(self):
        print("Inside Father's class")
        print("Parent is good")
        
class Son(Father):
    def job(self):
        print("Inside Son's class")
        print("Son is in Software job")

obj=Son()
obj.quality()
obj.job()

        