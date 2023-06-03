text_file = open("input.txt", "r")
contents = text_file.read()
cal_list =contents.split('\n') 
cur_total = 0
high_score = 0
for cal in cal_list:
    if cal != '':
        cur_total = cur_total + int(cal)
    if cal == '':
        if cur_total > high_score:
            high_score = cur_total
            print("New High Score ",high_score)
            cur_total = 0
        elif cur_total < high_score:
            print("THE HIGH SCORE STANDS ", high_score)
            cur_total = 0
        elif cur_total == high_score:
            print("HIGH SCORE HAS BEEN MATCHED")
            cur_total=0

print("THIS IS THE HIGH SCORE: ",high_score)

        
        
text_file.close()

