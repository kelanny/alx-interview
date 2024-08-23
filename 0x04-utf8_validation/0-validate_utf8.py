#!usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check if the data set represents a valid UTF-8 encoding."""
    n_bytes = 0

    # Masks to check the significant bits in a byte.
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Count the number of leading 1's.
            while mask & num:
                n_bytes += 1
                mask >>= 1

            # If the number of bytes is 1, it's an ASCII character.
            if n_bytes == 0:
                continue

            # For UTF-8, the number of bytes must be between 2 and 4.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'.
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
