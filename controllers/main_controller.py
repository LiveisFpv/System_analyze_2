from views.main_window import MainWindow
from models.matrix import Matrix
from PyQt6.QtWidgets import QTableWidgetItem
class MainController:
    def __init__(self, view:MainWindow, model:Matrix):
        self.view = view
        self.model = model
        self.view.count.textChanged.connect(self.__update_size)
        self.view.calculate.clicked.connect(self.__on_button_click_calculate)
    def __on_button_click_calculate(self):
        self.__get_adjacency_matrix()
        self.model.set_adjacency_matrix(self.__adjacency_matrix)
        Gright_set,Gleft_set = self.model.get_matrixs()  # Получаем данные из модели
        if Gright_set is None:
            print("Множества G не созданы")
        else:
            self.__set_calculated_set(self.view.matrix_Gright_table,Gright_set)
            self.__set_calculated_set(self.view.matrix_Gleft_table,Gleft_set)
    def __update_size(self):
        size=self.view.count.text()
        if str.isdigit(size):
            self.__size=min(int(size),100)
            self.view.count.setText(str(min(int(size),100)))
            self.__update_matrix()
    def __update_matrix(self):
        self.view.matrix_smez_table.setColumnCount(self.__size)
        self.view.matrix_smez_table.setRowCount(self.__size)
        for i in range(self.__size):
            self.view.matrix_smez_table.setColumnWidth(i,15)
            for j in range(self.__size):
                self.view.matrix_smez_table.setItem(i, j, QTableWidgetItem("0"))
    def __get_adjacency_matrix(self):
        adjacency_matrix=[[0]*self.__size for _ in range(self.__size)]
        for i in range(self.__size):
            for j in range(self.__size):
                text=self.view.matrix_smez_table.item(i,j).text()
                if text!="0" and str.isdigit(text):
                    adjacency_matrix[i][j]=int(text)
        self.__adjacency_matrix=adjacency_matrix
    def __set_calculated_set(self,table_set,G_set):
        size=len(G_set)
        table_set.setRowCount(size)
        table_set.setColumnCount(1)
        for i in range(size):
            table_set.setItem(i, 0, QTableWidgetItem(str(G_set[i])))