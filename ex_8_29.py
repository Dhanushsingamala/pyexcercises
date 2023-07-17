import math

class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vec3D({self.x}, {self.y}, {self.z})"
    
    # vector has both magnitude and direction and scalar has only magnitude
    def __add__(self, other):
        if isinstance(other, Vec3D):  # Vector + Vector
            return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):  # Scalar + Vector
            return Vec3D(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError("Unsupported operand type")

    def __radd__(self, other):
        return self.__add__(other)  # Allow reverse order addition with scalar on the left-hand side

    def __sub__(self, other):
        if isinstance(other, Vec3D):  # Vector - Vector
            return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):  # Scalar - Vector
            return Vec3D(self.x - other, self.y - other, self.z - other)
        else:
            raise TypeError("Unsupported operand type")

    def __rsub__(self, other):
        return Vec3D(other - self.x, other - self.y, other - self.z)  # Reverse order subtraction with scalar on the left-hand side

    def __mul__(self, other):
        if isinstance(other, Vec3D):  # Vector * Vector (Cross product)
            return Vec3D(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        elif isinstance(other, (int, float)):  # Scalar * Vector
            return Vec3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported operand type")

    def __rmul__(self, other):
        return self.__mul__(other)  # Allow reverse order multiplication with scalar on the left-hand side

    def __truediv__(self, other):
        if isinstance(other, (int, float)):  # Vector / Scalar
            return Vec3D(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Unsupported operand type")

u = Vec3D(1, 0, 0)
v = Vec3D(0, -0.2, 8)
a = 1.2
b= 2.5j
print(u + v)  
print(a + v)  
print(v + a)  
print(a - v)  
print(v - a)  
print(a * v)  
print(v * a)  
print(v / a)  
print( u * b)
