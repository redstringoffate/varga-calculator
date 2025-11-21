# varga/d2.py

# ----------------------------------------
# D2 (Hora) - Parashara System
# ----------------------------------------

# Sign ↔ Number 매핑
SIGN_TO_NUM = {
    "Aries": 1, "Taurus": 2, "Gemini": 3, "Cancer": 4,
    "Leo": 5, "Virgo": 6, "Libra": 7, "Scorpio": 8,
    "Sagittarius": 9, "Capricorn": 10, "Aquarius": 11, "Pisces": 12
}

NUM_TO_SIGN = {v: k for k, v in SIGN_TO_NUM.items()}

def calc_d2(sign: str, degree: float):
    """
    Calculate D2 (Hora) sign based on Parashara rules.

    Parameters
    ----------
    sign : str
        Rasi name ("Taurus", "Leo", ...)
    degree : float
        Longitude within the sign (0° ~ <30°)

    Returns
    -------
    str
        Resulting D2 (Hora) sign → "Cancer" or "Leo"
    """

    sign_num = SIGN_TO_NUM[sign]

    # even sign
    if sign_num % 2 == 0:
        # 0-15 = Moon Hora → Cancer
        if 0 <= degree < 15:
            return "Cancer"
        else:  # 15-30 = Sun Hora → Leo
            return "Leo"

    # odd sign
    else:
        # 0-15 = Sun Hora → Leo
        if 0 <= degree < 15:
            return "Leo"
        else:  # 15-30 = Moon Hora → Cancer
            return "Cancer"
