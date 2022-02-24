string = 'banana'
bananarray = []
def banana():
    for i in range(10):
        n = 20 + i 
        print(string.upper().center(n,'!'))
        print(string.lower().center(n,'-'))

bananarray.append(banana())
print(bananarray)

def factorial():
    x = input()
    try:
        x = int(x)
    except ValueError:
        print('Invalid input')
        factorial()
    y = x
    for i in range(1,x):
        y=y * (x-i)
    print('Result: ' + str(y))
    factorial()
factorial()
