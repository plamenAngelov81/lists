numbers = input().split(" ")
string = input()
string_list = list(string)
message = []
string_len = len(string)
for i in numbers:
    sum_digit = 0
    for j in i:
        sum_digit += int(j)
    if sum_digit > len(string):
        index = sum_digit - len(string)
        message.append(string[index])
        string_list.pop(index)
        string = "".join(string_list)
    else:
        message.append(string[sum_digit])
        string_list.pop(sum_digit)
        string = "".join(string_list)
# for k in message:
#   print(k, end="")

print("".join(message))

