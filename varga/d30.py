# varga/d30.py

# ----------------------------------------
# D30 (Trimsamsa) - Parashara System
# ----------------------------------------

SIGN_TO_NUM = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
    "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
    "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
}

NUM_TO_SIGN = {v: k for k, v in SIGN_TO_NUM.items()}

# Male signs: 1,3,5,7,9,11
MALE_SIGNS = {1, 3, 5, 7, 9, 11}

# Trimsamsa mappings (Parashara)
D30_MALE = [
    "Aries",       # 0°–6°
    "Gemini",      # 6°–12°
    "Leo",         # 12°–18°
    "Sagittarius", # 18°–24°
    "Aquarius"     # 24°–30°
]

D30_FEMALE = [
    "Taurus",      # 0°–6°
    "Virgo",       # 6°–12°
    "Capricorn",   # 12°–18°
    "Pisces",      # 18°–24°
    "Scorpio"      # 24°–30°
]


def get_amsha_index_30(degree: float) -> int:
    """
    30° divided by 5 segments → 6° each.
    Returns index 0~4.
    """
    idx = int(degree // 6)
    return min(idx, 4)


def calc_d30(sign: str, degree: float):
    """
    Calculate D30 (Trimsamsa) according to Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name (e.g., "Taurus", "Leo")
    degree : float
        Longitude within the sign (0 <= degree < 30)

    Returns
    -------
    str
        Resulting D30 sign
    """

    base = SIGN_TO_NUM[sign]
    idx = get_amsha_index_30(degree)

    # Male sign
    if base in MALE_SIGNS:
        return D30_MALE[idx]

    # Female sign
    else:
        return D30_FEMALE[idx]
