highest_score = 0
result_f = open("results.txt")
for each_thing in result_f:
    (name, score) = each_thing.split()
    scoreproper = float(score)
    if (scoreproper > highest_score):
        highest_score = scoreproper
result_f.close()
print("The highest score was:")
print(highest_score)
print("Congratulations!")

