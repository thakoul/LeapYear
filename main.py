from functions import check_another_year, check_if_leap

# handles the main while loop for the application
check_again = True

# executes for one time when the application starts
check_if_leap()

while check_again:
    # if check_another_year returns false the program stops executing
    check_again = check_another_year()
