'''Crea un scrip en python el cual le permita al usuario crear una lista de objetos
a inventariar, en esta debera poder almacenar nombre,codigo y precio de productos para
poder y una ves echo esto debera poder relizar un conteo fisico de sus productos,
una ves termine el conteo debera desplegarse el total de piezas contadas y valor monetario
de su inventario'''

productos = {}
flag = True

while flag:
    buscar = input('Nombre de producto encontrado: ')
    if buscar not in productos:# se agrega producto si este no se encuentra
        nombre = buscar
        precio = float(input('Precio de el producto encontrado: $'))
        cantidad = int(input('Cantidad que encontraste: '))
        necesito = int(input('Cantidad que necesitas: '))
        productos[nombre] = [precio, cantidad, necesito]
        print(productos)
    else:# el producto ya se encunentra guardado
        precio, cantidad, necesito = productos[buscar]
        contado = []
        suma = cantidad
        
        print(f"Ya tienes registrado {cantidad} de {buscar}. Necesitas {necesito} en total.")
        
        while suma != necesito:# comparacion de cantidad existente vs necesaria
            encontrado = int(input('Digite la cantidad encontrada: '))
            contado.append(encontrado)
            suma += encontrado  
            print(f"Llevas acumulado: {suma} de {necesito}")
            
        print(f'Has encontrado todos los productos necesarios de {buscar}')
        