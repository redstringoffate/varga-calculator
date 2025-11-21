# varga/d7.py

# ----------------------------------------
# D7 (Saptamsa) - Parashara System
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


def get_amsha_index_7(degree: float) -> int:
    """
    Returns D7 amsha index (0~6).
    Segment ≈ 4.285714° each.
    """
    segment = 30.0 / 7.0  # ≈ 4.285714°
    idx = int(degree // segment)
    return min(idx, 6)  # ensure max 6


def calc_d7(sign: str, degree: float):
    """
    Calculate D7 (Saptamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D7 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_7(degree)

    # odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # even sign → backward
    else:
        target = wrap_rasi(base + (7 - idx))

    return NUM_TO_SIGN[target]
