import sys
from PyQt5 import QtWidgets, uic
from claseProducto import Producto

qtCreatorFile = "evaluacion_continua_3/PaqueteProducto/frmProducto.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

tipo = Producto()

class FormularioProducto(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(FormularioProducto, self).__init__(parent)
        uic.loadUi("evaluacion_continua_3/PaqueteProducto/frmProducto.ui",self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnMostrar.clicked.connect(self.mostrar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()

    def registrar(self):
        tipo.setCodigo(self.txtCodigo.text())
        tipo.setDescripcion(self.txtDescripcion.text())
        tipo.setCantidad(float(self.txtCantidad.text()))
        tipo.setPrecioUnitario(float(self.txtPrecioUnitario.text()))
        
        self.txtCodigo.setText("")
        self.txtDescripcion.setText("")
        self.txtCantidad.setText("")
        self.txtPrecioUnitario.setText("")

    def imprimir(self,cad):
        self.txtS.append(cad)

    def mostrar(self):
        self.imprimir("CODIGO\t\t: " + tipo.getCodigo())
        self.imprimir("DESCRIPCION\t\t: " + tipo.getDescripcion())
        self.imprimir("CANTIDAD\t\t: " + str(tipo.getCantidad()))
        self.imprimir("PRECIO UNITARIO\t: S/. " + str(tipo.getPrecioUnitario()))
        self.imprimir("PRECIO TOTAL\t\t: S/. " + str(tipo.PrecioTotal()))
        self.imprimir("")

    def limpiar(self):
        self.txtCodigo.setText("")
        self.txtDescripcion.setText("")
        self.txtCantidad.setText("")
        self.txtPrecioUnitario.setText("")
        self.txtS.setText("")

    def salir(self):
        self.close()

        

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioProducto()
    app.exec()