num_set = {1, 2, 3}
word_set = set(["one", "two", "three"])

print(3 in num_set)
print("five" not in word_set)

num_set.add(4)
num_set.remove(3)

print(num_set)

num_set.pop()

print(num_set)

set_one = {1,2,3,4,5,6}
set_two = {4,5,6,7,8,9}

print(set_one | set_two)
print(set_one & set_two)
print(set_one - set_two)
print(set_one ^ set_two)