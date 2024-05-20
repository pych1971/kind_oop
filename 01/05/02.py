class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
x = 1
y = 1
for i in range(1000):
    if i == 1:
        points.append(Point(x, y, 'yellow'))
    else:
        points.append(Point(x, y))
    x += 2
    y += 2
