def avg_sum(arg1, arg2, arg3):
    if arg1 + arg2 + arg3 != 1 and arg1 > 0 and arg2 > 0 and arg3 > 0:
        return "Invalid probabilities"
    else:
        one_dice_avg = 3.5
        return arg1 * one_dice_avg + arg2 * one_dice_avg * 2 + arg3 * one_dice_avg * 3

p1 = 0.33
p2 = 0.33
p3 = 1-0.66
print(avg_sum(p1,p2,p3))