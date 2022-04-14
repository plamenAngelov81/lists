easter_gifts = input().split(" ")

order = input().split(" ")

while order[0] != "No":
    if order[0] == "OutOfStock":
        easter_gifts = ["None" if i == order[1] else i for i in easter_gifts]

    elif order[0] == "Required":
        if int(order[2]) <= len(easter_gifts) - 1:
            easter_gifts.pop(int(order[2]))
            easter_gifts.insert(int(order[2]), order[1])

    elif order[0] == "JustInCase":
        easter_gifts.pop()
        easter_gifts.append(order[1])

    order = input().split(" ")

while 'None' in easter_gifts:
    easter_gifts.remove('None')

print(" ".join(easter_gifts))
