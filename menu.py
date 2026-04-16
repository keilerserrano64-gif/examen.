import json
import os
from datetime import datetime 

ARCHIVO_DATOS = "datos_restaurante.txt"

clientes_del_restaurante = []
mesas_del_restaurante = []
menu_del_restaurante = []

def guardar_datos():
    datos = {
        "clientes": clientes_del_restaurante,
        "mesas": mesas_del_restaurante,
        "menu": menu_del_restaurante
    }
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos():
    global clientes_del_restaurante, mesas_del_restaurante, menu_del_restaurante
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                clientes_del_restaurante = datos.get("clientes", [])
                mesas_del_restaurante = datos.get("mesas", [])
                menu_del_restaurante = datos.get("menu", [])
        except Exception as e:
            print(f"Error al cargar datos: {e}")


def mostrar_clientes(): 
    print("\n--- CLIENTES ---")
    for c in clientes_del_restaurante:
        print(f"ID: {c['identificacion']} | Nombre: {c['nombre']}")

def apartar_cita(): 
    nuevo_cliente = {
        "nombre": input("Nombre: "),
        "telefono": input("Teléfono: "),
        "identificacion": input("Cédula: "),
        "email": input("Email: ")
    }
    clientes_del_restaurante.append(nuevo_cliente) 
    guardar_datos() 
    print("CLIENTE GUARDADO")

def mostrar_menu():
    print("\n--- MENÚ ---")
    for i, p in enumerate(menu_del_restaurante):
        print(f"{i+1}. {p['nombre']} - ${p['precio']}")

def crear_platillo():
    nuevo_item = {"nombre": input("Nombre: "), "precio": float(input("Precio: "))}
    menu_del_restaurante.append(nuevo_item)
    guardar_datos()


def generar_factura():
    if not clientes_del_restaurante or not menu_del_restaurante:
        print("Error: Necesitas tener clientes y platillos registrados.")
        return

    print("\n--- GENERAR FACTURA ---")
    cedula = input("Cedula del cliente: ")
    cliente = next((c for c in clientes_del_restaurante if c['identificacion'] == cedula), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return

    mostrar_menu()
    seleccion = int(input("Seleccione el número del platillo: ")) - 1
    platillo = menu_del_restaurante[seleccion]

    ahora = datetime.now()
    fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")

    print("\n" + "="*30)
    print("FACTURA DE VENTA")
    print("="*30)
    print(f"Fecha: {fecha_formateada}")
    print(f"Cliente: {cliente['nombre']}")
    print(f"ID: {cliente['identificacion']}")
    print("-" * 30)
    print(f"Consumo: {platillo['nombre']}")
    print(f"TOTAL A PAGAR: ${platillo['precio']}")
    print("="*30)
    print("   ¡Gracias por su compra!")
cargar_datos()

while True:
    print("\n1. Clientes | 2. Mesas | 3. Menú | 4. FACTURAR | 5.salir")
    opcion = input("Seleccione: ")
    
    if opcion == "1":
        print("1. Ver | 2. Registrar")
        if input() == "1": mostrar_clientes()
        else: apartar_cita()
    elif opcion == "2":
      
        pass
    elif opcion == "3":
        print("1. Ver | 2. Agregar")
        if input() == "1": mostrar_menu()
        else: crear_platillo()
    elif opcion == "4":
        generar_factura()
    elif opcion == "5":
        break