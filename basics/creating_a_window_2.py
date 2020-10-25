from PySide2.QtWidgets import QApplication, QPushButton

import sys

app = QApplication(sys.argv)

window = QPushButton()
window.show()

app.exec_()