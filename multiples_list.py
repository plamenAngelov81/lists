num = int(input())
counter = int(input())

our_list = []

for i in range(1, counter + 1):
    integer = i * num
    our_list.append(integer)

print(our_list)
