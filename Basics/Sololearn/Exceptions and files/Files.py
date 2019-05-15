my_file = open("myTextFile.txt", "r")

# open("myTextFile.txt", "w")
# open("myTextFile.txt", "r")
# open("myTextFile.txt", "a")
# open("myTextFile.txt", "wb")
# open("myTextFile.txt", "r+")

cont = my_file.read(4)
cont1 = my_file.read()
print(cont)
print("*********")
print(cont1)
my_file.close()

my_file_1 = open("myTextFile.txt", "r")
print(my_file_1.readlines())
my_file_1.close()

my_file_2 = open("myTextFile.txt", "r")
for i in my_file_2:
    print(i)
my_file_2.close()


new_file = open("newFile.txt", "w")
new_file.write("new content")
new_file.close()

new_file = open("newFile.txt", "r")
print(new_file.read())
new_file.close()