import equations as eq

class equation_manager:
    def __init__(self, x, y, z):
        self.set_vars(x, y, z)

    def set_vars(self, x=None, y=None, z=None):
        if x is None: x = self.vars[0]
        if y is None: y = self.vars[1]
        if z is None: z = self.vars[2]
        self.vars = [x, y, z]

    def get_solutions(self):
        return [eq.solve_eq1(self.vars[0]), eq.solve_eq2(self.vars[1], self.vars[2]), eq.solve_eq3(self.vars[0], self.vars[1], self.vars[2])]