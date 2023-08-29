highest_score = 0
scores = []
players = []
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores.append(score)
    players.append(name)
    if float(score) > highest_score :
        highest_score = float(score)
result_f.close()
print("The highest score was:")
print(highest_score)
