def fibonacci(n):
    """
    Generate a list containing the Fibonacci series up to n terms.

    Args:
        n (int): Number of terms to generate

    Returns:
        list: Fibonacci series as a list of integers
    """
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


def factorial(num):
    """
    Recursively calculate the factorial of a number.

    Args:
        num (int): The number to calculate factorial for. Should be >= 0.

    Returns:
        int: Factorial of the number

    Raises:
        ValueError: If num is negative
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# Hands-on: Generate Fibonacci series using loops and functions
terms = 10
print(f"Fibonacci series with {terms} terms:")
print(fibonacci(terms))

print("\n" + "-"*40 + "\n")

# Exercise: Factorial using recursion and docstrings
try:
    n = 5
    print(f"Factorial of {n} is: {factorial(n)}")
except ValueError as e:
    print(e)

# Optional: Demonstrate the docstrings usage
print("\nFunction documentation:")
print("fibonacci docstring:")
print(fibonacci.__doc__)
print("\nfactorial docstring:")
print(factorial.__doc__)
