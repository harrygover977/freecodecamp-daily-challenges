def prime_factorization(number: int) -> list[int]:
    """Return a list of number's primer factors."""
    prime_factors = {}
    denominator = 2
    while number > 1:
        if number % denominator == 0:
            if denominator in prime_factors:
                prime_factors[denominator] += 1
            else:
                prime_factors[denominator] = 1
            number = number / denominator
            denominator = 2
        else: 
            denominator += 1
    return prime_factors

def lcm(a: int, b: int) -> int:
    """Return the lowest common multiple of a and b."""
    lowest_common_multiple = 1
    prime_factors_a = prime_factorization(a)
    prime_factors_b = prime_factorization(b)
    for i in range(max(a, b)):
        factor = i + 2
        if factor in prime_factors_a and factor in prime_factors_b:
            lowest_common_multiple *= factor ** max(prime_factors_a[factor], prime_factors_b[factor])
        elif factor in prime_factors_a:
            lowest_common_multiple *=  factor ** prime_factors_a[factor]
        elif factor in prime_factors_b:
            lowest_common_multiple *= factor ** prime_factors_b[factor]
    return lowest_common_multiple
    
assert lcm(4, 6) == 12
assert lcm(9, 6) == 18
assert lcm(10, 100) == 100
assert lcm(13, 17) == 221
assert lcm(45, 70) == 630
