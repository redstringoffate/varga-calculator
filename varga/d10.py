# varga/d10.py

# ----------------------------------------
# D10 (Dasamsa) - Parashara System
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


def get_amsha_index_10(degree: float) -> int:
    """
    Return D10 amsha index (0~9) using 3° segmentation.
    """
    idx = int(degree // 3)
    return min(idx, 9)


def calc_d10(sign: str, degree: float):
    """
    Calculate D10 (Dasamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Leo", "Virgo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D10 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_10(degree)

    # Odd sign → forward
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # Even sign → reversed
    else:
        target = wrap_rasi(base + (9 - idx))

    return NUM_TO_SIGN[target]
