from LazyGrad.Vector import Vector

class Matrix():
    def __init__(self, m, n, data=None):    

        self.m = m
        self.n = n

        self.data = Vector()

        for i in range(m):
            if data is not None and len(data[i]) != n:
                raise Exception(f'Incompatible size to build a matrix.')
            
            if data is not None:
                self.data.add(Vector(data[i]))
            else:
                self.data.add(Vector([0 if i != j else 1 for j in range(n)]))


    def __mul__(self, m2):
        if self.getNumCols() != m2.getNumRows():
            raise Exception(f'Cannot multiply matrices with incompatible sizes: {self.m}x{self.n} and {m2.getNumRows()}x{m2.getNumCols()}')
        
        result = Vector()

        for i in range(self.getNumRows()):
            for j in range(m2.getNumCols()):
                result.add(self.data[i].dot(m2.getColVec(j)))

    def __repr__(self):
        
        vectorString = "".join([f'\t{self.data[i].__repr__()}\n' for i in range(self.m)])
        return f'<Matrix {vectorString[1:-1]}>'
                
    def getColVec(self, colNum):
        colVec = Vector()
        for i in range(self.getNumRows()):
            for j in range(self.getNumCols()):
                if j == colNum: colVec.add(self.data[i][j])
        
        return colVec

    def getNumRows(self):
        return self.n

    def getNumCols(self):
        return self.m

    def convolve(self, kernel, padding=0, strides=1):

        k_width = kernel.getSize()//2

        newMatrix = Matrix(self.getNumRows()-1, self.getNumCols()-1)

        for i in range(newMatrix.getNumRows()):
            for j in range(newMatrix.getNumCols()):
                newMatrix.data[i][j] = sum([sum([self.data[i+r-k_width][j+c-k_width]*kernel.data[r][c] for c in range(kernel.getSize())]) for r in range(kernel.getSize())])
        
        return newMatrix

class Kernel(Matrix):
    def __init__(self,  size=3, data=None):
        super().__init__(size, size, data)

        self.size = size
    
    def getSize(self):
        return self.size




