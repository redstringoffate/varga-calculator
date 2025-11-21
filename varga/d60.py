# varga/d60.py

# ----------------------------------------
# D60 (Shashtiamsa) - Parashara System
# ----------------------------------------

SIGN_TO_NUM = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
    "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
    "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
}

NUM_TO_SIGN = {v: k for k, v in SIGN_TO_NUM.items()}


def wrap_rasi(num: int) -> int:
    """Wrap to 1~12."""
    return ((num - 1) % 12) + 1


def get_amsha_index_60(degree: float) -> int:
    """
    Return D60 amsha index (0~59) using 0.5° segmentation.
    """
    idx = int(degree // 0.5)
    return min(idx, 59)


def calc_d60(sign: str, degree: float):
    """
    Calculate D60 (Shashtiamsa) based on Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi (e.g. "Taurus", "Leo")
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D60 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_60(degree)

    # Odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign → reverse
    else:
        target = wrap_rasi(base + (59 - idx))

    return NUM_TO_SIGN[target]
