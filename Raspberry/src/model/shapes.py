from basics import two_d_position
class abstract_shape():
    def __init__(self)->None:
        self.start : two_d_position = two_d_position()
        pass
class line(abstract_shape):
    def __init__(self)->None:
        super.__init__(self)
        pass
class arch_cw(abstract_shape):
    def __init__(self)->None:
        super.__init__(self)
        pass
class arch_ccw(abstract_shape):
    def __init__(self)->None:
        super.__init__(self)
        pass
class line_circle(abstract_shape):
    def __init__(self)->None:
        super.__init__(self)
        pass
class line_spiral(abstract_shape):
    def __init__(self)->None:
        super.__init__(self)
        pass
bob = abstract_shape()
print(bob.start.x)
print(bob.start.y)
bob.start.x = 5
print(bob.start.x)
