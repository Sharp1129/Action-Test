def hannuo(n, a, b, c):
    global i
    if n == 1:
        print(a, '->', c)
        return
    else:
        hannuo(n-1, a, c, b)
        print(a, '->', c)
        hannuo(n-1, b, a, c)

hannuo(5, 'A', 'B', 'C')
