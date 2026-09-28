# -------------------------------
# Section 1: Classic textbook-style (plagiarized feel)
# -------------------------------

# Bubble Sort (common example found in many sources)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Factorial using recursion (standard example)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# -------------------------------
# Section 2: AI-generated creative utilities
# -------------------------------

# Generate Fibonacci numbers using a generator
def fibonacci_gen(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# AI-style creative: palindrome checker with comprehension
def is_palindrome(s):
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]

# AI-style creative: matrix transpose using zip
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


# -------------------------------
# Section 3: Mixed utilities
# -------------------------------

# Textbook-like gcd (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# AI-generated: random sentence generator
import random

def random_sentence():
    subjects = ["AI", "Python", "Student", "Developer"]
    verbs = ["creates", "analyzes", "builds", "tests"]
    objects = ["code", "project", "algorithm", "system"]
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."


# -------------------------------
# Section 4: Main execution
# -------------------------------

if __name__ == "__main__":
    print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print("Factorial(5):", factorial(5))
    print("Fibonacci(10):", list(fibonacci_gen(10)))
    print("Is 'Racecar' palindrome?:", is_palindrome("Racecar"))
    print("Transpose:", transpose_matrix([[1,2,3],[4,5,6]]))
    print("GCD(48,18):", gcd(48,18))
    print("Random Sentence:", random_sentence())
