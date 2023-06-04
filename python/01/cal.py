text_file = open("input.txt", "r")
contents = text_file.read()
cal_list =contents.split('\n') 
cur_total = 0
high_scores = [0,0,0]

for cal in cal_list:
    if cal != '':
        cur_total = cur_total + int(cal)
    elif cal == '':
        for i in range(len(high_scores)):
            if cur_total > high_scores[i]:
                high_scores[i] = cur_total
                break
            

        cur_total = 0

print("Hight Scores: ",high_scores)
print("Top 3 Total: ", sum(high_scores))

        
        
text_file.close()

