class equation_manager:
    def __init__(self, x, y, z):
        self.set_vars(x, y, z)

    def set_vars(self, x=None, y=None, z=None):
        if x is None: x = self.vars[0]
        if y is None: y = self.vars[1]
        if z is None: z = self.vars[2]
        self.vars = [x, y, z]