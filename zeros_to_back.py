numbers = input().split(", ")
numbers = [int(i) for i in numbers]

end_zero_list = []
zero_list = []

for i in numbers:
    if i != 0:
        end_zero_list.append(i)
    else:
        zero_list.append(i)


end_zero_list.extend(zero_list)

print(end_zero_list)
