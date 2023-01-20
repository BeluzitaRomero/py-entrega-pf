class Client:
    def __init__(self, name, lastname, dni, tel):
        self.name = name
        self.lastname = lastname
        self.dni = dni
        self.tel = tel
        self.cart = []


    def __str__(self):
       return str(f"Client {self.name} {self.lastname}")


    def buy(self,product):
        self.cart.append(product)
    

    def delete_product_cart(self, product_dict_id):

        #para recorrer una lista de diccionarios use un metodo por compresion
        #de listas ya que no se me ocurrio otra manera
        # me devuelve una lista con el elemento buscado por id
        exists = list(e for e in self.cart if e["id"] == product_dict_id)   
    
        #busco el indice de ese elemento en el carrito
        index = self.cart.index(exists[0])
        #Elimino por indice
        self.cart.pop(index) 

    def delete_product_instance_cart(self, product_id):
        for prod in self.cart:
            if prod.id == product_id:
                index_to_delete = self.cart.index(prod)
               
                self.cart.pop(index_to_delete)
        


class Product:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
    
    def __str__(self):
        return str(f"Producto: {self.title}, id: {self.id}")

    def __repr__(self):
        return self.title

