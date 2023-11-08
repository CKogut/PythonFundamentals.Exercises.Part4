def fibonacci(n):
    if n < 0:
        print("Need a number greater than or equal to zero.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))