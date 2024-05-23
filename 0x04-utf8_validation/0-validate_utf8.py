#!/usr/bin/python3
"""utf-8 validation module"""


def validUTF8(data):
    """Determines if a given data is a valid UTF-8 encoding"""
    byte_counter = 0
    # To count the number of bytes in the current UTF-8 character

    for a in data:
        if byte_counter == 0:
            # Check the first byte of a UTF-8 character
            if a >> 5 == 0b110:  # 2-byte character (starts with 110xxxxx)
                byte_counter = 1
            elif a >> 4 == 0b1110:  # 3-byte character (starts with 1110xxxx)
                byte_counter = 2
            elif a >> 3 == 0b11110:  # 4-byte character (starts with 11110xxx)
                byte_counter = 3
            elif a >> 7 == 0b1:
                # Invalid if it starts with 1xxxxxxx (single byte starts by 0)
                return False
        else:
            # Check the subsequent bytes which should be of the form 10xxxxxx
            if a >> 6 != 0b10:
                return False
            byte_counter -= 1

    # If we have processed all bytes, byte_count should be zero
    return byte_counter == 0