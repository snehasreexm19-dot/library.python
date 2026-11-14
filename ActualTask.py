"""ActualTask.py - function definitions for the Monthly Savings Analyzer."""


def _validate_number(value, name):
    """Helper: make sure a value is a non-negative number."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value < 0:
        raise ValueError(f"{name} cannot be negative")


def calculate_savings(income, expenses):
    """Return monthly savings = income - total expenses.

    expenses can be a dict {"Rent": 8000, ...} or a list [8000, 2000, ...].
    """
    _validate_number(income, "Income")

    # Dictionaries -> use their values; lists/tuples -> use as they are
    amounts = expenses.values() if isinstance(expenses, dict) else expenses

    total_expenses = 0
    for amount in amounts:          # loop adds up every expense
        _validate_number(amount, "Expense")
        total_expenses += amount

    return income - total_expenses  # negative result means overspending


def savings_rate(income, savings):
    """Return savings as a percentage of income."""
    _validate_number(income, "Income")
    if income == 0:
        raise ValueError("Income must be greater than zero to find savings rate")
    return (savings / income) * 100


def target_progress(current_savings, target):
    """Return (percentage_completed, amount_remaining) toward a savings target."""
    _validate_number(current_savings, "Current savings")
    _validate_number(target, "Target")
    if target == 0:
        raise ValueError("Target must be greater than zero")

    percentage = min((current_savings / target) * 100, 100)  # cap at 100%
    remaining = max(target - current_savings, 0)             # never below 0
    return percentage, remaining


def months_to_target(remaining, monthly_savings):
    """Return the number of whole months needed to reach the remaining amount."""
    _validate_number(remaining, "Remaining amount")
    if monthly_savings <= 0:
        raise ValueError("Monthly savings must be positive to reach a target")

    months = 0
    while remaining > 0:            # keep saving month by month
        remaining -= monthly_savings
        months += 1
    return months
