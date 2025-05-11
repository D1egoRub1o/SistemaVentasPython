# =============================================================
# Sistema de Gestión de Ventas
# Autor: Diego Fernando Rubio
# Curso: Lenguaje de Programación I
# Proyecto: Sistema de gestión de ventas
# =============================================================
# Descripción:
# Este sistema permite registrar ventas de cursos ofertados por una academia de programación.
# Incluye funcionalidades para ver los cursos disponibles, registrar una venta, 
# calcular el total vendido y aplicar un descuento si el total supera $1.000.000.
# Se utiliza una estructura de diccionario para representar cursos y una lista para
# almacenar las ventas realizadas durante la ejecución del programa.
# =============================================================

# Diccionario que contiene los cursos disponibles y sus precios
cursos = {
    1: {"nombre": "Curso de Python", "precio": 300000},
    2: {"nombre": "Curso de Java", "precio": 350000},
    3: {"nombre": "Curso de JavaScript", "precio": 250000},
}

# Lista global para almacenar todas las ventas registradas
ventas = []

# -------------------------------------------------------------
# Función: mostrarMenu
# Muestra el menú principal del sistema al usuario
# -------------------------------------------------------------
def mostrarMenu():
    print("\nMENU DE CODEMASTERS DE CURSOS")
    print("1. Ver los cursos disponibles")
    print("2. Registrar una venta de un curso")
    print("3. Calcular el total de ventas")
    print("4. Salir")

# -------------------------------------------------------------
# Función: verCursos
# Muestra los cursos disponibles con sus respectivos precios
# -------------------------------------------------------------
def verCursos():
    print("\nCURSOS DISPONIBLES")
    for clave, curso in cursos.items():
        print(f"{clave}. {curso['nombre']} - ${curso['precio']}")

# -------------------------------------------------------------
# Función: registrarVentas
# Permite seleccionar un curso y registrar su compra en la lista de ventas
# -------------------------------------------------------------
def registrarVentas():
    verCursos()
    try:
        opcion = int(input("Seleccione el número del curso: "))
        if opcion in cursos:
            cantidad = int(input("Cuantas unidades desea comprar: "))
            if cantidad > 0:
                curso = cursos[opcion]
                subTotal = curso['precio'] * cantidad
                ventas.append({
                    "nombre": curso["nombre"],
                    "precio": curso["precio"],
                    "cantidad": cantidad,
                    "subTotal": subTotal
                })
                print(f"Venta registrada: {curso['nombre']} X {cantidad} - TOTAL: ${subTotal}")
            else:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Opción inválida")
    except ValueError:
        print("Datos inválidos. Intente de nuevo")

# -------------------------------------------------------------
# Función: calcularTotalVentas
# Muestra un resumen de todas las ventas y aplica descuento si corresponde
# -------------------------------------------------------------
def calcularTotalVentas():
    if not ventas:
        print("No hay ventas registradas")
        return

    total = 0
    print("\nRESUMEN DE VENTAS")
    for i in ventas:
        print(f"{i['nombre']} X {i['cantidad']} - ${i['subTotal']}")
        total += i['subTotal']

    descuento = 0
    if total > 1000000:
        descuento = total * 0.10
        print("Descuento del 10% aplicado por compras superiores a $1.000.000")

    totalFinal = total - descuento
    print(f"SubTotal: ${total}")
    print(f"Descuento: ${descuento}")
    print(f"Total a pagar: ${totalFinal}")

# -------------------------------------------------------------
# Función: iniciarApp
# Controla el flujo principal de la aplicación mediante un ciclo de menú
# -------------------------------------------------------------
def iniciarApp():
    while True:
        mostrarMenu()
        try:
            opcion = int(input("Digite la opción: "))
            if opcion == 1:
                verCursos()
            elif opcion == 2:
                registrarVentas()
            elif opcion == 3:
                calcularTotalVentas()
            elif opcion == 4:
                print("Hasta la próxima ...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número válido.")

# -------------------------------------------------------------
# Inicio del programa
# -------------------------------------------------------------
iniciarApp()


