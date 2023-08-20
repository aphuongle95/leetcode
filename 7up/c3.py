# Overview
# Resistors are electrical components marked with colorful stripes/bands to indicate both their resistance value in ohms and how tight a tolerance that value has. Remembering these bands is tricky, so let's write a function that will take a string identifying the resistor's ohms and return a string containing a resistor's band colors.

# The resistor color codes
# You can see this Wikipedia page for a colorful chart, but the basic resistor color codes are:

# color:	black	brown	red	orange	yellow	green	blue	violet	gray	white
# value:	0	1	2	3	4	5	6	7	8	9
# All resistors have at least three bands, with the first and second bands indicating the first two digits of the ohms value, and the third indicating the power of ten to multiply them by, for example a resistor with a value of 47 ohms, which equals 47 * 10^0 ohms, would have the three bands "yellow violet black".

# Most resistors also have a fourth band indicating tolerance -- in an electronics kit like yours, the tolerance will always be 5%, which is indicated by a gold band. So in your kit, the 47-ohm resistor in the above paragraph would have the four bands "yellow violet black gold".


import re
from typing import Tuple, List
from enum import Enum
import math
import unittest


class WrongFormatException(Exception):
    pass


class ErrorMessage(str, Enum):
    GENERAL = "Please input the resistor value in format `{value} ohms` . "
    TOO_MANY_SPACE = "Input string has too many spaces."
    NOT_ENOUGH_INFORMATION = "Input string is too short."
    WRONG_UNIT = "Unit should be ohms."
    CANT_HANDLE_NUMBER = "We only support value as interger or with abbreviations like k (for thousand) or M (for million) "


class Colors(str, Enum):
    BLACK = "black"
    BROWN = "brown"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    VIOLET = "violet"
    GRAY = "gray"
    WHITE = "white"
    GOLD = "gold"


ColorCodes = [
    Colors.BLACK,
    Colors.BROWN,
    Colors.RED,
    Colors.ORANGE,
    Colors.YELLOW,
    Colors.GREEN,
    Colors.BLUE,
    Colors.VIOLET,
    Colors.GRAY,
    Colors.WHITE,
]


def encode_resistor_colors(ohms_string: str) -> str:
    print("Input Str: ", ohms_string)
    v, u = split_str(ohms_string)
    codes: List[int] = convert_number_to_code(v)
    results: List[str] = []
    for c in codes:
        results.append(ColorCodes[c])
    results.append(Colors.GOLD)
    return " ".join(results)


def convert_number_to_code(v: int) -> List[int]:
    n3 = find_pow(v)
    v = int(v / 10**n3)
    print("Value left: ", v)
    v_str: str = str(v)
    assert len(v_str) == 2
    n1 = int(v_str[0])
    n2 = int(v_str[1])
    r = [n1, n2, n3]
    print("codes: ", r)
    return r


def find_pow(v: int) -> int:
    r = math.floor(math.log10(v)) - 1
    print("Pow value: ", r)
    return r


def get_number_from_str(x: str) -> int:
    if x[-1] == "k":
        x = float(x.replace("k", "")) * 1000
    elif x[-1] == "M":
        x = float(x.replace("M", "")) * 1000000
    return int(x)


def split_str(inp: str) -> Tuple[float, str]:
    strs = inp.split(" ")
    if len(strs) > 2:
        raise WrongFormatException(ErrorMessage.GENERAL + ErrorMessage.TOO_MANY_SPACE)
    if len(strs) < 2:
        raise WrongFormatException(
            ErrorMessage.GENERAL + ErrorMessage.NOT_ENOUGH_INFORMATION
        )
    unit = strs[1]
    if unit != "ohms":
        raise WrongFormatException(ErrorMessage.GENERAL + ErrorMessage.WRONG_UNIT)
    x = strs[0]
    try:
        val: int = get_number_from_str(x)
    except ValueError:
        raise WrongFormatException(
            ErrorMessage.GENERAL + ErrorMessage.CANT_HANDLE_NUMBER
        )
    print("Splitted str: ", (val, unit))
    return (val, unit)

class Test(unittest.TestCase):
    def test_encode_resistor_colors(self):
        self.assertEqual(encode_resistor_colors("10 ohms"), "brown black black gold")
        self.assertEqual(encode_resistor_colors("100 ohms"), "brown black brown gold")
        self.assertEqual(encode_resistor_colors("220 ohms"), "red red brown gold")
        self.assertEqual(encode_resistor_colors("330 ohms"),"orange orange brown gold")
        self.assertEqual(encode_resistor_colors("470 ohms"), "yellow violet brown gold")
        self.assertEqual(encode_resistor_colors("680 ohms"), "blue gray brown gold")
        self.assertEqual(encode_resistor_colors("1k ohms"), "brown black red gold")
        self.assertEqual(encode_resistor_colors("10k ohms"), "brown black orange gold")
        self.assertEqual(encode_resistor_colors("22k ohms"), "red red orange gold")
        self.assertEqual(encode_resistor_colors("47k ohms"), "yellow violet orange gold")
        self.assertEqual(encode_resistor_colors("100k ohms"), "brown black yellow gold")
        self.assertEqual(encode_resistor_colors("330k ohms"), "orange orange yellow gold")
        self.assertEqual(encode_resistor_colors("2M ohms"), "red black green gold")

if __name__ == "__main__":
    unittest.main()