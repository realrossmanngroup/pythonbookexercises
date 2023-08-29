highest_score = 0
scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name
    if float(score) > highest_score :
        highest_score = float(score)
result_f.close()
sorted(scores.keys())
for score in sorted(scores.keys(), reverse=True):
    print("Surfer " + scores[score] + " scored " + score)
