from pickle import dump, load

# a = {'Vahan':1998}

# with open('test1.txt', 'xb') as fd:
#     dump(a, fd)

# with open('test1.txt', 'rb') as fd:
#     print(load(fd))

with open('test1.txt', 'rb') as fd:
    fact_cache = load(fd)
# fact_cache = {0: 1}


def fact(n):
    if n in fact_cache:
        return fact_cache[n]
    print('Computed for:', n)
    fact_cache[n] = fact(n-1)*n
    return fact_cache[n]


print(fact(102))
print(fact_cache)
with open('test1.txt', 'wb') as fd:
    dump(fact_cache, fd)