card_list = input().split(" ")

out_players = []

players_a = 11
players_b = 11

stop_game = False

for card in card_list:
    if card not in out_players:
        out_players.append(card)
        if "A" in card:
            players_a -= 1
        elif "B" in card:
            players_b -= 1

    if players_a < 7 or players_b < 7:
        stop_game = True
        break

print(f"Team A - {players_a}; Team B - {players_b}")
if stop_game:
    print("Game was terminated")