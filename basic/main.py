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


def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a:
    :param b:
    :return:
    """
    calculated_average = (a + b) / 2
    return calculated_average


def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:
    :param cost:
    :return:
    """
    if balance >= cost:
        return True
    else:
        return False


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text:
    :param times:
    :return:
    """
    calculated_repeat_text = text * times
    return calculated_repeat_text


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence:
    :param word:
    :return:
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost:
    :param percent:
    :return:
    """
    calculated_cost_tip = cost * (percent / 100)
    return calculated_cost_tip


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name:
    :param last_name:
    :return:
    """
    calculated_intials = first_name[0].upper() + last_name[0].upper()
    return calculated_intials


def percent_score(points: float, possible: float) -> float:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points:
    :param possible:
    :return:
    """
    if possible < 1:
        return None
    calculated_percent = (points / possible) * 100
    return calculated_percent


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number:
    :param minimum:
    :param maximum:
    :return:
    """
    if minimum <= number <= maximum:
        return True
    else:
        return False


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a:
    :param b:
    :param c:
    :return:
    """
    if a != b and b != c and a!= c:
        return True
    else:
        return False


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.

    :param a:
    :param b:
    :param c:
    :return:
    """
    calculated_average = (a + b + c) / 3
    return calculated_average


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature:
    :param cold_limit:
    :param hot_limit:
    :return:
    """
    if temperature < cold_limit:
        return "It's cold."
    if temperature > hot_limit:
        return "It's hot."
    else:
        return "It's just right."

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    print("Is the number 10 even?", is_even(10))
    print("Count the vowels in 'Hello World':", count_vowels("Hello World"))
    print("What is 25 Celsius in Fahrenheit:", celsius_to_fahrenheit(25))
    print("What is the reverse of 'robot':", reverse_text("robot"))
    print("Which is larger? 10 or 20?", larger_number(10,20))
    print("What is the average of 4 and 6?", average_two(4,6))
    print("Can I afford 50 with 40 balance?", can_afford(40,50))
    print("Can you repeat 'Hi' 5 times?", repeat_text("Hi", 5))
    print("Does 'Computer Science 15 class' have the word 'class'?:", ("Computer Science 15 class", "class"))
    print("Can you calculate the tip?", calculate_tip(20, 10))
    print("What are the initials in this name?", make_initials("Tomi", "Babasola"))
    print("What is my test percentage?", percent_score(28,30))
    print("Is 8 in between 1 and 10?", is_between(8, 1, 10))
    print("What is the average of these numbers? 10, 25, 50", average_three(10,25,50))
    print("What is the temperature?", describe_temperature(25, 10, 55))

