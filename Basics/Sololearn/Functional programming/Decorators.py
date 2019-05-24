def decor(func):
    def wrap():
        print("=" * 10)
        func()
        print("=" * 10)
    return wrap

def print_asterix():
    print("*" * 15)

decorated = decor(print_asterix)
print_asterix = decorated

print_asterix()



