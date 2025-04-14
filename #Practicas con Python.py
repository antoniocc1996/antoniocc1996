#Practicas con Python

#Ejercicio 1: Crear un programa que pida al usuario su nombre y lo imprima en pantalla.
nombre = input("Introduce tu nombre: ") 
print("Hola, " + nombre + " bienvenido a mi github")

#Ejercicio 2: Crear un programa que pida al usuario dos números y muestre su suma.
num1 = float(input("Introduce el numero que quieras:")) 
num2 = float(input("introduce el segundo numero que quieras:") )
suma = num1 + num2
print("La suma de los dos numeros es: " + str(suma))

#Ejercicio 3: Crear un programa que pida al usuario una cadena de texto y la imprima al revés.
cadena = input("Introduce una cadena de texto: ")
cadena_invertida = cadena[::-1]
print("La cadena invertida es: " + cadena_invertida)

#Ejercicio 4: Crear un programa que pida al usuario una lista de números y muestre su promedio.
numeros = input("Introduce una lista de numeros separados por comas: ")
numeros = [float(num) for num in numeros.split(",")]
promedio = sum(numeros) / len(numeros)
print("El promedio de la lista es: " +str(promedio))

#Ejercicio 5: Crear un programa que pida al usuario una lista de palabras y muestre la más larga.
palabras = input("Introduce una lista de palabras separadas por comas: ")
palabras = palabras.split(",")
palabra_larga = max(palabras, key=len)
print("La palabra más larga es: " + palabra_larga)

#Ejercicio 6: Crear un programa que pida al usuario una lista de números y muestre el mayor y el menor.
numeros = input("Introduce una lista de numeros separados por comas: ")
numeros = [int(num)for num in numeros.split(",")]
numero_mayor = max(numeros)
numero_menor = min(numeros)
print("El numero mayor es: " + str(numero_mayor))
print("El numero menor es: " + str(numero_menor))

#Ejercicio 7: Crear un programa que pida al usuario una lista de números y muestre la suma de los números pares.
numeros = input("Introduce una lista de numeros separados por comas: ")
numeros = [int(num) for num in numeros.split(",")]
suma_pares = sum(num for num in numeros if num % 2 == 0)
print("La suma de los números pares es: " + str(suma_pares))

#Ejercicio 8: Crear un programa que pida al usuario una lista de números y muestre la suma de los números impares.
numeros = input("Introduce una lista de numeros separados por comas: ")
numeros = [int(num) for num in numeros.split(",")]
suma_impares = sum(num for num in numeros if num % 2 != 0)
print("La suma de los números impares es: " + str(suma_impares))

#Ejercicio 9: Un programa que cambie de grados centigrados a fahrenheit
grados = float(input("Introduce la temperatura: "))
fahrenheit = (grados * 9/5) + 32
print("La temperatura en grados fahrenheit es: " + str(fahrenheit))

#Ejercicio 10: Un programa que cambie de fahrenheit a grados centigrados
fahrenheit = float(input("Introduce la temperatura: "))
centigrados = (fahrenheit - 32) * 5/9
print("La temperatura en grados centigrados es: " + str(centigrados))

#Ejercicio 11: Un programa que cambie de metros a pies
metros = float(input("Introduce la distancia en metros: "))
pies = metros * 3.28084
print("La distancia en pies es: " + str(pies))

