# There are N students in a class. Their heights are known.
# It is required to put stools of different heights under each student (except for the tallest ones) so that their heads are on the same level.
# You need to calculate the summary height of all the stools used. For example,
# if there are four students with heights 150, 160, 180, 175, we will need to put a stool of height 30 under the first student,
# 20 under the second, no stool under the third, and a stool of height 5 under the last one.
# The summary height of the stools is 55.

heights = list(map(int, input().split()))

max_height = max(heights)

sum_of_heights = 0

for i in heights:
    sum_of_heights += max_height - i

print(sum_of_heights)