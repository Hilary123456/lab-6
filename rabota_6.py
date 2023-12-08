class Figure:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_volume(self):
        return self.a * self.b * self.c
    
#Допзадание
    def __add__(self, other):
        if isinstance(other, Figure):
            return Figure(self.a + other.a, self.b + other.b, self.c + other.c)
        else:
            raise TypeError("Unsupported operand type for +")


class HollowBody(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def calculate_volume_without_void(self):
        return self.calculate_volume() - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
    
#Допзадание

    def __add__(self, other):
        if isinstance(other, HollowBody):
            # If both operands are instances of HollowBody, create a new HollowBody with combined dimensions
            return HollowBody(self.a + other.a, self.b + other.b, self.c + other.c, max(self.d, other.d))
        else:
            raise TypeError("Unsupported operand type for +")


# Example usage:

# Create figures
figure1 = Figure(2, 3, 4)
figure2 = Figure(3, 4, 5)

print('Figure1 volume: ', figure1.calculate_volume())
print('Figure2 volume: ', figure2.calculate_volume())
# Create hollow bodies
hollow_body1 = HollowBody(5, 6, 7, 1)
hollow_body2 = HollowBody(4, 5, 6, 2)

# Use the overloaded + operator
combined_figure = figure1 + figure2
combined_hollow_body = hollow_body1 + hollow_body2

# Display the result
print("Combined Figure:", combined_figure.calculate_volume())
print("Combined HollowBody:", combined_hollow_body.calculate_volume_without_void())
