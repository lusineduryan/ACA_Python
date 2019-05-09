# human = input()
# root = 77
# while int(human) != 0:
#     a = root ** 5
#     b = str(a)
#     c = int(b[2:5])
#     PC = c % 3 + 1
#     print(PC)
#     human = input()
#     root = c ** 5
# else:
#     root += 1

import datetime

current_time = datetime.datetime.now()
sum_of_time_components = current_time.year + current_time.month + current_time.day + \
                         current_time.hour + current_time.minute + current_time.second + current_time.microsecond


print(sum_of_time_components)
