#Proyectos sencillos

#Lanzamiento de dados
import random

def lanzar_dados():
    return random.randint(1,6)

def main():
    respuesta = input("Quieres lanzar el dado? (s/n)")
    if respuesta == "s":
        print(f"Tu número es: {lanzar_dados()}")
    else:
        print("Fin del juego")

if __name__ == "__main__":
    main()

#Agende de contactos con diccionario

contactos = {}
def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    print(f"Contacto {nombre}, agregado con éxito su {telefono}")

def mostrar_contactos():
    if contactos:
       print("Lista de contactos:")
       for nombre, telefono in contactos.items():
           print(f"{nombre}, {telefono}")
           if nombre == "":
               print("No hay contactos")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"El contacto {nombre} ha sido eliminado")
    else:
        print(f"No se encontró el contacto {nombre}")

def menu():
    while True:
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Eliminar contacto")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
            print(f"Contacto {nombre} eliminado con éxito")
        elif opcion == "4":
            print("Saliendo del programa...")
            break




