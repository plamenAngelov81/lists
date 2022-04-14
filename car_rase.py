time_needed = input().split()

final_line = int((len(time_needed) / 2))

time_num = list(map(int, time_needed))
index_car_2 = len(time_num)
car1 = time_num
car_1_time = 0
car_2_time = 0
counter_0 = 0
for i in range(final_line):

    car_1_time += car1[i]
    if car1[i] == 0:
        car_1_time = car_1_time - car_1_time * 0.2

for j in range(final_line):
    car_2_time += time_num[index_car_2 - 1]
    index_car_2 -= 1
    if car1[j] == 0:
        car_2_time = car_2_time - car_2_time * 0.2

if car_1_time < car_2_time:
    print(f"The winner is left with total time: {car_1_time:.1f}")
elif car_1_time > car_2_time:
    print(f"The winner is right with total time: {car_2_time:.1f}")
