from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox)
import sys

#  Funciones del programa 
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

# Configuración del programa
app = QApplication(sys.argv)
ventana = QWidget()

# Propiedades de la ventana
ventana.setWindowTitle("Gestión Personal de Proyectos y Compras")
ventana.setGeometry(200, 200, 400, 250)

# --- Widgets ---
label_titulo = QLabel("📌 Gestor de proyectos y compras")
label_instruccion = QLabel("Ingrese el nombre del proyecto o compra:")

entrada_proyecto = QLineEdit()
entrada_proyecto.setPlaceholderText("Ejemplo: Laptop nueva, Proyecto final...")

boton_agregar = QPushButton("➕ Agregar")
boton_agregar.clicked.connect(agregar_proyecto)

boton_salir = QPushButton("❌ Salir")
boton_salir.clicked.connect(salir_app)

# --- Layout ---
layout = QVBoxLayout()
layout.addWidget(label_titulo)
layout.addWidget(label_instruccion)
layout.addWidget(entrada_proyecto)
layout.addWidget(boton_agregar)
layout.addWidget(boton_salir)

ventana.setLayout(layout)

# Mostrar ventana
ventana.show()
sys.exit(app.exec_())
