#John Newberry
#19/1/2015
#Q2 part g

import random

def simulate_die_throw():
    number = [1,2,3,4,5,6]
    frequency = [0,0,0,0,0,0]
    for count in range(20):
        roll = random.randint(1,6)
        for count3 in range(6):
            if roll == number[count3]:
                frequency[count3] = frequency[count3]+1
    return frequency

def print_results(frequency):
    print("Score  Frequency")
    for count in range(6):
        print("{0:3} {1:9}".format(count+1,frequency[count]))

frequency = simulate_die_throw()
print_results(frequency)
