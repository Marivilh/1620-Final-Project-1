import sys
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("gui.ui")
window.show()
app.exec()

# FIXME: try to get pyuic6 to work, until then this is needed
# it really pissed me off trying to get pyuic6 to work so i just went with this
# that i foun on this website https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/