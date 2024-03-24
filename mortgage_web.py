import streamlit as st

def calculate_monthly_payment(purchase_price, down_payment_percent, interest_rate, rent_income, strata_fee, hydro_wifi_bills):
    loan_amount = purchase_price * (1 - down_payment_percent / 100)
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = 30 * 12  # Assuming a 30-year mortgage

    # Monthly payment calculation using the formula for mortgage payment
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    # Subtracting rental income, strata fee, hydro, and wifi bills from monthly payment
    monthly_payment = monthly_payment - rent_income + strata_fee + hydro_wifi_bills

    return monthly_payment

def main():
    st.title("Mortgage Payment Calculator")

    # Input data
    purchase_price = st.number_input("Enter the purchase price of the apartment:", min_value=0.0, step=1000.0)
    down_payment_percent = st.slider("Enter the down payment percentage:", min_value=0, max_value=100, value=20)
    interest_rate = st.number_input("Enter the mortgage interest rate (%):", min_value=0.0, step=0.1)
    rent_income = st.number_input("Enter the monthly rent income:", min_value=0.0, step=100.0)
    strata_fee = st.number_input("Enter the monthly strata fee:", min_value=0.0, step=10.0)
    hydro_wifi_bills = st.number_input("Enter the combined monthly hydro and wifi bills:", min_value=0.0, step=10.0)

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(purchase_price, down_payment_percent, interest_rate, rent_income, strata_fee, hydro_wifi_bills)

    # Display the result
    st.subheader("Monthly Payment:")
    st.write(f"${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
