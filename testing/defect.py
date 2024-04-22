def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error:", e)
    return result

numerator = 10
denominator = '2'  # Defect

result = divide(numerator, denominator)
print("Result of division:", result)
