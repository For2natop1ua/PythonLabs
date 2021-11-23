<h1 align="center">PythonLabs</h1>
<p align="center">
</p>

# Lab11-12
Написати програму на python + PyQt5 на допомогу медичним працівникам.
Користувач програми  повинен мати можливість завантажити з диска DICOM файл.
Програма має відобразити на екрані вміст цього файлу у вигляді зображення.

### main.py:
```python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main_form import Ui_MainWindow
import matplotlib.pyplot as plt
from pydicom import dcmread
import sys
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionupload_file.triggered.connect(self.btn_convert_clicked)

    def btn_convert_clicked(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "DICOM files (*.dcm)")
            fn = fname[0]
            ds = dcmread(fn)
            arr = ds.pixel_array
            plt.imshow(arr, cmap="gray")
            plt.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Помилка!")
            msg.setInformativeText('Під час завантаження файлу сталася помилка.')
            msg.setWindowTitle("Помилка")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_window = MainWindow()
    my_window.show()
    sys.exit(app.exec())
```
### main_form.py:
```python
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionupload_file = QtWidgets.QAction(MainWindow)
        self.actionupload_file.setObjectName("actionupload_file")
        self.menumenu.addAction(self.actionupload_file)
        self.menubar.addAction(self.menumenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DICOM Viewer"))
        self.menumenu.setTitle(_translate("MainWindow", "Меню"))
        self.actionupload_file.setText(_translate("MainWindow", "Завантажити файл"))
```
---
