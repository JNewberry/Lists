#John Newberry
#12/01/2015

def bubble_sort(unsorted_list):
    sort = False
    while sort == False:
        sort = True
        for count in range(len(unsorted_list)-1):
            if unsorted_list[count] > unsorted_list[count+1]:
                temp = unsorted_list[count+1]
                unsorted_list[count+1] = unsorted_list[count]
                unsorted_list[count] = temp
                sort = False


unsorted_list = ["a", "c", "b","z","a","c","y","b","c"]
bubble_sort(unsorted_list)
print(unsorted_list)
