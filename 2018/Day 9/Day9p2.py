import time
players = 478
player_scores = [0 for x in range(0, players)]
last_marble_value = 71240 * 100
marble_circle = [0]
current_marble = 0
now = time.time()
for marble in range(1, last_marble_value + 1):
    if marble % 71240 == 0:
        print (marble)
    if marble % players != 0:
        player = marble % players
    elif marble % players == 0:
        player = players
    if marble % 23 != 0:
        current_marble += 2
        if current_marble > len(marble_circle):
            current_marble -= len(marble_circle)
        marble_circle.insert(current_marble, marble)
        
    elif marble % 23 == 0:
        current_marble -= 7
        if current_marble < 0:
            current_marble += len(marble_circle)
        player_scores[player - 1] += marble
        player_scores[player - 1] += marble_circle[current_marble]
        del marble_circle[current_marble]
        
print(str(max(player_scores)) + " : " + str(time.time() - now))
#3037741441 : 17691.433662176132