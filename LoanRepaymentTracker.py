from matplotlib import pyplot as plt


def get_loan_info():
    """Collect loan details from the user."""
    loan = {}
    while True:
        try:
            loan['principal'] = float(input("Enter the loan amount: "))
            loan['rate'] = float(input("Enter the annual interest rate (in %): ")) / 100
            loan['monthlyPayment'] = float(input("Enter your monthly payment amount: "))
            loan['moneyPaid'] = 0
            if loan['principal'] <= 0 or loan['rate'] < 0 or loan['monthlyPayment'] <= 0:
                print("Please enter positive values for all fields.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    return loan


def show_loan_info(loan, month_number):
    """Display the current status of the loan."""
    print(f"\n--- Loan Information after {month_number} months ---")
    for key, value in loan.items():
        print(f"{key.title().replace('_', ' ')}: {value:.2f}" if isinstance(value, float) else f"{key.title().replace('_', ' ')}: {value}")


def collect_interest(loan):
    """Update the loan principal to include monthly interest."""
    loan['principal'] += loan['principal'] * loan['rate'] / 12


def make_monthly_payment(loan):
    """Simulate making a monthly payment."""
    loan['principal'] -= loan['monthlyPayment']
    if loan['principal'] > 0:
        loan['moneyPaid'] += loan['monthlyPayment']
    else:
        loan['moneyPaid'] += loan['monthlyPayment'] + loan['principal']
        loan['principal'] = 0


def summarize_loan(loan, months, initial_principal):
    """Display the summary of loan payments."""
    print(f"\n🎉 Congratulations! You paid off your loan in {months} months ({months / 12:.2f} years).")
    print(f"Initial loan amount: ${initial_principal:.2f}")
    print(f"Annual interest rate: {loan['rate'] * 100:.2f}%")
    print(f"Monthly payment: ${loan['monthlyPayment']:.2f}")
    print(f"Total paid: ${loan['moneyPaid']:.2f}")
    interest_paid = loan['moneyPaid'] - initial_principal
    print(f"Total interest paid: ${interest_paid:.2f}")


def create_loan_graph(data, loan):
    """Plot the principal balance over time."""
    months, principals = zip(*data)  # Unpack month and principal data
    plt.plot(months, principals, marker='o', label='Principal Remaining')
    plt.title(f"Loan Repayment at {loan['rate'] * 100:.2f}% Interest")
    plt.xlabel("Month Number")
    plt.ylabel("Remaining Principal")
    plt.grid(True)
    plt.legend()
    plt.show()


# Main Application Logic
def main():
    print("\n🎉 Welcome to the Loan Calculator App 🎉\n")
    month_number = 0
    loan = get_loan_info()
    initial_principal = loan['principal']
    data_to_plot = []

    show_loan_info(loan, month_number)
    input("\nPress Enter to start the repayment simulation...\n")

    while loan['principal'] > 0:
        if loan['principal'] > initial_principal:
            print("\nWarning: Your payments are too small to cover the interest!")
            print("Consider increasing your monthly payment or reducing your interest rate.")
            break

        month_number += 1
        collect_interest(loan)
        make_monthly_payment(loan)
        data_to_plot.append((month_number, loan['principal']))
        show_loan_info(loan, month_number)

        if loan['principal'] == 0:
            summarize_loan(loan, month_number, initial_principal)
            create_loan_graph(data_to_plot, loan)
            break


if __name__ == "__main__":
    main()
