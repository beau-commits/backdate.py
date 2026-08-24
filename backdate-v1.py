# explains the program 
print("let's work out when you were concieved lol")
# user inputs birth year and birth month and they are stored as variables ("birth_year") and (birth_month)
birth_year = int(input("Your year of birth (e.g. 2008):  "))
birth_month = int(input("your birth month (e.g. 01 or 06 or 12:  "))

#logic: if the birth month is less than 9 then the year remains the same, you just remove 9 months. 
# so you create variables (concieved_month) and (concieved_year) and make them the same as birth month and year but subtracting the neccisary values
# if the number is neither higher or smaller than 9 or not a number at all the program spits out a simple error message 
if birth_month >=9:
    concieved_month = birth_month - 9
    concieved_year = birth_year
elif birth_month < 9:
    concieved_month = birth_month -9 + 12
    concieved_year = birth_year - 1 
else:
    print("error please try again")

#outputs the results
print(f"you were conceived in {concieved_year}/{concieved_month:02d}")
