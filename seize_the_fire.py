type_of_fire = input().split("#")
water = int(input())

effort = 0
total_fire = 0
print("Cells:")

for fire in type_of_fire:
    fire_power = fire.split(" = ")
    size_of_fire = fire_power[0]
    fire_strength = int(fire_power[1])

    if size_of_fire == "High":
        if water >= fire_strength:
            if 81 <= fire_strength <= 125:
                water -= fire_strength
                effort += fire_strength * 0.25
                total_fire += fire_strength
                print(f" - {fire_strength}")

    if size_of_fire == "Medium":
        if water >= fire_strength:

            if 51 <= fire_strength <= 80:
                water -= fire_strength
                effort += fire_strength * 0.25
                total_fire += fire_strength
                print(f" - {fire_strength}")

    if size_of_fire == "Low":
        if water >= fire_strength:
            if 1 <= fire_strength <= 50:
                water -= fire_strength
                effort += fire_strength * 0.25
                total_fire += fire_strength
                print(f" - {fire_strength}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
