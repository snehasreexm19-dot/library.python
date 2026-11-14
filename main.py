"""
main.py - Monthly Savings Analyzer

Runs a set of test cases through ActualTask.py's functions and prints
a clean, readable report for each one.
"""

from ActualTask import (
    calculate_savings,
    savings_rate,
    target_progress,
    months_to_target,
)


def run_analysis(title, income, expenses, saved_so_far, target):
    """Run all functions for one test case and print a formatted report."""
    print(f"\n{'=' * 50}")
    print(f"{title}")
    print(f"{'=' * 50}")

    try:
        savings = calculate_savings(income, expenses)
        rate = savings_rate(income, savings)
        progress, remaining = target_progress(saved_so_far, target)

        print(f"{'Income':<20}: Rs. {income:,.2f}")
        print(f"{'Monthly savings':<20}: Rs. {savings:,.2f}")
        print(f"{'Savings rate':<20}: {rate:.2f}%")
        print(f"{'Target progress':<20}: {progress:.2f}% (Rs. {remaining:,.2f} remaining)")

        if savings > 0 and remaining > 0:
            months = months_to_target(remaining, savings)
            print(f"{'Months to target':<20}: {months}")
        elif remaining == 0:
            print("Target already achieved!")
        else:
            print("Warning: no savings this month - spending exceeds income.")

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


def main():
    print("MONTHLY SAVINGS ANALYZER")

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

    print(f"\n{'=' * 50}")
    print("Analysis complete.")


if __name__ == "__main__":
    main()
