from PyQt6.QtWidgets import QMainWindow
from frontend.design import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.matrix_smez_table.resizeColumnsToContents()
        self.matrix_Gright_table.resizeColumnsToContents()