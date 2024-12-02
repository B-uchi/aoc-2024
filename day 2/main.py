def first_half(report):
    index = 0
    difference = 0
    isSafe = True
    
    while index < len(report)-1:
        if index == 0:
            if 1 <= abs(report[index] - report[index+1]) <= 3 and report[index] != report[index+1]:
                difference = report[index] - report[index+1]
                index += 1
            else:
                isSafe = False
                break
        else:
            new_difference = report[index] - report[index+1]
            if new_difference == 0:
                isSafe = False
                break
            if (difference < 0 and new_difference > 0) or (difference > 0 and new_difference < 0):
                isSafe = False
                break
            if not 1 <= abs(new_difference) <= 3:
                isSafe = False
                break
            index += 1
                
    if isSafe:
        return True
    return False

def second_half(report):
    for remove_index in range(len(report)):
        modified_report = report[:remove_index] + report[remove_index+1:]
        index = 0
        difference = 0
        
        while index < len(modified_report) - 1:
            if index == 0:
                if 1 <= abs(modified_report[index] - modified_report[index+1]) <= 3 and modified_report[index] != modified_report[index+1]:
                    difference = modified_report[index] - modified_report[index+1]
                    index += 1
                else:
                    break
            else:
                new_difference = modified_report[index] - modified_report[index+1]
                if new_difference == 0:
                    break
                if (difference < 0 and new_difference > 0) or (difference > 0 and new_difference < 0):
                    break
                if not 1 <= abs(new_difference) <= 3:
                    break
                index += 1
        
        if index == len(modified_report) - 1:
            return True
    
    return False

reports = []
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
        levels = []
        for level in line.split(" "):
            levels.append(int(level))
        reports.append(levels)
        
safe_reports = sum(1 for report in reports if first_half(report))
safe_reports_with_dampener = sum(1 for report in reports if second_half(report))

print(safe_reports_with_dampener)
            
            
    