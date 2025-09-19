
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QPushButton,
    QVBoxLayout, QLineEdit, QMessageBox
)
import sys

# Lista para almacenar las tareas
tareas = []

def agregar_tarea():
    """Agrega la tarea escrita en el QLineEdit a la lista"""
    texto = entrada_tarea.text().strip()
    if texto:  
        tareas.append(texto)
        entrada_tarea.clear()
        QMessageBox.information(ventana, "Tarea agregada", f"La tarea '{texto}' fue añadida.")
    else:
        QMessageBox.warning(ventana, "Advertencia", "No puedes agregar una tarea vacía.")

def mostrar_tareas():
    """Muestra todas las tareas guardadas"""
    if tareas:
        lista = "\n".join([f"{i+1}. {t}" for i, t in enumerate(tareas)])
        QMessageBox.information(ventana, "Lista de Tareas", lista)
    else:
        QMessageBox.information(ventana, "Lista de Tareas", "No hay tareas registradas.")

# Configuración inicial de la aplicación
app = QApplication(sys.argv)
ventana = QWidget()

# Propiedades de la ventana
ventana.setWindowTitle("Gestor de Tareas - PyQt5")
ventana.setGeometry(200, 200, 400, 250)

# Layout
layout = QVBoxLayout()

# Widgets
titulo = QLabel("📌 Gestor de Tareas")
titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: darkblue;")

label_instruccion = QLabel("Escribe una tarea y agrégala:")
entrada_tarea = QLineEdit()
entrada_tarea.setPlaceholderText("Ejemplo: Estudiar para el examen...")

boton_agregar = QPushButton("➕ Agregar tarea")
boton_agregar.setStyleSheet("background-color: lightgreen; font-weight: bold;")
boton_agregar.clicked.connect(agregar_tarea)

boton_mostrar = QPushButton("📋 Mostrar tareas")
boton_mostrar.setStyleSheet("background-color: lightblue; font-weight: bold;")
boton_mostrar.clicked.connect(mostrar_tareas)

# Agregar widgets al layout
layout.addWidget(titulo)
layout.addWidget(label_instruccion)
layout.addWidget(entrada_tarea)
layout.addWidget(boton_agregar)
layout.addWidget(boton_mostrar)

ventana.setLayout(layout)
ventana.show()

sys.exit(app.exec_())
