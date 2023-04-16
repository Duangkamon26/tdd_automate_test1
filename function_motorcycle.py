def calculate_monthly_payment(price, down_payment):
    num_months = 12
    loan_amount = price - down_payment
    monthly_interest_rate = 0.05 / 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-num_months))
    return monthly_payment

def calculate_down_Payment(price):
    down = 0.2 * (price)
    return down

def validate_price(price):
    if isinstance(price, str) or price <= 0:
        return "Invalid input. Please enter a positive number."
    return price
