"""
Convert the given number into a roman numeral.
All roman numerals answers should be provided in upper-case.
"""


def convert_to_roman(num):
    if type(num) is int:
        lookup = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        roman_num = ""
        for i in lookup:
            while num >= lookup[i]:
                roman_num += i
                num -= lookup[i]

        return roman_num
    else:
        return "This Number cannot be converted"


print(convert_to_roman(10))
