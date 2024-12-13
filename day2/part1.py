def is_safe_report(report):
    """
    Determines if a report is safe according to the given rules.

    Parameters:
        report (list of int): A list of levels in the report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are within the range [-3, -1] or [1, 3]
    if all(-3 <= diff <= -1 for diff in differences):
        return True  # All levels are strictly decreasing by 1, 2, or 3.
    elif all(1 <= diff <= 3 for diff in differences):
        return True  # All levels are strictly increasing by 1, 2, or 3.

    return False

'''
# Method 2 - more manual but still valid, does not use 'all' method
def is_safe_report(report):
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]

    all_decreasing = True
    all_increasing = True
    for diff in differences:
        if not -3 <= diff <= -1:
            all_decreasing = False
        if not 1 <= diff <= 3:
            all_increasing = False

    if all_increasing:
        return True

    if all_decreasing:
        return True

    return False
'''

def count_safe_reports(lines):
    """
    Counts the number of safe reports in the given data.

    Parameters:
        data (list of str): List of reports, each as a space-separated string of numbers.

    Returns:
        int: The number of safe reports.
    """
    safe_count = 0
    for line in lines:
        report = list(map(int, line.split()))
        if is_safe_report(report):
            safe_count += 1

    return safe_count

with open('input.txt','r') as file:
    lines = file.readlines()

output = count_safe_reports(lines)

print(output)