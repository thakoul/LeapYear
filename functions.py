def enter_year():
    # initialize a boolean that handles the while loop
    not_number = True

    while not_number:
        # asks the user which year he wants to check
        year = input("Which year do you want to check?: ")
        if not year.isnumeric():
            # checks if input is not a number and prints a message
            print("Year must be a number")
        else:
            # changes the boolean value to false so that it stops from executing and then stores
            # the year variable as an integer, and finally it returns it.
            not_number = False
            year = int(year)
            return year


def check_another_year():
    # initialize a boolean that handles the while loop
    valid_input = True
    # asks the user if he wants to check for another year
    answer = input("Would you like to check another year, Yes or No: ")

    while valid_input:
        if answer == "Yes" or answer == "yes":
            # if the answer is positive it executes the check_if_leap function,
            # changes the boolean value of valid_input to false and returns
            # a True value to be used in main.py while loop
            check_if_leap()
            valid_input = False
            return True
        elif answer == "No" or answer == "no":
            # if the answer is negative it changes the boolean
            # value of valid_input to false so that this while loop will stop
            # and returns a False value to be used in main.py while loop
            valid_input = False
            return False
        else:
            answer = input("Please choose between Yes and No: ")


def check_if_leap():
    year = enter_year()
    if year % 4 == 0:
        if year % 100 == 0:
            # if year % 4 = 0 and year % 100 = 0 and year % 400 = 0
            # then year is a leap year
            if year % 400 == 0:
                print(f"{year} is a leap year")
            # if year % 4 = 0 and year % 100 = 0 but year % 400
            # is not equal to 0 then the year is not a leap year
            else:
                print(f"{year} is not a leap year.")
        # if year % 4 = 0 but year % 100 is not equal to zero
        # then the year is a leap year.
        else:
            print(f"{year} is a leap year.")
    # if year % 0 isn't equal to zero then the year isn't a leap year
    else:
        print(f"{year} is not a leap year.")
