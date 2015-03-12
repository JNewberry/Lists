#John Newberry
#13/01/2015
#lists stretch and challenge 3
timetable = [[p1,p2,p3,p4],
             [p1,p2,p3,p4],
             [p1,p2,p3,p4],
             [p1,p2,p3,p4],
             [p1,p2,p3,p4],
             ]
week = ["monday","teusday","wednesday","thursday","friday"]
for count in range(5):
    for index in range(4):
        input("what lesson did you have on {0} period {1}".format(week[count], timetable[count][index]))
