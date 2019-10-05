class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "Vector[x: " + str(self.x) + ", y: " + str(self.y) + "]" 


v = Vector(1, 0)
u = Vector(0, 1)

print(u.add(v))