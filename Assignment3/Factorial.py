
def factorial(fact):
    if fact < 2:
        return 1
    else:
        return fact + factorial(fact - 1)


value = int(input("Enter a Number:"))

output = factorial(value)
print("Factorial of {} is {}".format(value, output))
