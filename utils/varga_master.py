# utils/varga_master.py

# ----------------------------------------
# Master Varga Calculator (Parashara System)
# ----------------------------------------

from utils.sign import SIGN_TO_NUM, NUM_TO_SIGN
from utils.house import house_number

# import all Varga calculation functions
from varga.d2 import calc_d2
from varga.d3 import calc_d3
from varga.d4 import calc_d4
from varga.d6 import calc_d6
from varga.d7 import calc_d7
from varga.d8 import calc_d8
from varga.d9 import calc_d9
from varga.d10 import calc_d10
from varga.d12 import calc_d12
from varga.d16 import calc_d16
from varga.d20 import calc_d20
from varga.d24 import calc_d24
from varga.d30 import calc_d30
from varga.d60 import calc_d60


# varga registry (for iteration)
VARGA_MAP = {
    "D1": None,      # handled separately
    "D2": calc_d2,
    "D3": calc_d3,
    "D4": calc_d4,
    "D6": calc_d6,
    "D7": calc_d7,
    "D8": calc_d8,
    "D9": calc_d9,
    "D10": calc_d10,
    "D12": calc_d12,
    "D16": calc_d16,
    "D20": calc_d20,
    "D24": calc_d24,
    "D30": calc_d30,
    "D60": calc_d60,
}


def compute_vargas(planets: dict):
    """
    Compute all Varga charts (D1, D2, ... D60).

    Parameters
    ----------
    planets : dict
        {
           "ASC": ("Cancer", 13.00),
           "Sun": ("Taurus", 17.25),
           ...
        }

    Returns
    -------
    dict
        {
           "D1": {"ASC": {"sign":..., "house":...}, "Sun": {...}, ...},
           "D2": {...},
           ...
        }
    """

    results = {}

    # -------------------------
    # D1 is direct input
    # -------------------------
    results["D1"] = {}
    lagna_sign = planets["ASC"][0]

    for label, (sign, deg) in planets.items():
        house = house_number(sign, lagna_sign)
        results["D1"][label] = {
            "sign": sign,
            "degree": deg,
            "house": house,
        }

    # -------------------------
    # All other Vargas
    # -------------------------
    for dn, func in VARGA_MAP.items():
        if dn == "D1":
            continue

        results[dn] = {}

        # ASC first
        asc_sign, asc_deg = planets["ASC"]
        asc_varga_sign = func(asc_sign, asc_deg)
        results[dn]["ASC"] = {
            "sign": asc_varga_sign,
            "degree": asc_deg,
            "house": 1,   # ASC always 1st house
        }

        # All planets
        for label, (sign, deg) in planets.items():
            if label == "ASC":
                continue

            varga_sign = func(sign, deg)
            lagna_sign = asc_varga_sign

            house = house_number(varga_sign, lagna_sign)

            results[dn][label] = {
                "sign": varga_sign,
                "degree": deg,
                "house": house,
            }

    return results
