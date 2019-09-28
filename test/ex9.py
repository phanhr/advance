a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
def quadro(a,b,c):
    delta = b*b-4*a*c
    if delta < 0:
        print("error")
    elif delta == 0 :
        print("nghiem kep: ",-b/(2*a))
    elif delta > 0:
        print("hai nghiem phan biet: x1=",(-b+delta**(1/2))/(2*a),"x2=",(-b-delta**(1/2))/(2*a))
quadro(a,b,c)        