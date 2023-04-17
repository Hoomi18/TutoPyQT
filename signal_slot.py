import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from functools import partial

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World!")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
button = QPushButton("Greet")
button.clicked.connect(partial(greet, "World!"))
def greet(name):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f"Hello, {name}")
sys.exit(app.exec())

