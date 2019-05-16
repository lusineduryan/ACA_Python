a = ",".join(["Lucy", "Duryan"])
print(a, type(a))

b = "Lucy Duryan".replace("Lucy", "Gor")
print(b, type(b))

c = "Lucy Duryan".startswith("K")
print(c, type(c))

d = "Lucy Duryan".endswith("yan")
print(d, type(d))

e = "lucy".upper()
print(e)

f = "DURYAN".lower()
print(f)

g = "Lucy,Duryan".split(",")
print(g)

print(max([1, 2, 3, 5]))
print(min([1, 2, 3, 5]))
print(abs(-15))
print(sum([1, 1, 1]))

nums = [55, 44, 33, 22, 11]
print(all([i > 5 for i in nums]))
print(any([i % 2 == 0 for i in nums]))
for i in enumerate(nums):
    print(i)