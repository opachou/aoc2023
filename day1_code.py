import re

dict_string_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def total_calibration_value_pt1():
    with open("day1_input.txt") as file:
        total_calibration = 0
        for line in file:
            digits_in_line = re.findall(r"[0-9]", line)

            if len(digits_in_line) == 1:
                total_calibration += int(f"{digits_in_line[0]}" * 2)
            if len(digits_in_line) > 1:
                total_calibration += int(f"{digits_in_line[0]}{digits_in_line[-1]}")

    print(f"Result part 1: {total_calibration}")


def total_calibration_value_pt2():
    with open("day1_input.txt") as file:
        total_calibration = 0
        for line in file:
            for string, digit in dict_string_to_digit.items():
                idxs = [i.end() for i in re.finditer(string, line)]

                if len(idxs) > 0:
                    for idx in idxs:
                        line = line[:idx] + digit + line[idx - 1] + line[idx:]

            digits_in_line = re.findall(r"[0-9]", line)

            if len(digits_in_line) == 1:
                total_calibration += int(f"{digits_in_line[0]}" * 2)
            if len(digits_in_line) > 1:
                total_calibration += int(f"{digits_in_line[0]}{digits_in_line[-1]}")

    print(f"Result part 2: {total_calibration}")


total_calibration_value_pt1()
total_calibration_value_pt2()
