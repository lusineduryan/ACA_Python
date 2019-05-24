# Find the 1st and last members of a collection of 10 given the avergae of 1st and last 9 members.

coll = (2, 3, 4, 5, 6, 7, 8, 9)
avg_1 = 50
avg_2 = 65

sum_1 = 9 * avg_1
sum_2 = 9 * avg_2

sum = sum(coll)

x = sum_2 - sum
y = sum_1 - sum

print(x,y)