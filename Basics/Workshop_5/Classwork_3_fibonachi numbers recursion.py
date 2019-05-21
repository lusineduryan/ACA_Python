def fibonachi_number(n):
    if n <= 2:
        return 1
    else:
        return fibonachi_number(n - 1) + fibonachi_number(n - 2)

print(fibonachi_number(int(input())))