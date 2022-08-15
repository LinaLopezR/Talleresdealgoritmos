#Entradas
Sueldo=int(input("Introduzca el sueldo devengado por el empleado: $"))
Categoria=int(input("Digite la categoria a la que pertenece el empleado: "))
#Caja negra
if(Sueldo>=5000000):
    Aumento=Sueldo*0.10
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo>=4300000):
    Aumento=Sueldo*0.15
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo>=3600000):
    Aumento=Sueldo*0.20
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo>=2000000):
    Aumento=Sueldo*0.40
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo>=900000):
    Aumento=Sueldo*0.60
    print("La categoria del trabajador es: ",Categoria)
#Salidas
print("El nuevo saldo bruto del trabajador es de: $",Sueldo+Aumento)