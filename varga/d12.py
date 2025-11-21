# varga/d12.py

# ----------------------------------------
# D12 (Dwadasamsa) - Parashara System
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


def get_amsha_index_12(degree: float) -> int:
    """
    Return D12 amsha index (0~11) using 2.5° segmentation.
    """
    idx = int(degree // 2.5)
    return min(idx, 11)


def calc_d12(sign: str, degree: float):
    """
    Calculate D12 (Dwadasamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D12 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_12(degree)

    target = wrap_rasi(base + idx)
    return NUM_TO_SIGN[target]
