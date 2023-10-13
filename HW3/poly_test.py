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
            degree = int(degree.split('^')[-1])
            result += coeff * (x ** degree)
        return result
    
    

## test for construction    
   
print(Polynomial([4,-9,5.6]))

p1 = Polynomial([4, 0, -4, 3, 0])
p2 = Polynomial([-0.8, 2.3, 0.5, 1, 0.2])

## test for add and sub
p_sum = p1 + p2
p_diff = p1 - p2
print(p_sum) 
print(p_diff) 

## test for multiply
p1 = Polynomial([1, -2, 1])  
p2 = Polynomial([1, 2])      

result_mul = p1 * p2
print(result_mul)


## test for equal
p1 = Polynomial([1, -2, 1])  # Represents (x^2 - 2x + 1)
p2 = Polynomial([1, -2, 1])  # Represents the same polynomial

p3 = Polynomial([1, -2, 1])  # Represents the same polynomial as p1

print(p1 == p2)  # Output: True (p1 and p2 have the same coefficients)
print(p1 == p3)  # Output: True (p1 and p3 have the same coefficients)

## test for sparse with multiply that don't time out
q = Polynomial()
p = Polynomial()
w = Polynomial()
q[20000]= 5
q[10000] = 1
      
p[30000] = 4
p[1] = 3
w = p*q
print(w)

## test for negative
a = Polynomial()
a[-1] = 3
print(a)

## test for evaluate
p = Polynomial()
p["x^2"] = 4
p["x^1"] = 3
p["x^-1"] = 2

x_value = 2.1
result = p.eval(x_value)
print(f"p({x_value}) = {result}")


# test for substitute
c = Polynomial([1,2,3])
print(c)
c[0] = 5
print(c)


#test for derivative



