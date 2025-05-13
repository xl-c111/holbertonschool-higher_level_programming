#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        roman_dict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total_value = 0
        prev_value = 0

        for char in reversed(roman_string):
            current_value = roman_dict.get(char, 0)
            if current_value < prev_value:
                total_value -= current_value
            else:
                total_value += current_value
                prev_value = current_value
        return total_value
