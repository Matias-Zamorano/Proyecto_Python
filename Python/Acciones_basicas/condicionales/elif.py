ingreso_mensual = 81000
gasto_mensual   = 80000

#if anidados y else if (elif)

# Si el ingreso mensual es mayor a 10.000 has lo siguiente :
if ingreso_mensual > 10000: 
    if ingreso_mensual - gasto_mensual < 0: #Si el ingreso mensual "menos" (-) gasto mensual "es menor a" (<) 0 dime el siguiente mensaje : 
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000: # En el caso que no se resperte el primer if se hace el siguiente calculo :
        print(" estas bien")
    else: #En el caso que no se respeten los if anteriores  muestra el siguiente mensaje : 
        print("estas gastando mucho, hay que ver si te alcanza") 
    
#En el caso que no se haya alcanzado en el primer "if" que seria "ingreso_mensual > 10.000" dime lo siguiente :
    
elif ingreso_mensual > 1000: 
    print("estas bien en latinoamèrica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
    
else: 
    print("sos pobre")