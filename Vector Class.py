class Vector:

    def __init__(self, *args):

        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            self.magnitude = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        else:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
            self.magnitude = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


    def __add__(self, other):
        c = [(self.x + other.x), (self.y + other.y), (self.z + other.z)]
        return Vector(c)

    def __sub__(self, other):
        c = [(self.x - other.x), (self.y - other.y), (self.z - other.z)]
        return Vector(c)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return '<{}, {}, {}>'.format(self.x, self.y, self.z)

    def __repr__(self):
        return str(self)

    def cross(self, other):
        c = [(self.y * other.z - other.y * self.z), (-self.x * other.z + self.z * other.x),
             (self.x * other.y - self.y * other.x)]
        return Vector(c)

    def dot(self, other):
        output = self.x * other.x + self.y * other.y + self.z * other.z
        return output

    def to_tuple(self):
        return tuple([self.x, self.y, self.z])