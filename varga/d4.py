# varga/d4.py

# ----------------------------------------
# D4 (Chaturthamsa / Turyamsa) - Parashara System
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


def get_amsha_index_4(degree: float) -> int:
    """Return 0~3 for 7.5° divisions."""
    if 0 <= degree < 7.5:
        return 0
    elif 7.5 <= degree < 15:
        return 1
    elif 15 <= degree < 22.5:
        return 2
    else:
        return 3


def calc_d4(sign: str, degree: float):
    """
    Calculate D4 (Chaturthamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D4 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_4(degree)

    # odd sign (↑ increasing)
    if base % 2 == 1:
        target = wrap_rasi(base + idx)

    # even sign (reverse direction)
    else:
        target = wrap_rasi(base + (4 - idx))

    return NUM_TO_SIGN[target]
