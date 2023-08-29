highest_score = 0
scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[float(score)] = name
result_f.close()

print("The top scores were: ")

for each in scores.keys():
    print("The athlete named" + scores[each] + " scored a score of " + each)
