def is_safe_report(report):
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]

    all_decreasing = True
    all_increasing = True
    for diff in differences:
        if not -3 <= diff <= -1:
            all_decreasing = False
        if not 1 <= diff <= 3:
            all_increasing = False

    if all_increasing | all_decreasing:
        return True

    return False

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True

    # Try removing each level one at a time and check if the report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True

    return False

def count_safe_reports(lines):
    safe_count = 0
    for line in lines:
        report = list(map(int, line.split()))
        if is_safe_with_dampener(report):
            safe_count += 1

    return safe_count

with open('input.txt','r') as file:
    lines = file.readlines()

output = count_safe_reports(lines)

print(output)
