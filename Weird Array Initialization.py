class Array(list):
    def __init__(self, typecode,  val=None):
        self.typecode = typecode

        self.val = None
        if typecode is str:
            self.val = ''
        elif typecode is int:
            self.val = 0
        elif typecode is float:
            self.val = 0.0
        elif typecode is bool:
            self.val = False

    def __getitem__(self, key):
        if not hasattr(self, 'a'):
            setattr(self,'a', key)
            super(Array, self).__init__([self.val for v in range(key)])
            return self
        return list.__getitem__(self, key)

    def __setitem__(self, key, value):
        if type(value) is self.typecode:
            return list.__setitem__(self, key, value)
        elif value != None and type(value) is not self.typecode:
            raise TypeError