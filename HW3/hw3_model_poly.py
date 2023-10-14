# Copyright 2023 Jinzhi Shen/Xulun Huang  jinzhis9@bu.edu/jasonh1@bu.edu
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
            result += coeff * (x **(degree))

        return result
    
    def deriv(self):
        derivative = Polynomial()
        for degree, coeff in self.coefficients.items():
            if degree == 0:
                pass
            else:
                degree_new = degree -1
                coeff_new = degree * coeff
                derivative.coefficients[degree_new] = coeff_new
        return derivative
    
    def __getitem__(self, degree):
        return self.coefficients.get(degree, 0)


