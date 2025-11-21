# utils/sign.py

# ----------------------------------------
# Sign definitions and utilities
# ----------------------------------------

# 12 Signs in order (Aries → Pisces)
SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Sign → Number (1~12)
SIGN_TO_NUM = {name: i+1 for i, name in enumerate(SIGNS)}

# Number → Sign
NUM_TO_SIGN = {i+1: name for i, name in enumerate(SIGNS)}

# Unicode symbols (AstroSeek 스타일 오마쥬)
SIGN_SYMBOL = {
    "Aries":       "♈",
    "Taurus":      "♉",
    "Gemini":      "♊",
    "Cancer":      "♋",
    "Leo":         "♌",
    "Virgo":       "♍",
    "Libra":       "♎",
    "Scorpio":     "♏",
    "Sagittarius": "♐",
    "Capricorn":   "♑",
    "Aquarius":    "♒",
    "Pisces":      "♓",
}

def get_sign_symbol(sign: str) -> str:
    """Return unicode symbol for sign."""
    return SIGN_SYMBOL.get(sign, "?")


def num_to_symbol(num: int) -> str:
    """From sign number → symbol."""
    name = NUM_TO_SIGN[num]
    return SIGN_SYMBOL[name]
