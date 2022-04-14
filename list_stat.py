num = int(input())

positive = []
negative = []

negative_sum = 0

for i in range(1, num + 1):
    integer = int(input())
    if integer >= 0:
        positive.append(integer)
    else:
        negative.append(integer)
        negative_sum += integer

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {negative_sum}")