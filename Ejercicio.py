#Esta linea de comandos le dice a Python que importe los Widget que son la parte visual del programa
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox)
import sys

#  Estas lineas desde la 8 a la 18 son las que definen el compartoamiento del programa
# con la interaccion del usuario
def agregar_proyecto():
    nombre = entrada_proyecto.text()
    if nombre.strip():
        QMessageBox.information(ventana, "Proyecto agregado",
                                f"✅ Se agregó el proyecto/compra:\n{nombre}")
        entrada_proyecto.clear()
    else:
        QMessageBox.warning(ventana, "Error", "Por favor ingresa un nombre válido.")

def salir_app():
    ventana.close()

# Configuración del programa. Estas lineas de comandos son la funcion que controla en 
# si todo el programa, manejando los eventos y la comunicacion con el sistema operativo
app = QApplication(sys.argv)
ventana = QWidget()

# Propiedades de la ventana. Estas lineas en el programa son las
# que establecen el texto que aparecera en la barra de titulo de la ventana
ventana.setWindowTitle("Gestión Personal de Proyectos y Compras")
ventana.setGeometry(200, 200, 400, 250)

# Estos son los Widgets estos son los elementos visuales del programa.
# Estos estan en el programa para agregar el texto en el programa,
# los botones y los demas funciones visuales con las que cuenta el programa
label_titulo = QLabel("📌 Gestor de proyectos y compras")
label_instruccion = QLabel("Ingrese el nombre del proyecto o compra:")

entrada_proyecto = QLineEdit()
entrada_proyecto.setPlaceholderText("Ejemplo: Laptop nueva, Proyecto final...")

boton_agregar = QPushButton("➕ Agregar")
boton_agregar.clicked.connect(agregar_proyecto)

boton_salir = QPushButton("❌ Salir")
boton_salir.clicked.connect(salir_app)

# Estas lineas de comandos son los  Layout. 
# Su funcion es organizar los widget de manera vertical uno debajo del otro
layout = QVBoxLayout()
layout.addWidget(label_titulo)
layout.addWidget(label_instruccion)
layout.addWidget(entrada_proyecto)
layout.addWidget(boton_agregar)
layout.addWidget(boton_salir)

ventana.setLayout(layout)

# Estas dos lineas de en el programa son las que inician
# el programa y lo mantienen en ejecucion
ventana.show()
sys.exit(app.exec_())
