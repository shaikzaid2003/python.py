'''#class membership test
class A:
    name="Zaid"
class B:
    section="K22GB"
class C:
    age="19"
a=A()
b=B()
c=C()
print(isinstance(a,A))
print(isinstance(b,B))
print(isinstance(c,C))
print(a.name)
print(b.section)
print(c.age)'''

class A:
    def school(name,age):
        print(name,age)
    def school(name,marks):
        print(name,marks)
a=A()
A.school("Zaid",19)
