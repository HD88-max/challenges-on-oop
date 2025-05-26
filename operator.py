class A:
    def __init__(self,a):
        self.a = a
    def __gt__(self,other):
        if self.a>other.a:
            return "greater than"
        
        else:
            return "less than"
    def __eq__(self,other):
        if self.a==other.a:
            return "equal"
        
        else:
            return "not equal"

ob1=A(45)
ob2 = A(28)
print(ob1.a>ob2.a)
print(ob1.a==ob2.a)