num=int(input())
rev=0
while(num>0):
  rem=num%10
  rev=(rev*10)+rem
  num=num//10
if(num==rev):
  print("yes")
else:
  print("no")
  
