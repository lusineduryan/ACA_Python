def all_poss(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return all_poss(n - 1) + all_poss(n - 2)

print(all_poss(int(input())))