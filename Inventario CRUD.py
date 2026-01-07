
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}) - Precio: ${self.precio} - Stock: {self.cantidad}"
    

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            self.productos[producto.id].cantidad += producto.cantidad
            print("Producto ya existe. Actualizando cantidad...")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado al inventario")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado")
        else:
            print("Producto no encontrado")

    def listar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def actualizar_producto(self, id, cantidad=None, precio=None):
            if id in self.productos:
                if cantidad is not None:
                    self.productos[id].cantidad = cantidad
                if precio is not None:
                    self.productos[id].precio = precio
                print(f"Producto con ID {id} actualizado")
            else:
                print("Producto no encontrado")

# Ejemplo de uso
inventario = Inventario()
producto1 = Producto(1, "Manzana", 0.50, 100)
producto2 = Producto(2, "Naranja", 0.30, 150)
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto1)
inventario.listar_productos()
inventario.eliminar_producto(2)
inventario.actualizar_producto(1, cantidad=120, precio=0.55)
inventario.listar_productos()