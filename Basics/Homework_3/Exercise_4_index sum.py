# You are given two sequences. The first is a sequence A of N real numbers (N > 0),
# the other is a sequence of indices IND of size M (all the elements of the second sequence are nonnegative integers strictly less than N).
# Output the sum of elements of A with indices from IND. For example, if А = {1,2,3,4,5} аnd IND = {0 3 3 2}, you must calculate the sum A[0]+A[3]+A[3]+A[2] = 1 + 4 + 4 + 3 = 12.
# The first line of input contains real numbers. The second line contains nonnegative integers.

numbers_list = list(map(float, input().split()))
index_list = list(map(int, input().split()))

sum_of_numbers = 0
for i in index_list:
    sum_of_numbers += numbers_list[i]

print(sum_of_numbers)