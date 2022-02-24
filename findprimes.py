def findprimes():
    n = input()
    try:
        n = int(n)
    except ValueError:
        print('Invalid input')
        findprimes()
    primes =[]
    for i in range(2,n):
        for j in range(2,(i+1)//2):
            if i%j == 0:
                break
        else:
            primes.append(i)
    primes.remove(4)
    print(primes)
    findprimes()
findprimes()
