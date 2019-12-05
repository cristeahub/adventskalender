def tick(sheep, drag_size, foodless_days):
    x = sheep - drag_size
    if x >= 0:
        drag_size += 1
        foodless_days = 0
    else:
        foodless_days += 1
        drag_size -= 1

    return (x if x > 0 else 0, drag_size, foodless_days)

with open('sau.txt') as f:
    a = map(int, f.read().split(','))

foodless_days, drag_size, sheep, num_days = 0, 50, 0, 0

for i, x in enumerate(a):
    sheep, drag_size, foodless_days = tick(sheep + x, drag_size, foodless_days)
    if foodless_days == 5:
        num_days = i
        break

print(num_days if num_days > 0 else len(a))
