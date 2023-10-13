class Polynomial:
    def __init__(self, coefficients=None):
        if coefficients is None:
            self.coefficients = []
        else:
            self.coefficients = coefficients
        ## the data type is list

    def __str__(self):

        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree+1):
            coeff = self.coefficients[i]
            # nothing has to be done if coeff is 0:
            if abs(coeff) == 1 and i < degree:
                # 1 in front of x shouldn't occur, e.g. x instead of 1x
                # but we need the plus or minus sign:
                res += f"{'+' if coeff>0 else '-'}{x_expr(degree-i)}"  
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree-i)}" 

        return res.lstrip('+')    # removing leading '+'
 

    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(res[::-1])

    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1] 
        res = [t1-t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(res[::-1])


    def __mul__(self, other):
        degree1 = len(self.coefficients) - 1
        degree2 = len(other.coefficients) - 1


        result_coefficients = [0] * (degree1 + degree2 + 1)

        for i in range(degree1 + 1):
            for j in range(degree2 + 1):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result_coefficients)

    def __eq__(self, other):
        return self.coefficients == other.coefficients
    
    def __setitem__(self, degree, coefficient):
        if degree < 0:
            raise ValueError("Degree must be non-negative.")
        if degree < len(self.coefficients):
            self.coefficients[-(degree + 1)] = coefficient
        else:
            self.coefficients.extend([0] * (degree - len(self.coefficients) + 1))
            self.coefficients[-(degree + 1)] = coefficient

    


### here is the list for the helper-functions
def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res

def zip_longest(iter1, iter2, fillvalue=None):
    
    for i in range(max(len(iter1), len(iter2))):
        if i >= len(iter1):
            yield (fillvalue, iter2[i])
        elif i >= len(iter2):
            yield (iter1[i], fillvalue)
        else:
            yield (iter1[i], iter2[i])
        i += 1

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


