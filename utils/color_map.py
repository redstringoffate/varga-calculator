# utils/colors.py

"""
Color dictionaries for Varga Excel rendering.

- Element colors     (Main row background)
- Planet colors      (Nakshatra row background via Nakshatra Lord)
- Purushartha colors (Purushartha row font color only)

Colors are hex strings WITHOUT the '#'.
Excel (openpyxl) uses hex strings, e.g. "FF0000".
"""


# ----------------------------------------------------
# HEX → RGB 변환기 (필수)
# ----------------------------------------------------
def hex_to_rgb(hex_str):
    """
    Convert 'A6A6A6' → (166, 166, 166)
    """
    if hex_str is None:
        return None
    hex_str = hex_str.strip().lstrip("#")
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

# utils/color_map.py

SIGN_TO_ELEMENT = {
    "Aries": "Fire",
    "Leo": "Fire",
    "Sagittarius": "Fire",

    "Taurus": "Earth",
    "Virgo": "Earth",
    "Capricorn": "Earth",

    "Gemini": "Air",
    "Libra": "Air",
    "Aquarius": "Air",

    "Cancer": "Water",
    "Scorpio": "Water",
    "Pisces": "Water",
}


# ----------------------------------------
# 4 Elements → Background Colors
# ----------------------------------------

ELEMENT_COLOR = {
    "Fire":   "FFCCCC",   # R255 G204 B204
    "Earth":  "FFFF99",   # R255 G255 B153
    "Air":    "F2F2F2",   # R242 G242 B242
    "Water":  "CCFFFF"    # R204 G255 B255
}


# ----------------------------------------
# Planet Colors (Nakshatra Lord)
# ----------------------------------------

GRAHA_COLOR = {
    "Ketu":     None,        # blank
    "Venus":    "A6A6A6",    # R166 G166 B166
    "Sun":      "FF99CC",    # R255 G153 B204
    "Moon":     "FFCCFF",    # R255 G204 B255
    "Mars":     "FF0000",    # R255 G0 B0
    "Rahu":     "595959",    # R89 G89 B89
    "Jupiter":  "00B050",    # R0 G176 B80
    "Saturn":   "FFFF00",    # R255 G255 B0
    "Mercury":  "00B0F0"     # R0 G176 B240
}


# ----------------------------------------
# Purushartha → Font colors only
# ----------------------------------------

PURUSHARTHA_COLOR = {
    "Dharma": "CC9900",   # Golden-brown
    "Artha":  "008000",   # Deep green
    "Kama":   "CC0033",   # Deep red
    "Moksha": "003399",   # Deep blue
}
