from datetime import datetime

# Western zodiac date ranges
ZODIAC_DATES = {
    "Aries":       ((3, 21), (4, 19)),
    "Taurus":      ((4, 20), (5, 20)),
    "Gemini":      ((5, 21), (6, 20)),
    "Cancer":      ((6, 21), (7, 22)),
    "Leo":         ((7, 23), (8, 22)),
    "Virgo":       ((8, 23), (9, 22)),
    "Libra":       ((9, 23), (10, 22)),
    "Scorpio":     ((10, 23), (11, 21)),
    "Sagittarius": ((11, 22), (12, 21)),
    "Capricorn":   ((12, 22), (1, 19)),
    "Aquarius":    ((1, 20), (2, 18)),
    "Pisces":      ((2, 19), (3, 20)),
}

def get_zodiac(birth_date: str) -> str:
    """
    Given a birth_date in 'YYYY-MM-DD', return the zodiac sign.
    """
    try:
        dt = datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("birth_date must be in YYYY-MM-DD format")

    month, day = dt.month, dt.day

    for sign, ((start_m, start_d), (end_m, end_d)) in ZODIAC_DATES.items():
        # Normal range (e.g. Leo: 7/23–8/22)
        if (month == start_m and day >= start_d) or \
           (month == end_m and day <= end_d):
            return sign
        # Capricorn case (crosses Dec–Jan)
        if sign == "Capricorn" and (
            (month == 12 and day >= 22) or (month == 1 and day <= 19)
        ):
            return sign

    return "Unknown"