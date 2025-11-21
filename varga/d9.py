# varga/d9.py

# ----------------------------------------
# D9 (Navamsa) - Parashara System
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


def get_amsha_index_9(degree: float) -> int:
    """
    Return D9 amsha index (0~8) using 3°20' segmentation.
    """
    segment = 30.0 / 9.0   # 3.333333333°
    idx = int(degree // segment)
    return min(idx, 8)


def calc_d9(sign: str, degree: float):
    """
    Calculate D9 (Navamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name (e.g., "Taurus")
    degree : float
        Longitude within sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D9 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_9(degree)

    # Odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign → reversed pattern
    else:
        target = wrap_rasi(base + (8 - idx))

    return NUM_TO_SIGN[target]
