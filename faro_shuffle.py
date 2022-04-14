cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)

for i in range(0, shuffle):
    shuffle_list = []
    for p in range(0, mid):
        shuffle_list.append(cards[p])
        shuffle_list.append(cards[mid])
        mid += 1
    cards = shuffle_list
    mid = int(length / 2)
print(cards)
