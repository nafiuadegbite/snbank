import os
import json
from random import randint


def open_account():
    account_data = []
    with open("staff.txt","r") as file_obj:
            staff_details = json.load(file_obj)
    print("\nPlease enter your login details")
    while True:
        username = input("\nEnter your username: ")
        password = input("\nEnter your password: ")
        if (username != (staff_details['Staff 1']['Username']) or password != (staff_details['Staff 1']['Password'])) and (username != (staff_details['Staff 2']['Username']) or password != (staff_details['Staff 2']['Password'])):
            print("\n Wrong credentials")
        else:
            print("\nLogin Successful")
            while True:
                staff_response = int(input("\n1. Create new bank account \n2. Check account details \n3. Logout \n"))
                if staff_response == 1:
                    account_name = input("\nAccount Name: ")
                    opening_balance = int(input("\nOpening Balance: "))
                    account_type = input("\nAccount Type: ")
                    account_email = input("\nAcoount Email: ")
                    account_number = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
                    print("\nAccount Successfully Created \nThe Account Number is: "+account_number)
                    account_details = {"Account Name": account_name, "Opening Balance": opening_balance, "Account Type": account_type, "Account Email": account_email, "Account Number":account_number}
                    specific_account_details = {account_number:account_details}
                    account_data.append(specific_account_details)
                    if os.stat("customer.txt").st_size == 0:
                        with open("customer.txt", "w") as file_obj:
                            json.dump(account_data, file_obj)
                    else:
                        with open("customer.txt") as file_obj:
                            account_data = json.load(file_obj)
                            account_data.append(specific_account_details)
                        with open("customer.txt", "w") as file_obj:
                            json.dump(account_data, file_obj)
                elif staff_response == 2:
                    # check_account["Account Number"] = account_request
                    with open("customer.txt") as file_obj:
                        data = json.load(file_obj)
                    for user_data in data:
                        for user_data_key in user_data.keys():
                            account_request = input("\nPlease provide the account number: ")
                            if account_request in user_data_key:
                                for key, value in user_data[account_request].items():
                                    print(key, ":", value)
                            else:
                                print("\nAccount Not Found")
                        break
                elif staff_response == 3:
                    print("\n Logging out...")
                    break
            break
            

user_input = "\nWelcome, please enter: \n 1. Staff Login \n 2. Close App \n"
while True:
    try:
        user_response = int(input(user_input))
        if user_response == 1:
            open_account()
        elif user_response == 2:
            print("Closing App..")
            break
        else:
            print("Please Choose a number between 1 and 2")
    except ValueError:
            print("Please Choose a number between 1 and 2")