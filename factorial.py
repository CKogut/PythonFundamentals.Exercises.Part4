def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print (factorial(5))

def fact_recur(n):
    if n == 0:
        return 0
    else:
        return factorial(n-1) * n

print (factorial(5))