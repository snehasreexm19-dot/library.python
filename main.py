from savings_pkg import (
    calculate_savings,
    savings_rate,
    target_progress,
    months_to_target,
)


def run_analysis(title, income, expenses, saved_so_far, target):
    """Run all package functions for one test case and print the results."""
    print(f"\n=== {title} ===")
    try:
        savings = calculate_savings(income, expenses)
        rate = savings_rate(income, savings)
        progress, remaining = target_progress(saved_so_far, target)

        print(f"Income            : Rs. {income}")
        print(f"Monthly savings   : Rs. {savings}")
        print(f"Savings rate      : {rate:.2f}%")
        print(f"Target progress   : {progress:.2f}% (Rs. {remaining} remaining)")

        if savings > 0 and remaining > 0:
            print(f"Months to target  : {months_to_target(remaining, savings)}")
        elif remaining == 0:
            print("Target already achieved!")
        else:
            print("Warning: no savings this month - spending exceeds income.")
    except (ValueError, TypeError) as error:
        print("Error:", error)


# Test 1: normal case (expenses as a dictionary)
expenses = {"Rent": 8000, "Food": 4000, "Transport": 1500, "Others": 2500}
run_analysis("Test 1: Normal case", 25000, expenses, 10000, 50000)

# Test 2: edge case - expenses exceed income (negative savings)
run_analysis("Test 2: Edge case (overspending)", 15000, [10000, 7000], 5000, 20000)

# Test 3: edge case - target already reached
run_analysis("Test 3: Edge case (target reached)", 30000, [12000, 6000], 60000, 50000)

# Test 4: invalid input - negative income
run_analysis("Test 4: Invalid input (negative income)", -5000, [1000], 0, 10000)

# Test 5: invalid input - zero income
run_analysis("Test 5: Invalid input (zero income)", 0, [], 0, 10000)
