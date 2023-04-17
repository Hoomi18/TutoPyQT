import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QBoxLayout")


Flayout = QFormLayout()
Flayout.addRow("Name:", QLineEdit())
Flayout.addRow("Age:", QLineEdit())
Flayout.addRow("Job:", QLineEdit())
Flayout.addRow("Hobbies:", QLineEdit())
window.setLayout(Flayout)


Glayout = QGridLayout()
Glayout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
Glayout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
Glayout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
Glayout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
Glayout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
Glayout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
Glayout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
Glayout.addWidget(
    QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
)
window.setLayout(Glayout)

Vlayout = QVBoxLayout()
Vlayout.addWidget(QPushButton("Top"))
Vlayout.addWidget(QPushButton("Center"))
Vlayout.addWidget(QPushButton("Bottom"))
window.setLayout(Vlayout)

Hlayout = QHBoxLayout()
Hlayout.addWidget(QPushButton("Left"))
Hlayout.addWidget(QPushButton("Center"))
Hlayout.addWidget(QPushButton("Right"))
window.setLayout(Hlayout)


window.show()
sys.exit(app.exec())