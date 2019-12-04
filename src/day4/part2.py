#!/usr/bin/env python3

# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# the two adjacent matching digits are not part of a larger group of matching digits.
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# 1407 is too low


def password_cracker(password_from, password_to):
    possible_passwords = []
    for possible_password in range(password_from, password_to+1):
        prev = ''
        adjacent_digits = False
        decrease = False
        counter = 0
        for digit in str(possible_password):
            if digit == prev:
                counter += 1
            else:
                if counter == 1:
                    adjacent_digits = True
                counter = 0
            if prev != '' and int(digit) < int(prev):
                decrease = True
                break
            prev = digit
        if not decrease and (counter == 1 or adjacent_digits):
            possible_passwords.append(possible_password)
    return len(possible_passwords)


if __name__ == '__main__':
    print(str(password_cracker(108457, 562041)))
