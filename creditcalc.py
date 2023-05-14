import math
#
# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# # write your code here
# print(f"{loan_principal}\n{first_month}\n{second_month}\n{third_month}\n{final_output}")
# principal = int(input("Enter the loan principal:"))
# choice = input("What do you want to calculate?\ntype m - for number of monthly payments,\ntype p - for the monthly "
#                "payment:")
# if choice == 'm':
#     monthly = int(input("Enter the monthly payment:"))
#     if math.ceil(principal / monthly) < 2:
#         print(f"It will take {math.ceil(principal / monthly)} month to repay the loan")
#     else:
#         print(f"It will take {math.ceil(principal / monthly)} months to repay the loan")
# if choice == 'p':
#     months = int(input("Enter the number of months:"))
#     last_payment = principal - (months - 1) * math.ceil(principal / months)
#     if last_payment < math.ceil(principal / months):
#         print(f"Your monthly payment = {math.ceil(principal / months)} and the last payment = {last_payment}")
#     else:
#         print(f"Your monthly payment = {math.ceil(principal / months)}")
# answer = input("What do you want to calculate?\ntype n for number of monthly payments,\ntype a for annuity monthly "
#                "payment amount,\ntype p for loan principal:")
# if answer == 'n':
#     principal = int(input("Enter the loan principal:"))
#     monthly_payment = int(input("Enter the monthly payment:"))
#     interest = float(input("Enter the loan interest:"))
#     nominal_interest_rate = interest / 1200
#     number_of_months = math.ceil(math.log((
#             monthly_payment / (monthly_payment - nominal_interest_rate * principal)), 1 + nominal_interest_rate ))
#     print(f"It will take {number_of_months//12} years and {number_of_months%12} months to repay this loan!")
# if answer == 'a':
#     principal = int(input("Enter the loan principal:"))
#     periods = int(input("Enter the number of periods:"))
#     interest = float(input("Enter the loan interest:"))
#     nominal_interest_rate = interest / 1200
#     monthly_payments = principal*(nominal_interest_rate*math.pow((1+nominal_interest_rate),periods)/(math.pow((1+nominal_interest_rate),periods)-1))
#     print(f"Your monthly payment = {math.ceil(monthly_payments)}!")
# if answer == 'p':
#     annuity_payment = float(input("Enter the annuity payment:"))
#     periods = int(input("Enter the number of periods:"))
#     interest = float(input("Enter the loan interest:"))
#     nominal_interest_rate = interest / 1200
#     # principals= annuity_payment/((nominal_interest_rate*math.pow((1+nominal_interest_rate),periods))/(nominal_interest_rate*math.pow((1+nominal_interest_rate),periods)-1))
#     principals = annuity_payment/((nominal_interest_rate*math.pow((1+nominal_interest_rate),periods))/(math.pow((1+nominal_interest_rate),periods)-1))
#
#     print(f"Your loan principal = {principals}!")

import argparse
import math
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)

args = parser.parse_args()

t = args.type
principal = args.principal
n = args.periods
if args.interest is not None:
    i = args.interest / 1200
payment = args.payment

if len(sys.argv) < 5:
    print("Incorrect parameters")
    sys.exit()
if len(sys.argv) == 5 and t == "diff":
    if principal < 0 or n < 0 or i < 0:
        print("Incorrect parameters")
        sys.exit()
    else:
        total = 0
        m = 1
        while m < n + 1:
            d = (principal / n) + i * (principal - principal * (m - 1) / n)
            print(f"Month {m}: payment is {math.ceil(d)}")
            total += math.ceil(d)
            m += 1
        print(f"Overpayment = {math.ceil(total - principal)}")
if len(sys.argv) == 5 and t == "annuity" and payment is None:
    if principal < 0 or n < 0 or i < 0:
        print("Incorrect parameters")
        sys.exit()
    else:
        annuity_payments = math.ceil(principal * (i * math.pow((1 + i), n) / (
                math.pow((1 + i), n) - 1)))
        print(f"Your annuity payment = {annuity_payments}!")
        print(f"Overpayment = {math.ceil(annuity_payments * n - principal)}")

if len(sys.argv) == 5 and t == "annuity" and principal is None:
    if n < 0 or i < 0 or payment < 0:
        print("Incorrect parameters")
        sys.exit()
    else:
        p = math.floor(payment / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
        print(f"Your loan principal = {p}!")
        print(f"Overpayment = {math.ceil(payment * n - p)}")

if len(sys.argv) == 5 and t == "annuity" and n is None:
    if principal < 0 or i < 0 or payment < 0:
        print("Incorrect parameters")
        sys.exit()
    else:
        number_of_months = math.ceil(math.log((
                payment / (payment - i * principal)), 1 + i))
        print(f"It will take {number_of_months // 12} years to repay this loan!")
        print(f"Overpayment = {math.ceil(payment * number_of_months - principal)}")
