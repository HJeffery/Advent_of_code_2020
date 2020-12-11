"""
Task:
To identify seat locations on the plane
"""
import math


def file_to_list(filename: str):
    data = []
    with open(filename, 'r') as infile:
        for line in infile:
            data.append(line.strip("\n"))
    return data


def get_region(half: str, start: int, end: int):
    if half == "F" or half == "L":
        new_end = math.floor(((end - start) / 2) + start)
        region = (start, new_end)
    elif half == "B" or half == "R":
        new_start = math.ceil(((end - start) / 2) + start)
        region = (new_start, end)
    return region


def calculate_seat_id(column, row):
    seat_id = (column * 8) + row
    return seat_id


boarding_passes = file_to_list("day5_boarding_pass.txt")

seat_ids = []
seats_taken = {}

for item in boarding_passes:
    col_start = 0
    col_end = 127
    row_start = 0
    row_end = 7
    for i in item:
        if i == "F" or i == "B":
            (col_start, col_end) = get_region(i, col_start, col_end)
        if i == "L" or i == "R":
            (row_start, row_end) = get_region(i, row_start, row_end)
    if col_start in seats_taken.keys():
        seats_taken[col_start].append(row_start)
    else:
        seats_taken[col_start] = [row_start]
    unique_seat_id = calculate_seat_id(col_start, row_start)
    seat_ids.append(unique_seat_id)

print(f"Highest seat ID = {max(seat_ids)}")
print(seats_taken)
for i in range(0, 128):
    if i - 1 not in seats_taken.keys():
        continue
    elif i + 1 not in seats_taken.keys():
        continue
    elif len(seats_taken[i]) != 8:
        column = i
        print(i, seats_taken[i])
        for j in range(0, 8):
            if j not in seats_taken[i]:
                row = j

missing_seat_id = calculate_seat_id(column, row)

print(f"Empty seat is at column {column} and row {row} with seat id "
      f"{missing_seat_id}")
