def factorial(n):
    for i in range(1, n + 1):
        result = result * n
        return result

result = 1
print (factorial(3))