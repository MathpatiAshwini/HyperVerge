num = int(input("enter number"))
if(num % 7==0) and (num%3!=0) and (num%5!=0): 
  print("Plong")
elif (num % 7!=0) and (num%3==0) and (num%5==0): 
  print("PlingPlang")
elif  (num%3==0) and (num%5==0)and  (num%7==0):
  print("PlingPlangPlong")
else:
  print(num)