class Line:
    def __init__(self, x0, y0, x1, y1):
        self.m = (x1 - x0) / (y1 - y0)
        if x0 < x1:
            self.domain = (x0, x1)
        else:
            self.domain = (x1, x0)
        if y0 < y1:
            self.range = (y0, y1)
        else:
            self.range = (y1, y0)
        self.b = -1 * self.m * x0 + y0

    def y_at(self, x):
        return self.m * x + self.b


def shared_dr(line1, line2):
    shared_domain = False
    shared_range = False
    if (line1.domain[0] <= line2.domain[0] <= line1.domain[1]) or (line2.domain[0] <= line1.domain[0] <= line2.domain[1]):
        shared_domain = True
    if (line1.range[0] <= line2.range[0] <= line1.range[1]) or (line2.range[0] <= line1.range[0] <= line2.range[1]):
        shared_range = True
    return shared_domain and shared_range


def find_int(line1, line2):
    x = (line1.b - line2.b) / (line2.m - line1.m)
    y = line1.y_at(x)
    return (x, y)


def intercept(line1, line2):
    if shared_dr(line1, line2):
        print(find_int(line1, line2))
    else:
        print("None")


testline1 = Line(-1, -1, 2, 2)
testline2 = Line(-2, 2, 1, -1)
intercept(testline1, testline2)
