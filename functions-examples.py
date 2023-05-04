
#Ejemplos if-else y ternary operator
print("-----Ejemplos de if-else-----")

edad1 = 2

if edad1 >= 18:
    print("Eres mayor de edad")
elif edad1 <= 0:
    print("No existes")
else:
    print("Todavia estas bebe")


contraseña = 'hola'

if contraseña == 'Hola':
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta, ushcale de aqui")


if  0 <= edad1 <= 12:
    print("Eres un niño")
elif 13 <= edad1 <=17:
    print("Eres un adolscente")
elif 18 <= edad1 <= 59:
    print("Eres un adulto")
elif edad1 >= 60:
    print("Eres de la tercera edad")


#Ejemplos de for loop with range()
print("Ejemplos de for loop")

n = 10

for index in range(n):
    print(index)

print("-------")

for index in range(0,4):
    print(index)
print("------")

for num in range(1,5):
    print(num*2)


#Ejemplos de while
print("Ejemplos de while")

i = 1

while i <= 10:
    print("Todo bien")
    i+=1
