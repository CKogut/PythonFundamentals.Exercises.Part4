def fibonacci(n):
    # a serves as n-2
    a = 0
    # b serves as n-1
    b = 1
    
    if n < 0:
        print("Need a number greater than or equal to zero.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            # temp holds the fibonacci of current i
            temp = a + b
            # shift a up to a new (n-2)
            a = b
            # shift b up to a new (n-1)
            b = temp
        return b

    
print(fibonacci(7))