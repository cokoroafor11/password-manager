from config import *
from menu_options import *
from table_options import *

def main():
    '''
    Function to control the flow of password manager
    '''
    while True:
        #Loop to verify correct input
        while True:
            try:
                #Prompt for what user wants to do
                option_prompt = int(input("Welcome to the password manager. What would you like to do? \n \
1: Retrieve password\n \
2: Add password\n \
3: Delete password\n \
4: Update password\n \
5: Generate password\n \
6: View table\n \
7: Create table\n \
8: Delete table\n \
0: Exit\n\n"))
                
                #Check that the value of input is in correct range, otherwise, friendly msg
                if option_prompt >= 0  and option_prompt <= 7:
                    break
                else:
                    print("Please enter proper value. \n")
            #Check for value error (makes sure input is int)
            except ValueError:
                print("Invalid input, please enter a number.\n")

        #Retrieve Password
        if option_prompt == 1:
            #Prompt for username
            username = str(input("What is the username for the account? ").strip())
            #Prompt for app name
            app_name = str(input("Enter app name: ").strip())
            retrieve_pass(username,app_name)
            
            print('\n')

        #Add password
        elif option_prompt == 2:
            #Prompt for inputs
            username = str(input("Enter username: ").strip())
            app_pw = str(input("Enter password: ").strip())
            app_name = str(input("Enter app name: ").strip())
            app_email = str(input("Enter email: ").strip())
            app_website = str(input("Enter website: ").strip())

            #Add record
            add_pass(username,app_pw,app_email,app_name,app_website)


        #Delete Password
        elif option_prompt == 3:
            #Prompt for username and app name
            username = str(input("Enter username: ").strip())
            app_name = str(input("Enter app name: ").strip())

            #Delete record
            delete_pass(username,app_name)

        #Update Password
        elif option_prompt == 4:
            #Prompt for username, account, new password
            username = str(input("Enter username: ").strip())
            app_name = str(input("Enter app name: ").strip())
            new_pass = input('Please enter new password: ')
            update_pass(username,app_name,new_pass)
        
        #Generate password
        elif option_prompt == 5:
            while True:
                try:
                    #Prompt for length
                    length = int(input('Enter password length: '))
                    new_pass = generate_pass(length)
                    print('Your generated password is: {}\n'.format(new_pass))
                    break
                #Check for value error (makes sure input is int)
                except ValueError:
                    print("Invalid input, please enter a number. \n")
            
                

        #View Database
        elif option_prompt == 6:
            #Prompt for sort type and direction
            print('Below are the current records in your database: \n')
            view_database('passwords')

        #Create Database
        elif option_prompt == 7:
            create_table('passwords')
            
        #Delete Database
        elif option_prompt == 8:
            choice = input("Are you sure you want to delete the database? All passwords will be deleted (Y/N)?").strip().lower()
            if choice.startswith('y'):
                delete_table('passwords')
                print("Your database was deleted.")
            else:
                print("Database still intact.")

        #Exit the program
        elif option_prompt == 0:
            break


if __name__ == "__main__":
    main()
