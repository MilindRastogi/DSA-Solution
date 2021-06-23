def fibonaci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonaci(n-1) + fibonaci(n-2)


a = int(input())
print(fibonaci(a))
