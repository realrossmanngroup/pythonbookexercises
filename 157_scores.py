scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name
result_f.close()

print("The top scores were:")
for each_score in scores.keys():
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)
          
      
