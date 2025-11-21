# varga/d6.py

# ----------------------------------------
# D6 (Shashtamsa) - Parashara System
# ----------------------------------------

SIGN_TO_NUM = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
    "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
    "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
}

NUM_TO_SIGN = {v: k for k, v in SIGN_TO_NUM.items()}


def wrap_rasi(num: int) -> int:
    """Wrap sign number into 1~12."""
    return ((num - 1) % 12) + 1


def get_amsha_index_6(degree: float) -> int:
    """
    Returns the D6 amsha index (0~5) based on 5° segmentation.
    """
    if 0 <= degree < 5:
        return 0
    elif 5 <= degree < 10:
        return 1
    elif 10 <= degree < 15:
        return 2
    elif 15 <= degree < 20:
        return 3
    elif 20 <= degree < 25:
        return 4
    else:
        return 5


def calc_d6(sign: str, degree: float):
    """
    Calculate D6 (Shashtamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D6 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_6(degree)

    # Odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign → reverse
    else:
        target = wrap_rasi(base + (6 - idx))

    return NUM_TO_SIGN[target]
