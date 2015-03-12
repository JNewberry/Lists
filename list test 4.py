shopping_list = []
finished = False
list_amount = 0
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list
        list_amount = list_amount + 1

exit1 = False
while exit1 == False:

    for count in range(len(shopping_list)):
        print("item {0} is {1}".format(count, shopping_list[count]))

    edit_value = int(input("Please select an item to edit: "))
    if edit_value == 0:
        exit1 = True
    else:
        new_name = input("Please enter their new name: ")
        shopping_list[edit_value] = new_name
