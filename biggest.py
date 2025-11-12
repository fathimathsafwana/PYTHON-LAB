a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))
if a>b and a>c:
    print("The biggest number is:",a)
elif b>a and b>c:
    print("The biggest number is:",b)
else:
    print("The biggest number is:",c)
