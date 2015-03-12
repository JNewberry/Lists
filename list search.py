#John Newberry
#12/01/2015

def linear_search(search_list, search_item):
    found = False
    index = 0
    while not found:
        if search_item == search_list[index]:
            found = True
        else:
            index = index + 1
    return found

search_list = ["one", "two", "three", "four", "five", "six"]
search_item = "five"
found = linear_search(search_list, search_item)
if found == True:
    print("Found")
else:
    print("Not found")
