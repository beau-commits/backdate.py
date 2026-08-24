
def result(concieved_year, concieved_month): # creates result function 
    # outputs the results
    # using f string allows you to display the variables instead of the actual curly braces and string inside
    # ":02d" is used for formatting how concieved_month is displayed. : signals formatting instructions follow "0" makes the padding zero digits instead of spaces "2" tells it to pad until two total digits and "d" tells the program to treat it as an int
    print(f"you were conceived in {concieved_year}/{concieved_month:02d}")

def calc(): # defines the function that takes the data and does the maths to create the result
    # user inputs birth year and it gets stored as a variable 
    birth_year = int(input("Your year of birth (e.g. 2008):  "))
    

    if birth_year > 9999 or birth_year < 1: # checks for invalid year input
        print("error. year must be between 1 and 9999. please try again.")
    else:
        # user imputs birth month and it gets stored as a variable
        birth_month = int(input("Your birth month (e.g. 01 or 06 or 12:  "))

        if birth_month <1 or birth_month > 12:
            print("error: month must be between 1 and 12. please try again.")

        elif birth_month > 9: # if the birth month is more than 9 then the year remains the same, you just remove 9 months. 
            concieved_month = birth_month - 9 # subtracts 9 months (pregnancy) from the birth month creating variable concieved_month
            concieved_year = birth_year # year remains the same because the birth month is more than 9 
            result(concieved_year, concieved_month)

        elif birth_month <= 9: # if the birth month is less than or equal to 9 then the year subtracts by one, you also subtract the 9 months, but add 12 to get the final answer
            concieved_month = birth_month -9 + 12 # subtracts the 9 months of pregnancy and adds 12 months due to subtracting the year
            concieved_year = birth_year - 1 # subtracts one year from the birth year to find the concieved year
            result(concieved_year, concieved_month)

        else:  # if the input is invalid the program prints an error
            print("error please try again")

# explains the program 
def start(): # defines the function that starts the intitial menu
    running = True
    while running:
        ans = input("Work out date of conception? Y/N:  ")
        if ans.lower() == "y":
            calc()
        else:
            running = False
            print("closing program....")
            

start()