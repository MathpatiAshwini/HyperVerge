string=input("enter the string: ")
spaces = " "
hyphens = "-"
for item in string:
    if  string.count(item) > 1 :
      print("No")
      break
    elif string.count(spaces) > 1 or string.count(hyphens) > 1:
      print("Yes")
      break
    else:
      print("Yes")