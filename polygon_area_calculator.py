class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.height >= 50 or self.width >= 50:
            return "Too big for picture."
        else:
            shape = ""

            for i in range(self.height):
                shape += "".center(self.width, "*")
                shape += "\n"
            return shape

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return f"Square(side={self.height})"


if __name__ == "__main__":
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
    sq.set_width(5)
    sq.set_height(5)
    print(sq)
    print(sq.get_picture())
    sq.set_height(50)
    sq.set_width(50)
    print(sq.get_picture())
    print(Rectangle(4, 8).get_amount_inside(Rectangle(3, 6)))
