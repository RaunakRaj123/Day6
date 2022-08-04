class student:
    __name=None
    _a=2
    def __init__(self,a):
        self.__name=a
        print(self.__name)
ob=student('xyz')
print(ob._a)