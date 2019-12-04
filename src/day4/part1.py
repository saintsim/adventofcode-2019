#!/usr/bin/env python3


# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

def password_cracker(password_from, password_to):
    possible_passwords = []
    for possible_password in range(password_from, password_to+1):
        prev = ''
        adjacent_digits = False
        decrease = False
        for digit in str(possible_password):
            if digit == prev:
                adjacent_digits = True
            if prev != '' and int(digit) < int(prev):
                decrease = True
                break
            prev = digit
        if not decrease and adjacent_digits:
            possible_passwords.append(possible_password)
    return len(possible_passwords)


if __name__ == '__main__':
    print(str(password_cracker(108457,562041)))
