from views.main_window import MainWindow
from models.matrix import Matrix
from PyQt6.QtWidgets import QTableWidgetItem
class MainController:
    def __init__(self, view:MainWindow, model:Matrix):
        self.view = view
        self.model = model
        self.view.count.textChanged.connect(self.__update_size)
        self.view.calculate.clicked.connect(self.__on_button_click_calculate)
    # Запуск рассчета матрицы
    def __on_button_click_calculate(self):
        # Получение матрицы с фронта
        self.__get_adjacency_matrix()
        # Передача матрицы в модель
        self.model.set_adjacency_matrix(self.__adjacency_matrix)
        # Получение матрицы правых инциденций из модели
        Gright_set= self.model.get_matrixs()  # Получаем данные из модели
        levels = self.model.get_levels()
        # Получение преобразованной нумерации
        Numbers=self.model.get_node_transpose()
        if Gright_set is None:
            print("Множества G не созданы")
        else:
            self.__to_one_start_node(Gright_set,Numbers)
            self.__set_calculated_set(self.view.matrix_Gright_table,Gright_set)
            self.__set_calculated_set(self.view.matrix_Gleft_table,Numbers) 
            self.__set_calculated_set(self.view.matrix_level_table,levels)
    
    # Преобразование старта не с 0 а с 1
    def __to_one_start_node(self,G_set,Numbers):
        for i in range(len(G_set)):
            G_set[i]=[v+1 for v in G_set[i]]
        for i in range(len(Numbers)):
            Numbers[i]+=1

    # Изменение размера матрицы смежности
    def __update_size(self):
        size=self.view.count.text()
        if str.isdigit(size):
            self.__size=min(int(size),100)
            self.view.count.setText(str(min(int(size),100)))
            self.__update_matrix()
    
    # Обновление матриц
    def __update_matrix(self):
        self.view.matrix_smez_table.setColumnCount(self.__size)
        self.view.matrix_smez_table.setRowCount(self.__size)
        for i in range(self.__size):
            self.view.matrix_smez_table.setColumnWidth(i,15)
            for j in range(self.__size):
                self.view.matrix_smez_table.setItem(i, j, QTableWidgetItem("0"))
    
    # Считывание матрицы в двумерных массив
    def __get_adjacency_matrix(self):
        adjacency_matrix=[[0]*self.__size for _ in range(self.__size)]
        for i in range(self.__size):
            for j in range(self.__size):
                text=self.view.matrix_smez_table.item(i,j).text()
                if text!="0" and str.isdigit(text):
                    adjacency_matrix[i][j]=int(text)
        self.__adjacency_matrix=adjacency_matrix
    # Передача полученных множеств на фронт
    def __set_calculated_set(self,table_set,G_set):
        size=len(G_set)
        table_set.setRowCount(size)
        table_set.setColumnCount(1)
        for i in range(size):
            table_set.setItem(i, 0, QTableWidgetItem(str(G_set[i])))