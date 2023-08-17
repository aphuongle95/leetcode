# You are given an array of three non-negative integers, each less than 256.

# Your task is to pack these integers into one number M so that the first element of the array occupies the first (or least significant) 8 bits of M; the second element occupies next 8 bits, and so on.

# Return the obtained integer M as unsigned integer.


def array_packing(integers: list[int]) -> int:
    packed_bits_str: str = ""
    for i in integers:
      sanity_check(i)
      b = convert_to_bits(i)
      packed_bits_str = str(b) + packed_bits_str
    print("combined number: ", packed_bits_str)
    result = int(packed_bits_str, 2)
    print("final number: ", result)
    return result

def sanity_check(i: int):
    """Check if the given integer is within range"""
    if i<0 or i>256:
        raise ValueError
    return
  
def fill_bits(b: str, n: int=8) -> str:
    """Fill the missing most important bits with zero.
    Args:
      b: the original bit string
      n: number of bits for output bit
    Returns:
      str: the bit string filled with 0 for the left most bits, 
    Examples:
      >>> print(fill_bits("11000"))
      00011000
    """
    r = "0"*(8-len(b)) + b
    return r
  
def convert_to_bits(n: int, b: int = 2, number_bits: int = 8) -> str:
    """Convert an integer into a binary number with certain number of bits
    Args:
      n: the orginal integer
      b: the base, can be any positive integer, e.g. 2, 8, 10
      number_bits: number of bits for the expected outputs, if missing, fill with zeros
    Returns:
      str: the converted bit string
    Examples:
      >>> print(convert_to_bits(24))
      00011000
    """
    print("integer number: ", n)
    r = ""
    while n:
      r = str(int(n%b)) + r
      n //= b
    r = fill_bits(r, n = number_bits)
    print("binary number: ", r)
    return r