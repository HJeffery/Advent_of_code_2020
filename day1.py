"""
Task:
Find the two numbers in a list that sum to 2020 and multiply them together
"""
def sum_and_multiply_2(expenses):
    expenses_list = []
    with open(expenses, 'r') as infile:
        for line in infile:
            expenses_list.append(line.strip("\n"))
    for i in expenses_list:
        if str(2020 - int(i)) in expenses_list:
            multiplied_total = int(i) * int(2020 - int(i))
    return multiplied_total

def sum_and_multiply_3(expenses):
    expenses_list = []
    with open(expenses, 'r') as infile:
        for line in infile:
            expenses_list.append(line.strip("\n"))
    counter = 0
    for i in expenses_list:
        remainder = 2020 - int(i)
        for j in expenses_list[counter:]:
            for k in expenses_list[counter:]:
                if int(j) + int(k) == remainder:
                    multiplied_total = int(i) * int(j) * int(k)
        counter += 1
    return multiplied_total

if __name__ == '__main__':
    multiplied_total = sum_and_multiply_2("expenses_report.txt")
    print(f'Answer to part a: {multiplied_total}')
    multiplied_total_3 = sum_and_multiply_3("expenses_report.txt")
    print(f'Answer to part b: {multiplied_total_3}')