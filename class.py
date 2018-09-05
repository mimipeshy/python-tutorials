class A:
    def str(self):
        return '1'

class B(A):
    def init(self):
        super().init()

class C(B):
    def init(self):
        super().init()

def main():
    obj1 = B()
    obj2 = A()
    obj3 = C()
print(obj1, obj2,obj3)
main()
