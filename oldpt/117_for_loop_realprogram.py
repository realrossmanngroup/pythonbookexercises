highest_score = 0
result_f = open("results.txt")
for line in result_f:
    
    if float(line) > highest_score :
        highest_score = float(line)
result_f.close()
print("The highest score was:")
print(highest_score)
