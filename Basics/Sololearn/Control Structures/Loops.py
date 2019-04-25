i = 1
while i < 5:
    print(i)
    i += 1

print("The end")

i = 1
while i < 5:
    print(i)
    i += 1
    if i == 4:
        print("Breaking")
        break

print("The end")

i = 1
while i < 5:
    print(i)
    i += 1
    if i == 4:
        print("Skipping")
        continue

print("The end")