class Vector():
    def __init__(self, data=None):
    
        self.data = data if data is not None else list()

    def add(self, item):
        self.data.append(item)

    def dot(self, v2):
        if len(self.data) != len(v2.data):
            raise Exception(f'Cannot perform the dot product for vector of different sizes: {len(self.data)} and {len(v2.data)}')

        return sum([self.data[i]*v2.data[i] for i in range(self.data)])

    def __repr__(self):
        elementString = "".join([f'{self.data[i]}, ' for i in range(len(self.data))])
        return f'<Vector data=[{elementString[:-2]}]>'

    def __getitem__(self, item):
         return self.data[item]
    
    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

        
