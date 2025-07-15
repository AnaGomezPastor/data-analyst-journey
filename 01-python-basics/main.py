## Ejercicio 1: crea un hello world
print("Hello, World!");

## Ejercicio 2: parcticar con if/else if/ else

edad = 18
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")

## Ejercicio 3: practicar con for

for i in range(5):
    print(i)

## Ejercicio 4: practicar con while

contador=0
while contador <= 5:
    print(contador)
    contador += 1

## Ejercicio 5: practicar con funciones
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ana")

## Ejercicio 6: practicar con listas
nombres=["Ana", "Luis", "Pedro"]
for nombre in nombres:
    print(f"Hola, {nombre}")

## Ejercicio 7: practicar con diccionarios
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Barcelona"
}
print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}")

## Ejercicio 8: practicar con tuplas
coordenadas = (10.0, 20.0)
print(f"Coordenadas: {coordenadas[0]}, {coordenadas[1]}")

## Ejercicio 9: practicar con sets
frutas = {"manzana", "banana", "naranja"}
frutas.add("uva")
print("Frutas:", frutas)

## Ejercicio 10: practicar con excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida")

## Ejercicio 11: practicar con clases
