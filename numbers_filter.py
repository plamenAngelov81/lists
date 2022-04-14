num = int(input())

even = []
odd = []
positive = []
negative = []

for i in range(1, num + 1):
    current_integer = int(input())
    if current_integer % 2 == 0:
        even.append(current_integer)
    else:
        odd.append(current_integer)
    if current_integer >= 0:
        positive.append(current_integer)
    else:
        negative.append(current_integer)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)

# Допълнение: функцията eval: reflection - отражение на текст.
# print(eval(command)) - търси стринг който е същият като нашата команда. Демек even, odd,
# positive, negative.
