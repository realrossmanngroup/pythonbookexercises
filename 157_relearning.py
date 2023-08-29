scores = {}
results = open("results.txt")
for entry in results:
    (name, score) = entry.split()
    scores[score] = name
results.close()

for each in scores.keys():
    print('Athlete named ' + scores[each] + ' got ' + each)
