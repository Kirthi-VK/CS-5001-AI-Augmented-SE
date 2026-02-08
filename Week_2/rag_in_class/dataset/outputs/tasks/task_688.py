import cmath

def len_complex(a, b):
    """Calculate the length (magnitude) of a complex number formed from a and b."""
    cn = complex(a, b)
    length = abs(cn)
    return length
