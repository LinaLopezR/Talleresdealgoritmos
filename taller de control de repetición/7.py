while True:
    datos=input()
    x,m=datos.split(" ")
    x=int(x)
    m=int(m)
    #condicional
    if(x==0 and m==0):
        break
    r=x*m
    print(r)