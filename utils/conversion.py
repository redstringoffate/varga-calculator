# utils/conversion.py

# ----------------------------------------
# Degree & Minute → Decimal Degree converter
# ----------------------------------------

def to_decimal(degree: float, minute: float) -> float:
    """
    Convert degree + minute to decimal degree.
    
    Parameters
    ----------
    degree : float
        Integer degree (0–29 ideally)
    minute : float
        Integer minute (0–59)

    Returns
    -------
    float
        Decimal degree value
    """
    return degree + (minute / 60.0)


def to_degree_minute(decimal_degree: float):
    """
    Convert decimal degree back to (degree, minute).
    Useful for debugging or re-formatting.

    Parameters
    ----------
    decimal_degree : float

    Returns
    -------
    (int, int)
        degree, minute
    """
    d = int(decimal_degree)
    m = int(round((decimal_degree - d) * 60))
    
    # minute은 60이 될 수 있으므로 보정
    if m == 60:
        d += 1
        m = 0

    return d, m
