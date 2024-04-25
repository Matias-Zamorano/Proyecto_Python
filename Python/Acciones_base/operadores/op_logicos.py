#Operador AND 
"""
Si ambas condiciones son verdaderas, el resultado es verdadero.
Si una o ambas condiciones son falsas, el resultado es falso.
Si la primera condición es falsa, la segunda no se evalúa.
"""
Resultado_1 = True  & True  #Devuelve True
Resultado_2 = False & True  #Devuelve Falso
Resultado_3 = True  & False #Devuelve Falso
Resultado_4 = False & False #Devuelve Falso

#Operador OR ,
"""
Si al menos una de las condiciones es verdadera, el resultado es verdadero.
Si ambas condiciones son falsas, el resultado es falso.
Si la primera condición es verdadera, la segunda no se evalúa
"""

Resultado_5 = True  | True  #Devuelve True
Resultado_6 = False | True  #Devuelve True
Resultado_7 = True  | False #Devuelve True
Resultado_8 = False | False #Devuelve Falso

#Operador NOT,
"""
Niega el valor de la condición. Si la condición original es verdadera, not la convierte en falsa, y viceversa.
"""

Resultado_9  = not True  #Devuelve Falso
Resultado_10 = not False #Devuelve True

print(Resultado_9)

