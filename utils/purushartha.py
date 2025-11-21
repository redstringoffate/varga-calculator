from utils.nakshatra_purushartha import NAKSHATRA_PURUSHARTHA

PADA_PURUSHARTHA = {
    1: ("Dharma", "D"),
    2: ("Artha",  "A"),
    3: ("Kama",   "K"),
    4: ("Moksha", "M")
}

def get_purushartha(nk_name, nk_pada):
    # 1) Nakshatra-level Purushartha
    nk_p = NAKSHATRA_PURUSHARTHA[nk_name]

    # 2) Pada-level Purushartha code only
    _, code = PADA_PURUSHARTHA[nk_pada]

    # 3) Combine
    return f"{nk_p}-{code}"
