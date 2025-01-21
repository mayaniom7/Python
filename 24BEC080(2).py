a=int(input("Enter The Number a:"))
b=int(input("Enter the Number b:"))
c=int(input("Enter the Number c:"))
if(a>=b)and(b>=c):
    print("a is the largest number",a)
elif(b>=a)and(b>=c):    
    print("b is the largest number",b)
else:
    print("c is the largest number",c)
