import math

class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    # string representation of vec3D
    def __repr__(self):
        return f"Vec3D({self.x}, {self.y}, {self.z})"
    #calculating eucledian norm also called magnitude of vector
    def len(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    #getitem is used  to acces individual components
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Invalid index")
    
    #setitem is used to modify individual components
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Invalid index")

    def __add__(self, other):
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vec3D):  # Cross product
            return Vec3D(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vec3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported operand type")     #raising custom error if float is not given

    def __rmul__(self, other):
        return self.__mul__(other)  # Allow scalar multiplication with vector on the right-hand side

    def __pow__(self, other):  # Dot product
        return self.x * other.x + self.y * other.y + self.z * other.z
    
u = Vec3D(1, 0, 0)  # (1,0,0) vector
v = Vec3D(0, 1, 0)


print(str(u))  
print(repr(u))  
print(u.len()) #magnitude
print(u[1])    #accessing
v[2] = 2.5     #modifying
print(u * v)
print(repr(u + v))      #repr and str applied to get desired output format  
print(repr(u - v))  
print(str(u ** v))