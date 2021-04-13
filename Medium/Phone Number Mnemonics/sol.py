key_pad = {
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': ['0']
}


def phoneNumberMnemonics(phoneNumber):
    return phone_number_mnemonics_util("", phoneNumber)

# T.C: O(4^n * n), n = length of the telephone number, 4 & n is the breadth & depth of recursion
# S.C: O(4^n * n), since maximum permutaion can be 4 for a number(keypad 7 & 8)
def phone_number_mnemonics_util(starting_numbers, remaning_numbers):
    global key_pad
    if not remaning_numbers:
        return [starting_numbers]
    _ = []
    for number in key_pad[remaning_numbers[0]]:
        _ += phone_number_mnemonics_util(starting_numbers + number, remaning_numbers[1:])
    return _

# T.C: O(4^n * n)
# S.C: O(4^n * n)
def phoneNumberMnemonics(phoneNumber):
    global key_pad, memoization
    if len(phoneNumber) == 1:
        return key_pad[phoneNumber[0]]
    if phoneNumber in memoization:
        return phoneNumber[memoization]
    _ = []
    sub_memonics = phoneNumberMnemonics(phoneNumber[1:])
    memoization[phoneNumber[1:]] = sub_memonics
    for number in key_pad[phoneNumber[0]]:
        for sub_memonic in sub_memonics:
            _.append(number + sub_memonic)
    return _

