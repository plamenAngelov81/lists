nums = input().split(" ")
count = int(input())

copy_nums = list(map(int, nums))

for i in range(count):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(", ".join(nums))
