##Check whether the number is Armstrong Number or not.
n=int(input("Enter the number = "))
c=0
Sum=0
n2=n
while n!=0:
    n=n//10
    c=c+1
n=n2
for i in range (0,c):
    a=n2%10
    Sum=Sum+a**c
    n2=n2//10
if Sum!=n:
    print("The number is not an Armstrong Number")
else:
    print("The number is an Armstrong Number")
    
