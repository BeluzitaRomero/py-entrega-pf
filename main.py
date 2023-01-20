from paquete_1 import client as C


cliente_1 = C.Client("Belen", "Romero", 34152, 456123)

# ! Elegir un tipo de dato guardar en el carrito para (dict o class)

# *Pruebas del metodo delete con diccionarios
# toallon = {"id":1, "title":"toallon", "price": 3000}
# juego = {"id":2, "title":"juego", "price": 100}

# cliente_1.buy(toallon)
# cliente_1.buy(juego)
# print("carrito antes del delete: ", cliente_1.cart)
# cliente_1.delete_product_cart(juego["id"])
# print("carrito actualizado: ",cliente_1.cart)


#* Prueba del metodo delete con instancias de la clase Product
producto1  = C.Product(1, "lima", 12)
producto2  = C.Product(2, "esmalte", 120)
producto3  = C.Product(3, "toalla", 3000)
producto4  = C.Product(4, "algodon", 200)

cliente_1.buy(producto1)
cliente_1.buy(producto2)
cliente_1.buy(producto3)
cliente_1.buy(producto4)


print(cliente_1.cart)
cliente_1.delete_product_instance_cart(producto2.id)
print(cliente_1.cart)
