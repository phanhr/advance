x=[4,5]
print(x)
y=input("xoa dau hay duoi: ")
if y == "dau": 
    x.pop(0)
elif y=="duoi": 
    x.pop(len(x)-1)
print(x)