PADA_PURUSHARTHA = {
    1: ("Dharma", "D"),
    2: ("Artha", "A"),
    3: ("Kama", "K"),
    4: ("Moksha", "M")
}

def get_purushartha(nk_name, nk_pada):
    name, code = PADA_PURUSHARTHA[nk_pada]
    return f"{name}-{code}"
