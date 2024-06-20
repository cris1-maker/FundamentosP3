import Funciones  as fn
clientes=[]
while True:
    print("PaquExpress")
    print("1-Registrar pedido")
    print("2-Listar los todos los pedidos")
    print("3-Imprimir hoja de ruta")
    print("4-Salir del programa")
    opcion=int(input("Ingrese opcion: "))
    if opcion==1:
        fn.registroPedido(clientes)
    else:
        if opcion==2:
            fn.listadoPedido(clientes)
        else:
            if opcion==3:
                fn.imprimirRuta(clientes)
            else:
                if opcion==4:
                    break
                else:
                    print("Ingrese una opcion valida")