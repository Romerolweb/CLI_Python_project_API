#Task 1
#create menu

def display_menu():
    """
    Displays a menu with numbered options.
    """
    print("Help")
    print("====")
    print("The following commands are recognized:")
    print("1. Display help",)
    print("2. Exit the application")



#write function for option exit applicatoin

























#Task 2
#function that: ...



def choose_option(userInput):
    if userInput == 1 or userInput == "help" or userInput ==  "Display help":
        display_menu()
    elif userInput == 2 or userInput == "Exit" or userInput == "Exit the application":
        exit()

'''
Task 2 User Input
Next, write a main() function that displays the help menu and then 
repeatedly prompts the user to input their command.
• The user should be prompted for a command with the 
following: “wildlife> ”
o If the user inputs help, the function should call 
display_menu() 
o If the user enters exit, then the system should exit.

'''
def main():   
    display_menu()

    userInput = input("Enter the option you want to choose: ")
    print(f"The option that you have chosen is, {userInput}!")
    choose_option(userInput)

#write display 2 options
# pass

if __name__ == "__main__":
    main()
















#Task 3
#function that:...





































#Task 4
#function that:...

