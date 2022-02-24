import math
print("Hello world!")

def fibonacci():
    n = input()
    try:
        n = int(n)
    except ValueError:
        print('Invalid')
        fibonacci()
    x = 0
    y = 1
    fib = []
    g_ratio = (1+math.sqrt(5))/2
    for i in range(n):
        z = x+y
        x = y
        y = z
        fib.append(z)
    ratio = fib[-1]/fib[-2]
    print(fib)
    print('Ratio = '+str(ratio))
    print('Difference =' + str(ratio-g_ratio))
    fibonacci()
fibonacci()
