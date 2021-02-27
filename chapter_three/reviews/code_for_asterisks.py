# input
# for loops
# range
# print

Creating_A_New_File = open("asterisks.pyCharm", "w")
Creating_A_New_File.write("I created this asterisks file \n"
                          "So here is the brief history of this file \n\n"
                          "1: This asterisks code can print stars in form of a right angle triangle\n"
                          "2: This file doesn't have any unit testing because it's not a function\n"
                          "3: This file is a statement without a function,, so it might break If handled carelessly."
                          "\n\n "
                          "Thanks for reading my files.. Hope to see you correct me. ")
Creating_A_New_File.close()
User_To_Enter_An_Asterisks = int(input("Enter asterisks row: "))
for If_The_User_Gives_A_Number_For_A_Row in range(1, User_To_Enter_An_Asterisks + 1):
    for The_Number_Of_Asterisks_In_A_Columns in range(1, If_The_User_Gives_A_Number_For_A_Row + 1):
        print("*", end=" ")
    print ()

User_To_Enter_An_Asterisks = int(input("Enter asterisks row: "))
for If_The_User_Gives_A_Number_For_A_Row in range(1, User_To_Enter_An_Asterisks + 1):
    print("" * 1 + "*" * (1 + User_To_Enter_An_Asterisks - If_The_User_Gives_A_Number_For_A_Row))
