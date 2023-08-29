scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[float(score)] = name

result_f.close()

print("The top scores were:")
for lol in sorted(scores.keys(), reverse = True):
    #print('Surfer ' + scores[lol] + ' scored ' + lol)
    print('Surfer ' + scores[lol] + ' scored ', lol)

print("BS ABOVE, RESULT BELOW!")

print('Surfer ' + scores[9.12] + ' scored 9.12')
      
