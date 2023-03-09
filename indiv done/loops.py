#first loop, output is numbers 0 through 9 six times over
def one ():
    for i in range (0,6):
        for j in range (0,10):
            print(j, end = ' ')
        print()

#second loop
def two ():
    for i in range (0,10):
        for j in range (0,10):
            print(i, end = ' ')
        print()

#third loop
def three ():
    n = 0
    for i in range (0,10):
        n += 1
        for j in range (0,n):
            print(j, end = ' ')
        print()

#fourth loop
def four ():
    n = 11
    for i in range (0,10):
        n -= 1
        for l in range (i):
            print(' ', end = ' ')
        for j in range (0,n):
            print(j, end = ' ')
        print()

#fifth loop
def five ():
    n = 10
    for i in range (0,9):
        for j in range (0,i+1):
            print(n, end = ' ')
            n += 1
        print()

#execute everything
one()
print()
two()
print()
three()
print()
four()
print()
five()