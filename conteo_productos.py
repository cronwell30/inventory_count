'''Crea un scrip en python el cual le permita al usuario crear una lista de objetos
a inventariar, en esta debera poder almacenar nombre,codigo y precio de productos para
poder y una ves echo esto debera poder relizar un conteo fisico de sus productos,
una ves termine el conteo debera desplegarse el total de piezas contadas y valor monetario
de su inventario'''

productos = {}
flag = True
#import os

while flag is True:
       #os.system('clear')
    buscar = str(input('Nombre de producto encontrado: '))
    if buscar not in productos:
        nombre = (buscar)
        precio = float(input('Precio de el producto encontrado: $'))
        cantidad = int(input('Cantidad que encontraste: '))
        necesito = int(input('Cantidad que necesitas: '))
        productos [nombre] = [precio,cantidad,necesito]
        print(productos)
    elif buscar in productos:
        contado = []
        suma = 0
        while contado != necesito:
            encontrado = int(input('Digite la cantidadencontrada: '))
            contado.append(encontrado)
            print(contado)
            for i in (contado):
                suma = sum(contado)
                print(suma)
            if suma >= necesito:
                print ('Has encontrado todos los productos necesarios')