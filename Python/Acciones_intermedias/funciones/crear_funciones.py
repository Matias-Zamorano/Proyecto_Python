
#creando una función simple
def saludar():
   print("Hola programador ¿Como estas?")
    
#ejecutando la funcion simple
saludar()

#crear una funcion que tenga parametros
def saludar_persona(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Reina"
    elif (sexo == "hombre"):
        adjetivo = "Rey"
    else:
        adjetivo = 'amor'
    print(f"Hola {nombre}, mi {adjetivo} estoy a su servicio")
    
saludar_persona("Camila","MuJER")
saludar_persona("PEDRO","hombre")
saludar_persona("Fran","no binario")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_numero}")




