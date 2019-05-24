from itertools import count, repeat

for i in count(3):
    print(i)
    if i >= 9:
        break

for i in repeat(10, 3):
    print(i)

from itertools import accumulate, takewhile

nums = list(accumulate(range(5)))
print(nums)

print(list(takewhile(lambda x: x <= 5, nums)))

from itertools import product, permutations

letters = ("A", "B", "C")
print(list(product(letters, range(3))))
print(list(permutations(letters)))
