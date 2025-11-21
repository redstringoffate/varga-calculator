# varga/d3.py

# ----------------------------------------
# D3 (Drekkana) - Parashara System
# ----------------------------------------

SIGN_TO_NUM = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
    "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
    "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
}

NUM_TO_SIGN = {v: k for k, v in SIGN_TO_NUM.items()}


def wrap_rasi(num: int) -> int:
    """Wrap sign number into 1~12."""
    if num < 1:
        num = 12 + (num % 12)
    return ((num - 1) % 12) + 1


def calc_d3(sign: str, degree: float):
    """
    Calculate D3 (Drekkana) based on Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D3 sign
    """

    base = SIGN_TO_NUM[sign]

    # 0°–10° → same sign
    if 0 <= degree < 10:
        return sign

    # 10°–20° → 5th from base ( = base + 4 )
    elif 10 <= degree < 20:
        target = wrap_rasi(base + 4)
        return NUM_TO_SIGN[target]

    # 20°–30° → 9th from base ( = base + 8 )
    else:
        target = wrap_rasi(base + 8)
        return NUM_TO_SIGN[target]
