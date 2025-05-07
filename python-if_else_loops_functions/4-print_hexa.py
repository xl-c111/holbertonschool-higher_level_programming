#!/usr/bin/python3
# in range(n) already give numbers in decimal
for i in range(0, 99):
    # f"{i:x}" converts decimal into lowercase hexadecimal
    # f"{i:X}" converts decimal into uppercase hexadecimal
    # f"{i:#x}" converts decimal into a lowercase hexadecimal with 0x prefix
    # f"{i:#X}" converts decimal into a uppercase hexadecimal with 0x prefix
    # f"{i:02x}" converts decimal into a lowercase hexadecimal, zero-padded 2 digits
    print("{} = {:#x}".format(i, i))
