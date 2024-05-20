import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
for i in range(217):
    shape = random.choice(['Line', 'Rect', 'Ellipse'])
    if shape == 'Line':
        elements.append(Line(0, 0, 0, 0))
    elif shape == 'Rect':
        elements.append(Rect(random.random(), random.random(), random.random(), random.random()))
    else:
        elements.append(Ellipse(random.random(), random.random(), random.random(), random.random()))
