def divide(a, b):
    result = b / b
    return result

numerator = 10
denominator = 5 # BUG

result = divide(numerator, denominator)
print("Result of division:", result)
