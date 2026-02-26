Kansas_Players = [
    {'name': "Patrick Mahomes", 'Position': "QB", 'Jersey_Number': "15",},
    {'name': "Travis Kelce", 'Position': "TE", 'Jersey_Number': "87",},
    {'name': "Xavier Worthy", 'Position': "TE", 'Jersey_Number': "1",},
    {'name': "Isiah Pacheco", 'Position': "RB", 'Jersey_Number': "10",},
    {'name': "Chris Jones", 'Position': "DT", 'Jersey_Number': "95",},
    {'name': "Nick Bolton", 'Position': "LB", 'Jersey_Number': "32",},
    {'name': "Harrison Butker", 'Position': "K", 'Jersey_Number': "7",},
    {'name': "Creed Humphrey", 'Position': "C", 'Jersey_Number': "52",},
    {'name': "Marquise Brown", 'Position': "WR", 'Jersey_Number': "5",},
    {'name': "Drue Tranquill", 'Position': "LB", 'Jersey_Number': "23",}
]

for player in Kansas_Players:
    print(player['Position'])

Kansas_Players[2]['Position'] = "RB"
print(Kansas_Players[2])

jerseyNumbers_sum = 0
for player in Kansas_Players:
    jerseyNumbers_sum += int(player['Jersey_Number'])

print(jerseyNumbers_sum)

