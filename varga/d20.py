# varga/d20.py

# ----------------------------------------
# D20 (Vimshamsa) - Parashara System
# ----------------------------------------

SIGN_TO_NUM = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
    "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
    "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
}

NUM_TO_SIGN = {v: k for k, v in SIGN_TO_NUM.items()}


def wrap_rasi(num: int) -> int:
    """Wraps sign number to 1–12."""
    return ((num - 1) % 12) + 1


def get_amsha_index_20(degree: float) -> int:
    """
    Return D20 amsha index (0~19) using 1.5° segmentation.
    """
    segment = 30.0 / 20.0  # 1.5°
    idx = int(degree // segment)
    return min(idx, 19)


def calc_d20(sign: str, degree: float):
    """
    Calculate D20 (Vimshamsa) based on Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name (e.g., "Leo", "Cancer")
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D20 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_20(degree)

    # Odd sign = forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign = reverse pattern
    else:
        # Equivalent to base + (19 - idx)
        target = wrap_rasi(base + (19 - idx))

    return NUM_TO_SIGN[target]
