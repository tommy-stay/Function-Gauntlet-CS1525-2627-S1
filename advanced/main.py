def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """Convert Celsius to Fahrenheit and return True if within safe range limits.

    :param celsius: Temperature in Celsius.
    :param minimum_f: Minimum safe Fahrenheit limit.
    :param maximum_f: Maximum safe Fahrenheit limit.
    :return: True if converted temperature is within limits, False otherwise.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    if minimum_f <= fahrenheit <= maximum_f:
        calculated_safe_range = True
    else:
        calculated_safe_range = False
    return calculated_safe_range

def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """Calculate total cost with tip and return True if balance covers it.

    :param balance: Available balance.
    :param cost: Base cost.
    :param tip_percent: Tip percentage.
    :return: True if affordable, False otherwise.
    """
    tip = cost * (tip_percent / 100)
    total = cost + tip
    if balance >= total:
        calculated_tip = True
    else:
        calculated_tip = False
    return calculated_tip

def meets_average(score1: float, score2: float, score3: float, required_average: float) -> bool:
    """Calculate three-score average and compare with required average.

    :param score1: First score.
    :param score2: Second score.
    :param score3: Third score.
    :param required_average: Minimum required average.
    :return: True if average meets requirement, False otherwise.
    """
    avg = (score1 + score2 + score3) / 3
    if avg >= required_average:
        calculated_average = True
    else:
        calculated_average = False
    return calculated_average

def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """Determine name initials and check if they match expected initials case-insensitively.

    :param first_name: First name string.
    :param last_name: Last name string.
    :param expected_initials: Expected initials string.
    :return: True if they match, False otherwise.
    """
    actual = (first_name[0] + last_name[0]).upper()
    if actual == expected_initials.upper():
        calculated_initials = True
    else:
        calculated_initials = False
    return calculated_initials

if __name__ == '__main__':
    print("Is this temperature in the safe range? (25C, 60F, 90F)", temperature_in_safe_range(25, 60, 90))
    