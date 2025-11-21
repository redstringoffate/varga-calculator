# utils/house.py

# ----------------------------------------
# Whole-Sign House calculation utility
# ----------------------------------------

from utils.sign import SIGN_TO_NUM, NUM_TO_SIGN

def house_number(planet_sign: str, lagna_sign: str) -> int:
    """
    Calculate whole-sign house number for a planet in a varga chart.

    Parameters
    ----------
    planet_sign : str
        e.g., "Taurus"
    lagna_sign : str
        e.g., "Cancer"

    Returns
    -------
    int
        House number (1~12)
    """
    p_num = SIGN_TO_NUM[planet_sign]
    l_num = SIGN_TO_NUM[lagna_sign]

    return ((p_num - l_num) % 12) + 1


def house_number_num(planet_num: int, lagna_num: int) -> int:
    """
    Same as house_number() but works directly with sign numbers.

    Parameters
    ----------
    planet_num : int  (1~12)
    lagna_num : int   (1~12)

    Returns
    -------
    int
        House number (1~12)
    """
    return ((planet_num - lagna_num) % 12) + 1
