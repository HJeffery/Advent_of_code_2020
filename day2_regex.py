"""
Task:
Find the number of valid passwords
"""

import re


def file_to_list(filename: str):
    data = []
    with open(filename, 'r') as infile:
        for line in infile:
            data.append(line.strip("\n"))
    return data


def check_password_validity(passwords: list):
    valid_passwords = 0
    for password in passwords:
        requirements = re.search(r"\d+-\d+", password)
        lower = int(requirements.group(0).split("-")[0])
        upper = int(requirements.group(0).split("-")[1])
        character = re.search(r"\w", password)
        code = re.search(r"\w+", password)
        char_count = 0
        for i in code.group(0):
            if i == character:
                char_count += 1
        if lower <= char_count <= upper:
            valid_passwords += 1
            print(" ".join(requirements), code.group(0), char_count)
    return valid_passwords


def check_new_password_validity(passwords: list):
    new_valid_passwords = 0
    for password in passwords:
        requirements = re.search(r"\d+-\d+", password)
        first = int(requirements.group(0).split("-")[0])
        second = int(requirements.group(0).split("-")[1])
        character = re.search(r"\w", password)
        code = re.search(r"\w+", password)
        # Only want one condition to be True
        if (code[first - 1] == character) != (code[second - 1] == character):
            new_valid_passwords += 1
            print(" ".join(requirements), code, new_valid_passwords)
    return new_valid_passwords


data_list = file_to_list("day2_passwords.txt")
print(data_list)
print(len(data_list))
valid = check_password_validity(data_list)
print(f"There are {valid} valid passwords according to the original method")
new_valid = check_new_password_validity(data_list)
print(f"There are {new_valid} valid passwords according to the new method")
