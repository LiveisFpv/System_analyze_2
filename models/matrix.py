import queue
class Matrix:
    def __init__(self):
        self.__size=0
    def set_adjacency_matrix(self, adjacency_matrix):
        # Проверка на пустую матрицу
        if not adjacency_matrix or not isinstance(adjacency_matrix, list):
            raise ValueError("Матрица должна быть списком с хотя бы одним элементом")
        size=len(adjacency_matrix)
        self.__size=size
        if any(len(row) != size for row in adjacency_matrix):
            raise ValueError("Матрица должна быть квадратной (NxN)")
        self.__adjacency_matrix = adjacency_matrix
        self.__create_Gright_set()
        self.__create_Gleft_set()
        self.__create_leveled_Gright_matrix()
    def __create_Gright_set(self):
        self.__Gright_set=[[]for _ in range(self.__size)]
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__adjacency_matrix[i][j] > 0:
                    self.__Gright_set[i].append(j)
    def __create_Gleft_set(self):
        self.__Gleft_set=[[]for _ in range(self.__size)]
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__adjacency_matrix[j][i] > 0:
                    self.__Gleft_set[i].append(j)
    def get_matrixs(self)->tuple[list]|tuple[None]:
        if self.__size >0:
            return (self.__Gright_set, self.__Gleft_set)
        else:
            return None, None
    def __create_leveled_Gright_matrix(self):
        queue_el=[]
        for i,el in enumerate(self.__Gleft_set):
            if len(el)==0:
                queue_el.append(i)
        self.__search_levels(queue_el)
        
        return None
    def __search_levels(self,queue_el:list,):
        levels=[0]*self.__size
        for el in queue_el:
            q=queue.PriorityQueue()
            q.put((0,el))
            while not q.empty():
                level,q_el=q.get()
                levels[q_el]=max(levels[q_el],-level)
                for v in self.__Gright_set[q_el]:
                    if (-level)>=levels[v]:
                        q.put((level-1,v))
        print(levels)

        


if __name__ == "__main__":
    # Пример использования
    adjacency_matrix=[[0, 1, 0, 1],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1],
                     [0, 0, 0, 0]]
    matrix=Matrix()
    matrix.set_adjacency_matrix(adjacency_matrix)
    Gright_set,Gleft_set=matrix.get_matrixs()
    print("Матрица правых инциденций G+:")
    print(Gright_set)
    print("Матрица левых инциденций G-:")
    print(Gleft_set)