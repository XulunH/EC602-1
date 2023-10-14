class Polynomial:
    def __init__(self, coefficients=None):
        if coefficients is None:
            self.coefficients = {}
        else:
            num_coeffs = len(coefficients)
            self.coefficients = {num_coeffs - 1 - i: coeff for i, coeff in enumerate(coefficients)}
            ##print(self.coefficients)

    def __str__(self):
        res = ""
        for degree, coeff in sorted(self.coefficients.items(), reverse=True):
            term = ""
            if coeff != 1 or degree == 0:
                term += f"{coeff:g}"
            if degree > 0:
                term += "x"
            if degree > 1:
                term += f"^{degree}"
            if degree < 0:
                term += f"^{degree}"
            if res and term:
                res += " + "
            res += term

        return res
    
    def __add__(self, other):
        result = Polynomial()
        for degree in set(self.coefficients) | set(other.coefficients):
            result.coefficients[degree] = self.coefficients.get(degree, 0) + other.coefficients.get(degree, 0)
        return result
    
    def __sub__(self, other):
        result = Polynomial()
        for degree in set(self.coefficients) | set(other.coefficients):
            result.coefficients[degree] = self.coefficients.get(degree, 0) - other.coefficients.get(degree, 0)
        return result
    
    def __mul__(self, other):
        result = Polynomial()
        for degree1, coeff1 in self.coefficients.items():
            for degree2, coeff2 in other.coefficients.items():
                degree = degree1 + degree2
                result.coefficients[degree] = result.coefficients.get(degree, 0) + coeff1 * coeff2

        result.coefficients = {degree: coeff for degree, coeff in result.coefficients.items() if coeff != 0}

        return result
    
    def __eq__(self, other):
        return self.coefficients == other.coefficients
    
    def __setitem__(self, degree, coefficient):
        self.coefficients[degree] = coefficient

    def eval(self, x):
        result = 0
        for degree, coeff in self.coefficients.items():
            print("print degree")
            print(degree)
            print("print coeff")
            print(coeff)
            result += coeff * (x **(degree))

        return result
    
    def deriv(self):
        derivative = Polynomial()
        for degree, coeff in self.coefficients.items():
            degree_int = int(degree.split('^')[-1])
            new_degree = degree_int - 1
            new_coeff = coeff * degree_int
            if new_degree == 0:
                derivative[0] = new_coeff
            elif new_degree > 0:
                derivative[new_degree] = new_coeff
            elif new_degree < 0:
                derivative[-abs(new_degree)] = new_coeff
        return derivative
    
    def __getitem__(self, degree):
        return self.coefficients.get(degree, 0)

## evaluation test
q1 = Polynomial([4,1])
p1 = Polynomial([4,0,1])
print(p1[1],4)


