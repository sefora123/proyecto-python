class Empleado:

    # Constructor
    def __init__(self, codigo, nombre, dni, horas, tarifa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__dni = dni
        self.__horas = horas
        self.__tarifa = tarifa
    
    # Métodos de acseso get y set
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getHoras(self):
        return self.__horas

    def getTarifa(self):
        return self.__tarifa 

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDni(self, dni):
        self.__dni = dni

    def setHoras(self, horas):
        self.__horas = horas

    def setTarifa(self, tarifa):
        self.__tarifa = tarifa
        
    # Métodos

    def sueldoBruto(self):
        return self.getHoras() * self.getTarifa()

    def descuentoESSALUD(self):
        return 12/100 * self.sueldoBruto()
    def descuentoAFP(self):
        return 11/100 * self.sueldoBruto()
    def descuentototal(self):
        return self.descuentoESSALUD()+self.descuentoAFP()
    def sueldoNeto(self):
        return self.sueldoBruto() - self.descuentototal()

    
