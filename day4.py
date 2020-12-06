"""
Task:
To identify valid passports containing the correct fields
"""
import re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def file_to_list(filename: str):
    data = []
    passport = []
    with open(filename, 'r') as infile:
        for line in infile:
            if line == "\n":
                data.append(passport)
                passport = []
            line = line.strip("\n")
            line = line.split(" ")
            for i in line:
                passport.append(i)
        data.append(passport)
    return data

def check_validity(field_list, passport_list):
    valid = 0
    for passport in passport_list:
        invalid = False
        passport_fields = []
        for field in passport:
            field = field.split(":")
            passport_fields.append(field[0])
        for i in field_list:
            if i not in passport_fields:
                invalid = True
                break
        if not invalid:
            valid += 1
    return valid


def check_new_validity(field_list, passport_list):
    valid = 0
    for passport in passport_list:
        invalid = False
        all_fields = []
        for field in passport:
            field = field.split(":")
            all_fields.append(field[0])
            if field[0] == "byr":
                if len(field[1]) != 4:
                    invalid = True
                    break
                if int(field[1]) > 2002 or int(field[1]) < 1920:
                    invalid = True
                    break
            elif field[0] == "iyr":
                if len(field[1]) != 4:
                    invalid = True
                    break
                if int(field[1]) > 2020 or int(field[1]) < 2010:
                    invalid = True
                    break
            elif field[0] == "eyr":
                if len(field[1]) != 4:
                    invalid = True
                    break
                if int(field[1]) > 2030 or int(field[1]) < 2020:
                    invalid = True
                    break
            elif field[0] == "hgt":
                if field[1][-2:] == "cm":
                    if int(field[1][:-2]) > 193 or \
                            int(field[1][:-2]) < 150:
                        invalid = True
                        break
                elif field[1][-2:] == "in":
                    if 76 < int(field[1][:-2]) or \
                            int(field[1][:-2]) < 59:
                        invalid = True
                        break
                else:
                    # Missing inches or cm units
                    invalid = True
                    break
            elif field[0] == "hcl":
                if not re.search(r'#[a-f0-9]{6}', field[1]):
                    invalid = True
                    break
                if len(field[1]) > 7:
                    invalid = True
                    break
            elif field[0] == "ecl":
                if not field[1] in \
                ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    invalid = True
                    break
            elif field[0] == "pid":
                if not re.search(r'\d{9}', field[1]):
                    invalid = True
                    break
                if len(field[1]) > 9:
                    invalid = True
                    break
        for i in field_list:
            if i not in all_fields:
                invalid = True
                break
        if not invalid:
            valid += 1
    return valid


passport_data = file_to_list("day4_passports.txt")
# 202 passports valid with no CID
print(len(passport_data))
valid_passports = check_validity(fields, passport_data)
print(f"There are {valid_passports} valid passports")
new_valid_passports = check_new_validity(fields, passport_data)
print(f"There are {new_valid_passports} new valid passports")
# 137 passports valid with more restrictions