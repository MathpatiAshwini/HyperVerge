a=int(input("enter the number:-"))
temp=a
sum=i=0
b=len(str(a))  
while temp!=0:
    d=temp%10
    sum+=d**b
    temp//=10
if a==sum:
    print("armstrong no")
else:
    print("not armstrong no.")