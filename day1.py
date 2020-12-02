"""
Task:
Find the two numbers in a list that sum to 2020 and multiply them together
"""

def file_to_list(filename):
    data_list = []
    with open(filename, 'r') as infile:
        for line in infile:
            data_list.append(line.strip("\n"))
    for counter, i in enumerate(data_list):
        data_list[counter] = int(i)
    return data_list

def sum_and_multiply_2(expenses_list):
    for i in expenses_list:
        if 2020 - i in expenses_list:
            multiplied_total = i * (2020 - i)
    return multiplied_total

def sum_and_multiply_3(expenses_list):
    for counter, i in enumerate(expenses_list):
        remainder = 2020 - i
        for j in expenses_list[counter:]:
            for k in expenses_list[counter:]:
                if j + k == remainder:
                    multiplied_total = i * j * k
    return multiplied_total

data_list = file_to_list("expenses_report.txt")
multiplied_total = sum_and_multiply_2(data_list)
print(f'Answer to part a: {multiplied_total}')
multiplied_total_3 = sum_and_multiply_3(data_list)
print(f'Answer to part b: {multiplied_total_3}')