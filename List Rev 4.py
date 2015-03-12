#John Newberry
#25/12/2014
#lists rev4

Student = []
DoB = []

for count in range(5):
    Student.append(input("Please enter the name of a student: "))
    DoB.append(input("Please enter His/Her date of birth: "))
while(1):
    search = input("Please enter the name of the student you are looking for: ")
    for count in range(5):
        if search == Student[count]:
            selection = Student[count]
            selected_DoB = DoB[count]
            YoB = selected_DoB[-4:]
            
            print(selection)
            print(YoB)
        else:
            print("The name you entered is invalid")
    
