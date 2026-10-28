def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number:
    :return:
    """
    if number / 2 == 0:
        return True
    else:
        return False



def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.


    :param text:
    :return:
    """
    count = 0
    for char in "aeiou":
            count += 1
    calculated_vowels = count
    return calculated_vowels


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius:
    :return:
    """
    calculated_temperature = (9.0/5.0 * celsius + 32) + 32
    return calculated_temperature


def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text:
    :return:
    """
    calculated_text = text[::-1]
    return calculated_text


def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a:
    :param b:
    :return:
    """
    if a > b:
        return a
    else:
        return b


def average_two(a, b):
    """Calculate and return the average of two integers.

    :param a:
    :param b:
    :return:
    """
    pass


def can_afford(balance, cost):
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:
    :param cost:
    :return:
    """
    pass


def repeat_text(text, times):
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text:
    :param times:
    :return:
    """
    pass


def contains_word(sentence, word):
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence:
    :param word:
    :return:
    """
    pass


def calculate_tip(cost, percent):
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost:
    :param percent:
    :return:
    """
    pass


def make_initials(first_name, last_name):
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name:
    :param last_name:
    :return:
    """
    pass


def percent_score(points, possible):
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points:
    :param possible:
    :return:
    """
    pass


def is_between(number, minimum, maximum):
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number:
    :param minimum:
    :param maximum:
    :return:
    """
    pass


def all_different(a, b, c):
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a:
    :param b:
    :param c:
    :return:
    """
    pass


def average_three(a, b, c):
    """Calculate and return the average of three integers.

    :param a:
    :param b:
    :param c:
    :return:
    """
    pass


def describe_temperature(temperature, cold_limit, hot_limit):
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature:
    :param cold_limit:
    :param hot_limit:
    :return:
    """
    pass

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    pass

