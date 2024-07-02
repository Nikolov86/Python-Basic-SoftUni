deposit = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())


accrued_interest = deposit * annual_interest_rate / 100
monthly_interest = accrued_interest / 12
total_deposit_period = deposit + term_of_the_deposit * monthly_interest


print(f"{total_deposit_period} lv.")
