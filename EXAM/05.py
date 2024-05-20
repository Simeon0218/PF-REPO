max_goals = 0
best_player = ""
hat_trick = False

while True:
    name = input()
    if name == "END":
        break
    goals_count = int(input())

    if goals_count > max_goals:
        best_player = name
        max_goals = goals_count
        if goals_count >= 3:
            hat_trick = True
    if max_goals >= 10:
        break

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
