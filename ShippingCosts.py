weight=80
#Ground Shipping
print("Ground shipping: ")
if weight<=2:
  total= weight*1.50+20
  print("Cost: $",total)
elif weight<2 and weight<=6:
  total= weight*3.00+20
  print("Cost: $",total)
elif weight>6 and weight<=10:
  total= weight*4.00+20
  print("Cost: $",total)
elif weight>10:
  total=weight*4.75+20
  print("Cost: $",total)
premium_shipping=125.00
print("Ground Shipping Premium is a flat charge of " ,premium_shipping)
#Drone shipping
print("Drone shipping:")
if weight<=2:
  total= weight*4.50
  print("Cost: $",total)
elif weight<2 and weight<=6:
  total= weight*9.00
  print("Cost: $",total)
elif weight>6 and weight<=10:
  total= weight*12.00
  print("Cost: $",total)
elif weight>10:
  total=weight*14.25
  print("Cost: $",total)
