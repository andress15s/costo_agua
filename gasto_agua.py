print("----------------------------------")
print("-----calcular costo de agua-------")
print("----------------------------------")



#input

gasto_agua=int(input("ingrese el valor de metros cubicos gastados: "))

#Processing
  
if gasto_agua<=50:
  costo_agua=10000
 
if gasto_agua>50 and gasto_agua<=200:
 costo_agua = 10000+(gasto_agua-50)*2000

else:
 costo_agua = (gasto_agua-200) * 3000 +10000+300000
print(" el costo es " + str(costo_agua))

#output
print("eso era.")