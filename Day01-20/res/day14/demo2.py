def bc(*,a,b,c):
  return a+b>c and a+c>b and b+c>a
print(bc(1,2,3))  
print(bc(3,4,5))
print(bc(a=9,b=22,c=32)) 
