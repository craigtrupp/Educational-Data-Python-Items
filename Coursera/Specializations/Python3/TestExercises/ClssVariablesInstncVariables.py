class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())


# 4
# 3 *
# 2
# 1
# 01234

# 3
# 2  *
# 1
# 0
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 01234567890123


# graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:
# looking up p1 and finding that it’s an instance of Point
# looking for an instance variable called graph in p1, but not finding one
# looking for a class variable called graph in p1’s class, the Point class; it finds a function/method object
# Because of the () after the word graph, it invokes the function/method object, with the parameter self bound to the object p1 points to.

