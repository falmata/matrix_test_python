class Matrix(object):
    """
    Classe pour représenter une matrice et réaliser les opérations de base :
    addition, soustraction, multiplication et calcul du déterminant.
    """
    # 1. initialize a matrix: ex.mat = Matrix([[1,2,3],[1,2,3]])
    def __init__ (self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    # 2. realize the basic operation add: ex. mat1 + mat2 = mat3
    def __add__(self, mat):
        if self.rows != mat.rows or self.cols != mat.cols:
            print("error")
        result = []

        for i in range(self.rows):
            rows_result = []
            for j in range(self.cols):
                rows_result.append(self.data[i][j] + mat.data[i][j])
            result.append(rows_result)
        return Matrix(result)

    # 3. calculate the determinant of a matrix: ex. mat.det
    def __det__(self):
        if self.rows != self.cols:
            print("error")
        det = 0

        for j in range(self.cols):
            matrix = []
            for i in range(self.rows):
                row = self.data[i][:j] + self.data[i][j+1:]
                matrix.append(row)
            minus = (-1) ** j
            mat = Matrix(matrix)
            det += minus * self.data[0][j] * mat.__det__()

        if self.rows == 1:
            return self.data[0][0]
        return det



if __name__ == '__main__':
    # Example

    # Test for #1
    mat1 = Matrix([[1,2,3],[1,4,3],[1,4,4]])

    # Test for #2
    mat2 = Matrix([[1,2,3],[1,4,3],[1,4,4]])
    mat3 = mat1 + mat2

    # Test for #3
    print(mat1)
    print(mat1.__det__())
    print(mat3)
    pass
