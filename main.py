from motorcycle_shop import calculate_monthly_payment, calculate_total_payment

def calculate_monthly_payment(price, down_payment):
    remaining_balance = price - down_payment
    monthly_interest_rate = 0.05 / 12
    num_payments = 12
    monthly_payment = remaining_balance * (monthly_interest_rate * (1 + monthly_interest_rate)**num_payments) / ((1 + monthly_interest_rate)**num_payments - 1)
    return monthly_payment

print(f"Monthly payment: {monthly_payment}")
print(f"Total payment: {total_payment}")