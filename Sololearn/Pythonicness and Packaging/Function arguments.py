def func(named_arg, *args):
    print(named_arg)
    print(args)

func(1,2,3,4,5)

def func1(x,y,food = 'spam'):
    print(food)

func1(1,2)
func1(3,4,'egg')

def func2(x, y = 7, *args, **kwargs):
    print(kwargs)

func2(2,3,4,5,6, a = 7, b = 8)