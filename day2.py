"""
Task:
Find the number of valid passwords
"""


def file_to_list(filename: str):
    data = []
    with open(filename, 'r') as infile:
        for line in infile:
            data.append(line.strip("\n"))
    return data


def check_password_validity(passwords: list):
    valid_passwords = 0
    for password in passwords:
        requirements = password.split(":")[0]
        code = password.split(":")[1]
        code = code.strip(" ")
        requirements = requirements.split(" ")
        lower = int(requirements[0].split("-")[0])
        upper = int(requirements[0].split("-")[1])
        character = requirements[1]
        char_count = 0
        for i in code:
            if i == character:
                char_count += 1
        if lower <= char_count <= upper:
            valid_passwords += 1
    return valid_passwords


def check_new_password_validity(passwords: list):
    new_valid_passwords = 0
    for password in passwords:
        requirements = password.split(":")[0]
        code = password.split(":")[1]
        code = code.strip(" ")
        requirements = requirements.split(" ")
        first = int(requirements[0].split("-")[0])
        second = int(requirements[0].split("-")[1])
        character = requirements[1]
        # Only want one condition to be True
        if (code[first - 1] == character) != (code[second - 1] == character):
            new_valid_passwords += 1
    return new_valid_passwords


data_list = file_to_list("day2_passwords.txt")
valid = check_password_validity(data_list)
print(f"There are {valid} valid passwords according to the original method")
new_valid = check_new_password_validity(data_list)
print(f"There are {new_valid} valid passwords according to the new method")
