SECTOR=["centro","norte","sur"]
pedido=["pequeño","mediano","grande"]
def registroPedido(clientes):
    nombre=input("Ingrese nombre y apellido: ")
    direccion=input("Ingrese direccion: ")
    while True:
        sector=input("Ingrese sector (Centro/Norte/Sur): ").lower()
        if sector in SECTOR:
            break
        else:
            print("Sector no valido,vuelva a intentarlo.")
    while True:
        detallePedido=input("Ingrese tamaño del paquete(Pequeño/Mediano/Grande): ").lower()
        if detallePedido in pedido:
            cantPaquetes=int(input("Ingrese cantidad de paquetes: "))
            respuesta=input("Desea agregar mas pedidos?(s/n): ")
            if respuesta=="s":
                print("")
            else:
                break
        else:
            print("Ingrese un tamaño valido.")

    clientes.append({
        "Nombre":nombre,
        "Direccion":direccion,
        "Sector":sector,
        "DetallePaquete":detallePedido,
        "CantPaquetes":cantPaquetes
    })
def listadoPedido(clientes):
    print("Listado pedidos")
    for elemento in clientes:
        print(elemento)
def imprimirRuta(clientes):
    selSector=input("Ingrese sector: ")
    if selSector in SECTOR:
        ruta_imp=[]
        for cliente in clientes:
            if cliente["Sector"]==selSector:
                ruta_imp.append(clientes)
        nuevo_archivo="Ruta.txt"

    with open(nuevo_archivo,"w") as archivo:
        for ruta_imp in clientes:
            archivo.write(f"Nombre: {cliente["Nombre"]}\n")
            archivo.write(f"Direccion: {cliente["Direccion"]}\n")
            archivo.write(f"Sector: {cliente["Sector"]}\n")
            archivo.write(f"Tamaño del paquete: {cliente["DetallePaquete"]}\n")
            archivo.write(f"Cantidad: {cliente["CantPaquetes"]}\n\n")
