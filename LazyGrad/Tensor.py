class Tensor():
    def __init__(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = []

        self.size = len(self.data)

    def getSize(self):
        return self.size

    def __repr__(self):
        return f'<Tensor size={len(self.data)}, data={self.data}>'

    def __add__(self, t2):
        if self.getSize() != t2.getSize():
            raise Exception(f'Tensor size must be equal for adition, got {self.getSize()} and {t2.getSize()}.')

        return [self.data[i] + t2.data[i] for i in range(self.size)]

    def __mul__(self, t2):
        if self.getSize() != t2.getSize():
            raise Exception(f'Tensor size must be equal for adition, got {self.getSize()} and {t2.getSize()}.')

        return [self.data[i] * t2.data[i] for i in range(self.size)]
