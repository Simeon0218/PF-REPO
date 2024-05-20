from math import ceil
total_days = int(input())
first_day_km = float(input())

sum_km = 0

first_increase = int(input()) / 100

sum_km += (first_increase * first_day_km) + first_day_km
total = first_day_km + sum_km

for _ in range(total_days - 1):
    increase = int(input()) / 100
    sum_km += (sum_km * increase)
    total += sum_km
    continue

if total < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {abs(ceil(1000 - total))} more kilometers")
else:
    print(f"You've done a great job running {ceil(total - 1000)} more kilometers!")
