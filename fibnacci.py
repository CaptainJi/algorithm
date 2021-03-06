from timewrap import cal_time


def fibnacci(n):  # 时间复杂度O(2^n)
    if n == 0 or n == 1:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


@cal_time
def fib(n):
    return fibnacci(n)


@cal_time
def fib2(n): # 时间复杂度O(n);空间复杂度O(n)
    li = [1, 1]
    for i in range(2, n + 1):
        li.append(li[-1] + li[-2])
    return li[n]


@cal_time
def fib3(n): # 时间复杂度O(n);空间复杂度O(1)
    a = 1
    b = 1
    c = 0
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c

@cal_time
def fib3_1(n):
    a = 1
    b = 1
    c = 0
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


print(fib3(1200))
