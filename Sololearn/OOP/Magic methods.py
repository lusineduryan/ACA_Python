class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = '=' * len(other.cont)
        return '\n'.join([self.cont, line, other.cont])

    def __gt__(self, other):
        for i in range(len(other.cont) + 1):
            result = other.cont[:i] + '>' + self.cont
            result += '>' + other.cont[i:]
            print(result)

lucy = SpecialString('Lucy')
duryan = SpecialString('Duryan')
print(lucy / duryan)
lucy > duryan