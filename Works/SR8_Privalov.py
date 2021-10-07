def f(n, base = 2):
    s = ''
    while n > 0:
        s += str(n%base)
        n //= base
    return s[::-1]

while 1:
    try:
        print("Enter the num:", end = '')
        a = int(input())
        print("Enter the base of system: ", end = '')
        b = int(input())

        print(a, "-", f(a, b))
        break
    except ValueError:
        print("No books next time!")
