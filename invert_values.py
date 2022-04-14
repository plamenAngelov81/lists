numbers = input().split()

changed_list = []

for i in numbers:
    if int(i) > 0:
        changed_list.append(-int(i))
    else:
        changed_list.append(abs(int(i)))

print(changed_list)