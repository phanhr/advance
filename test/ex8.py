x=[4,5,6,3]
print(*x)
y=input("delete head or tail: ")
if y == "head": 
    x.pop(0)
elif y=="tail": 
    x.pop(len(x)-1)
print(*x)