width = int(raw_input("Width?"))
height = int(raw_input("Height?"))
print '*' * width

for i in range(height-2):
    x = width - 2
    spaces = x * " "
    row = "*" + spaces + "*"

    print row

print '*' * width
