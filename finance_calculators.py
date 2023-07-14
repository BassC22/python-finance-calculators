import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print()
choice = input("Enter either 'investment' or 'bond' from the menu to proceed: ")

# found .casefold() method on Stack Overflow, ensures upper/lower case inputs match required case
# user input is float rather than integer to allow for decimal amounts


if choice.casefold() == "investment":
    deposit_amount = float(input("Please enter the amount of money you are depositing (in Pounds): "))
    interest_rate = float(input("Please enter the interest rate (as a percentage): "))
    years = float(input("How many years do you plan on investing for? "))
    interest = input("What kind of interest would you like? Please enter either 'simple' or 'compound': ")

    # r=interest_rate/100, P=deposit_amount, t=years A=total_amount
    
    if interest.casefold() == "simple":
        total_amount = deposit_amount*(1 + (interest_rate/100)*years)
        print("You will receive £{:.2f}".format(total_amount) + " after " + str(years) + " years")     #used java2blog.com to find a way to format to 2 decimal places

    elif interest.casefold() == "compound":
        total_amount = deposit_amount*math.pow((1 +(interest_rate/100)),years)
        print("You will receive £{:.2f}".format(total_amount) + " after " + str(years) + " years")
    
    else:
        print("Please enter either 'simple' or 'compound' to continue")


elif choice.casefold() == "bond":
    house_value = float(input ("Please enter the current value of the house (in Pounds): "))
    interest_rate = float(input("Please enter the interest rate (as a percentage): "))
    months = float(input("How many months do you plan on taking to repay the bond? "))

    #calculate the monthly interest rate from the interest_rate rate to simplify the main calculation:

    monthly_interest_rate = (interest_rate/100)/12

    #continue with the rest of the formula with the monthly interest rate:
    # P=house_value, i=monthly_interest_rate, n=months

    monthly_repayment = (monthly_interest_rate*house_value)/(1 - (1 + monthly_interest_rate)**(-months))

    print("Your monthly repayment will be £{:.2f}".format(monthly_repayment))


else:
    print("Please enter either 'investment' or 'bond' to continue")
