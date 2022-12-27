import sys
from PyQt5 import QtWidgets, uic
from claseEmpleado import Empleado

qtCreatorFile = "EVALUACION_CONTINUA_3/PaqueteEmpleado/frmEmpleado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class formularioEmpleado(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(formularioEmpleado, self).__init__(parent)
        uic.loadUi("EVALUACION_CONTINUA_3/PaqueteEmpleado/frmEmpleado.ui", self)

        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCerrar.clicked.connect(self.cerrar)
        self.show()

    def aceptar(self):
        empleado = Empleado(12345, "SEFORA",74565298, 30,35)
        self.mostrarDatos(empleado)

        
    def imprimir(self, cad):
        self.txtS.append(cad)
    
    def mostrarDatos(self, Empleado):
        self.imprimir("CODIGO\t\t: " + str(Empleado.getCodigo()))
        self.imprimir("NOMBRE\t\t: " + str(Empleado.getNombre()))
        self.imprimir("DNI\t\t: " + str(Empleado.getDni()))
        self.imprimir("HORAS\t\t: " + str(Empleado.getHoras()))
        self.imprimir("TARIFA\t\t: " + str(Empleado.getTarifa()))
        self.imprimir("")
        self.imprimir("sueldo bruto\t\t: " + str(Empleado.sueldoBruto()))
        self.imprimir("DESCUENTO ESSALUD\t: " + str(Empleado.descuentoESSALUD()))
        self.imprimir("DESCUENTO AFP\t: " + str(Empleado.descuentoAFP()))
        self.imprimir("DESCUENTO TOTAL\t: " + str(Empleado.descuentototal()))
        self.imprimir("SUELDO NETO\t\t: " + str(Empleado.sueldoNeto()))

    def cerrar(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = formularioEmpleado()
    app.exec()