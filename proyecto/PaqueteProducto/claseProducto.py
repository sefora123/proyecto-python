class Producto:

    def __init__(self):
        self.__codigo = ""
        self.__descripcion = ""
        self.__cantidad = ""
        self.__preciounitario = ""

# Metodos de acceso get y set
    def getCodigo(self):
        return self.__codigo

    def getDescripcion(self):
        return self.__descripcion

    def getCantidad(self):
        return self.__cantidad
    
    def getPrecioUnitario(self):
        return self.__preciounitario

    def setCodigo(self,codigo):
        self.__codigo = codigo

    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion

    def setCantidad(self,cantidad):
        self.__cantidad = cantidad

    def setPrecioUnitario(self,preciounitario):
        self.__preciounitario = preciounitario

    
    def PrecioTotal(self):
        return self.getCantidad() * self.getPrecioUnitario()

    