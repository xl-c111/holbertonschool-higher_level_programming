#!/usr/bin/python3
"""
range(65, 91): generate ints from 65 to 90(ASCII code: "A" -> 65, "Z" -> 90)
map(chr, range(65, 91)): map each int to its corresponding char using chr()
*map(): the asterisk * unpacks the mapped characters so that each char is passed as seperate argument to print()
sep=str()[::]: use an empty string as the separator between print arguments
            str() returns empty string''
            [::] slics the full string until returns ''
            e.g., print("A", "B", "C", sep=str()[::]) equals print("ABC")
"""
print(*map(chr, range(65, 91)), sep=str()[::])
