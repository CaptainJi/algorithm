def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, B, C)
        print(f'{A}->{C}')
        hanoi(n - 1, B, A, C)

hanoi(4,'a','b','c')