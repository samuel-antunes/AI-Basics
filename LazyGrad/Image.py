from LazyGrad.Matrix import Kernel

class Image():
    def __init__(self, data):
        self.data = data

        self.width = len(data)
        self.height = len(data[0])

    
