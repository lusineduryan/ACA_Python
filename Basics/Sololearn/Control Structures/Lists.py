words = ["rock", "paper", "scissors"]

print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)

things = ["name", 4.56, words,5]
print(things[2][1])

str = "Hello"
print(str[3])

nums = [7,7,7,7,7]
nums[2] = 5
print(nums)
print(nums + [1,2,3])
print(nums * 3)
print(7 in nums)
print(not 1 in nums)
print(1 not in nums)

nums.append(10)
print(nums)
print(len(nums))
nums.insert(1, 12)
print(nums)
print(nums.index(12))
print(max(nums))
print(min(nums))
print(nums.count(7))
nums.remove(10)
print(nums)
nums.reverse()
print(nums)


