# varga/d8.py

# ----------------------------------------
# D8 (Ashtamsa) - Parashara System
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


def get_amsha_index_8(degree: float) -> int:
    """
    Return D8 amsha index (0~7) using 3.75° segmentation.
    """
    segment = 30.0 / 8.0  # 3.75°
    idx = int(degree // segment)
    return min(idx, 7)


def calc_d8(sign: str, degree: float):
    """
    Calculate D8 (Ashtamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D8 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_8(degree)

    # Odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign → backward
    else:
        target = wrap_rasi(base - idx)

    return NUM_TO_SIGN[target]
