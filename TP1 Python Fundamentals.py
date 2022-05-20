# PROYECTO 1 PYTHON FUNDAMENTALS: ELABORAR UN MINI COBRADOR

productos = {}

def MenuPrincipal():
    return int(input("Bienvenido al MINI COBRADOR: \n 1- Ver lista de productos \n 2- Agregar producto \n 3- Remover producto \n 4- Ver carrito \n 5- Añadir a carrito \n 6- Retirar del carrito \n 7- Cobrar  \n 0- Cerrar programa \n"))

menu = MenuPrincipal()

while menu != 0:
    if menu == 1:
        print("Producto   |  Precio  ")
        for id in productos: 
            print(id, "        ", productos[id][0] )
    
    elif menu == 2:
        clave = str(input("Ingresar producto a agregar: "))
        precio = float(input("Ingresar precio del nuevo producto: "))
        productos[clave] = [precio, 0]

    elif menu == 3:
        clave = str(input("Ingresar producto a remover: "))
        del productos[clave]

    elif menu == 4:
        print(" Producto   |  Precio  |  cantidad |  total " )
        
        for id in productos: 
            total = productos[id][0]* productos[id][1]
            if productos[id][1] > 0:
                print(id, "         ", productos[id][0],"      ", productos[id][1], "     ", total )
            
    elif menu == 5:
        clave = str(input("Ingresar producto a agregar al carrito: ")) 
        productos[clave][1] += int(input("Ingrese cantidad: ")) # Cantidad de producto
        print(productos[clave][1])
    
    elif menu == 6:
        clave = str(input("Ingresar producto a retirar del carrito: ")) 
        productos[clave][1] -= int(input("Ingrese cantidad: ")) # Cantidad de producto
        print(productos[clave][1])

    elif menu == 7: 
        total = 0
        for id in productos: 
            total += productos[id][0]* productos[id][1]
        print("Gracias por su compra! Total: $",total)

    menu = MenuPrincipal()