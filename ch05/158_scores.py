scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[float(score)] = name
result_f.close()

print("The top scores were:")
for lol in sorted(scores.keys(), reverse = True):
    print('Surfer ' + scores[lol] + ' scored ' , lol)
          
      
