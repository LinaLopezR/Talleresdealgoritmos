#entradas
a=float(input("ingrese calificacion uno: "))
b=float(input("ingrese calificacion dos: "))
c=float(input("ingrese calificacion tres: "))
e=float(input("ingrese promedio del examen"))
t=float(input("ingrese nota del trabajo final: "))
#caja negra
p=(a+b+c)/3
f=(p*.55)+(e*.30)+(t*.15)
#salidas
print("promedio final de la materia computacion: ", f)
