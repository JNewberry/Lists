#John Newberry
#19/1/2015
#Q1 part d
scores = [18,23,36,21,58,40,45,59]

Max = 8
for count1 in range(Max-1):
    for count2 in range(Max-1):
        if scores[count2] > scores[count2 + 1]:
            temp = scores[count2]
            scores[count2] = scores[count2 + 1]
            scores[count2 + 1] = temp

for count in range(len(scores)):
    print("{0}. {1}".format(count +1,scores[count]))
    
