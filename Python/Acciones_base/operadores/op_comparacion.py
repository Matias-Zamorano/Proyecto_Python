
igual_que       = 5 == 6

distinto_de     = 5 != 6

mayor_que       = 5 >  6

menor_que       = 5 <  6

mayor_o_igual   = 5 >= 6

menor_o_igual   = 5 <= 6

#calculos combinados
a = 5
b = 10
c = 20
comparacion = a + b < c

#comparar usuarios , en caso que sea distinta dara error dado que tiene un ""=="" lo cual dice es igual_que 
contraseña_almacenada = "hola123"
contraseña_escrita    = '''Hola123'''

print(contraseña_almacenada == contraseña_escrita)