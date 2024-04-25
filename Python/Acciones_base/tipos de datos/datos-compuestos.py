
#creando una lista (se pueden modificar)
lista = ["Matias Zamorano", 123, True, 1.69,'manzana']

print(lista)

#creando una tupla (no pueden modificar)
tupla = ("Matias Zamorano", 123, True, 1.69,"manzana")

#esto es válido
lista[3] = "Desayuno"

#esto no es válido
tupla[3] = "Desayuno"


#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Matias Zamorano", 123, True, 1.69,"manzana"}

print(conjunto[3]) #-> no puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Matias Zamorano",
    'numero' : 123,
    'esta_emocionado' : True,
    'altura' : 1.69,
    'fruta_favorita' : "manzana" # en el ultimo no lleva comillas al final ""
}

print(diccionario['numero'])



