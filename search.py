num = int(input())
word = input()

list_words = []

for i in range(1 , num + 1):
    current_string = input()
    list_words.append(current_string)

search_list = []

for y in list_words:
    if word in y:
        search_list.append(y)

print(list_words)
print(search_list)
