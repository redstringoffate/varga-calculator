# varga/d24.py

# ----------------------------------------
# D24 (Chaturvimshamsa) - Parashara System
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


def get_amsha_index_24(degree: float) -> int:
    """
    Return D24 amsha index (0~23) using 1.25° segmentation.
    """
    segment = 30.0 / 24.0  # 1.25°
    idx = int(degree // segment)
    return min(idx, 23)


def calc_d24(sign: str, degree: float):
    """
    Calculate D24 (Chaturvimshamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name
    degree : float
        Longitude within sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D24 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_24(degree)

    # Odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign → reverse
    else:
        target = wrap_rasi(base + (23 - idx))

    return NUM_TO_SIGN[target]
