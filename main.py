# Calculate the total expenses
import csv
def total_expenses(file_name: str) -> int:
    """
    Calculate the total expenses
    Args:
        file_name: str
    Returns:
        total_expenses: total expenses
    """
    f = open('data.csv')
    data = csv.reader(f)

    total = 0
    for row in data:
        total += int(row[1][:-1])

    return total