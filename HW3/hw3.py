class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(str(coef))
                else:
                    if coef == 1:
                        terms.append(f"x^{i}")
                    else:
                        terms.append(f"{coef}x^{i}")
        return " + ".join(terms[::-1])

    def __add__(self, other):
        result = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        for i in range(max_len):
            self_coef = self.coefficients[i] if i < len(self.coefficients) else 0
            other_coef = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(self_coef + other_coef)
        return Polynomial(result)

    def __sub__(self, other):
        result = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        for i in range(max_len):
            self_coef = self.coefficients[i] if i < len(self.coefficients) else 0
            other_coef = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(self_coef - other_coef)
        return Polynomial(result)

    def __mul__(self, other):
        result = [0] * (
