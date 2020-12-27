gpy= float(input("enter gpy:"))
nol= float(input("enter number of lectures:"))

if gpy>=2 and nol>=47:
  x= str("Graduated")
elif nol<47 and gpy>=2:
  x= str("your number of lectures are not enought ")
elif gpy<2 and nol>=47:
  x= str("gpy is not enoght")
else: 
  x= str("your gpy and lectures are not enought")
print (x)