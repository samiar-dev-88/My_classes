
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
    QRadioButton

)

import sys

# Creat Window
app = QApplication(sys.argv) # Creat app
window = QWidget() # Window
window.setWindowTitle("PyQt5 Complete Demo") # Title
window.resize(500, 500) # Size
central_widget = QWidget() # Main widget

a = QLabel("Hello" , window)
a.move(20,20)

b = QPushButton("Click me" , window)
b.move(60,20)
def butt():
    print("Hi")
b.clicked.connect(butt)

c = QLineEdit(window)
c.move(200,20)
tex = c.text()
c.setPlaceholderText("Enter your name...")
c.setEchoMode(QLineEdit.Password)
c.clear()

d = QCheckBox("Turn on..." , window)
d.move(40,40)
checkk = d.isChecked()
print(checkk)

e = QRadioButton("python" , window)
e.move(40,40)
f = QRadioButton("python" , window)
f.move(40,200)
g = QRadioButton("python" , window)
g.move(40,400)
radio = e.isChecked()
print(radio)

window.show()
sys.exit(app.exec_())