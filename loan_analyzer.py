# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

# Calculations for the loan portfolio summaries.
    # Number of loans in the list.
    # Total amount of all loans.
    # Average loan price.
"""                                 

loan_costs = [500, 600, 200, 1000, 450]


total_number_of_loans = len(loan_costs)
print(total_number_of_loans)

total_of_all_loans = sum(loan_costs)
print(total_of_all_loans)

average_loan_price = total_of_all_loans / total_number_of_loans
print(average_loan_price)



"""Part 2: Analyze Loan Data.
"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract Future Value and Remnaining Months on loan. 

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"Future value will be ${future_value}")
print(f"Remaining months on the loan: {remaining_months}")

discount_rate = 20/100
pv = future_value / (1 + discount_rate/12) ** remaining_months
print(f"The present value for this loan is: ${pv: .2f}")

# Comparison of loan investment. 

fair_value = pv

if fair_value >= loan.get("loan_price"):
    print("Buy it! Loan is worth at least the cost to invest!")
else:
    print("Too expensive! Don't do it, it's not worth the price!")



"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions for a new loan.

"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def new_loan_pv():
    fv = new_loan["future_value"]
    rm = new_loan["remaining_months"]
    annual_discount_rate = 0.2
    present_value = fv / (1 + (annual_discount_rate / 12)) ** rm
    return present_value

new_loan_pv()

print(f"The present value of the loan is:", new_loan_pv())



"""Part 4: Conditionally filter lists of loans.

# Loop to iterate loans, selecting only inexpensive loans into new list. 

"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = []
for loan in loans:
    loan_price= loan["loan_price"]
    if loan_price <= 500:
        inexpensive_loans.append(loan)

print("List of inexpensive loans:", inexpensive_loans)



"""Part 5: Save the results."""


output_path = Path("inexpensive_loans.csv")


header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
# save csvpath
with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(header)
        for loan in inexpensive_loans:
            csvwriter.writerow(loan.values())