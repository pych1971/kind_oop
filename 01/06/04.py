class Point:

    def __init__(self, x, y, cl=False):
        self.x = x
        self.y = y
        self.cl = cl

    def clone(self):
        return Point(self.x, self.y)


pt = Point(5, 5)
pt_clone = pt.clone()
