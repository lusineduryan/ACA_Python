# The root of a number is
#  - the sum of its digit if it(the sum) is less than 10
#  - the root of the sum of its digits otherwise.
# Let’s consider 78996. The sum of its digits is 39. Since it’s not less than 10, we have to find the root of 39.
# The sum of its digits is 12. Still not less than 10, so repeating again, we add the digits again and get 3, which is finally less than 10.
# So the root of 78996 is 3. Given a natural number N, find its root, outputting intermediary results in the process.

input_number = input()
int_number = int(input_number)
digits_coll = map(int, input_number)
sum = 0

while int_number > 10:
    sum += sum(digits_coll)
    print(input_number)
    input_number = sum