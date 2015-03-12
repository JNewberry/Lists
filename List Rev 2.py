#John Newberry
#
#List Rev 2
name_list = []
order = 0
for count in range(6):
    order + 1
    name = input("Please input a name: ")
    name_list.append(name)
print(name_list)
while 1:
    print("Please input the names you wish to view")
    view = int(input("From: "))
    end_view = int(input("To: "))
    print(name_list[view:end_view])

