from dateutil.relativedelta import relativedelta
from datetime import datetime

MASTER_NUMBERS = [11, 22, 33]
KARMIC_NUMBERS = [13, 14, 16, 19]

full = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
        "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "O": 6, "P": 7, "Q": 8, "R": 9,
        "S": 1, "T": 2, "U": 3, "V": 4, "W": 5, "X": 6, "Y": 7, "Z": 8}

vowels = {"A": 1, "E": 5, "I": 9, "O": 6, "U": 3}

consonants = {"B": 2, "C": 3, "D": 4, "F": 6, "G": 7, "H": 8,
              "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "Q": 8, "R": 9,
              "S": 1, "T": 2, "V": 4, "W": 5, "X": 6, "Y": 7, "Z": 8}

planes_matrix = {
    "E": ("Physical", "Creative"),
    "W": ("Physical", "Vacillating"),
    "D": ("Physical", "Grounded"),
    "M": ("Physical", "Grounded"),
    "A": ("Mental", "Creative"),
    "H": ("Mental", "Vacillating"),
    "J": ("Mental", "Vacillating"),
    "N": ("Mental", "Vacillating"),
    "P": ("Mental", "Vacillating"),
    "G": ("Mental", "Grounded"),
    "L": ("Mental", "Grounded"),
    "I": ("Emotional", "Creative"),
    "O": ("Emotional", "Creative"),
    "R": ("Emotional", "Creative"),
    "Z": ("Emotional", "Creative"),
    "B": ("Emotional", "Vacillating"),
    "S": ("Emotional", "Vacillating"),
    "T": ("Emotional", "Vacillating"),
    "X": ("Emotional", "Vacillating"),
    "K": ("Intuitive", "Creative"),
    "F": ("Intuitive", "Vacillating"),
    "Q": ("Intuitive", "Vacillating"),
    "U": ("Intuitive", "Vacillating"),
    "Y": ("Intuitive", "Vacillating"),
    "C": ("Intuitive", "Grounded"),
    "V": ("Intuitive", "Grounded")
}

result_q_str =  (
                "1 - Life Path\n"
                "2 - Period Cycles\n"
                "3 - Pinnacle Cycles\n"
                "4 - Challenge Numbers\n"
                "5 - Life Path - Birth Day bridge\n"
                "6 - Sun Number\n"
                "7 - Expression Number and Karmic Debt\n"
                "8 - Minor Expression Number\n"
                "9 - Heart's Desire/Soul Urge"
                "10 - Minor Heart's Desire/Soul Urge"
                "11 - Personality\n"
                "12 - Minor Personality\n"
                "13 - Heart's Desire - Personality bridge\n"
                "14 - Life Path - Expression bridge\n"
                "15 - Maturity Number\n"
                "16 - Rational Thought Number\n"
                "17 - Hidden Passion(s)\n"
                "18 - Karmic Lesson(s)\n"
                "19 - Balance Number\n"
                "20 - Cornerstone Letter\n"
                "21 - Subconscious Self Number\n"
                "22 - Physical Plane of Expression\n"
                "23 - Mental Plane of Expression\n"
                "24 - Emotional Plane of Expression\n"
                "25 - Intuitive Plane of Expression\n"
                "26 - Physical Transit\n"
                "27 - Spiritual Transit\n"
                "28 - Mental Transit\n"
                "29 - Essence Cycle\n"
                "30 - Personal Year Number\n"
                "31 - Personal Month Number\n"
                "32 - Personal Day Number\n"
                "33 - Duality\n"
                "Want an explanation for any of the above? Type its number and press ENTER if so:   ")

karma = []
added_karma = []
karma_count = []
helper_repo = {}


def sum_digits(n, mode=""):
    s = 0

    if mode != "ignore":
        if n in MASTER_NUMBERS:
            return n
        if n in KARMIC_NUMBERS and n not in added_karma:
            karma.append(
                f"{n}/{sum(int(d) for d in str(n))}")  # append karmic number to list as a nicely formatted string
            added_karma.append(n)
    while n:
        s += n % 10
        n //= 10

    if mode != "ignore":
        if s >= 10 and s not in MASTER_NUMBERS:
            return sum_digits(s)  # recursive call in case s still has multiple digits
    else:
        if s >= 10:
            return sum_digits(s, mode="ignore")

    return s


def pure_sum_letters(f_name: str, l_name: str, m_name=""):
    name_dict = full

    for name in [f_name, l_name, m_name]:
        total = 0
        for l in name:
            l = l.upper()
            if l in name_dict:
                total += name_dict[l]
    return total


def challenge_math(n1, n2):
    res = n1 - n2
    if res < 0:
        res *= -1
    return sum_digits(res, mode="ignore")


def bridge(n1, n2, mode=""):
    x = n1 - n2
    if x < 0:
        x *= -1
    if mode == "sp":
        helper_repo.update({"sp_bridge" : x})
        print(f"Your Heart's Desire - Personality bridge is {x}")
    if mode == "le":
        helper_repo.update({"le_bridge" : x})
        print(f"Your Life's Path - Expression bridge is {x}")
    else:
        return x


def sum_digits_and_print(n, mode=""):
    x = sum_digits(n, mode='ignore')
    if mode == "maturity":
        helper_repo.update({"maturity" : x})
        print(f"Your Maturity number is {x}")
    if mode == "rational":
        helper_repo.update({"rational" : x})
        print(f"Your Rational Thought number is {x}")


def karma_print():
    karma_str = ""
    count = 0
    for entry in karma:
        karma_str += entry
        count += 1
        if count != len(karma):
            karma_str += ", "
    helper_repo.update({"karmic_debt" : karma})
    return karma_str


def passion_karma(f_name: str, l_name: str, d, m_name=""):
    master_val_list = []
    for name in [f_name, l_name, m_name]:
        val_list = []
        for l in name:
            l = l.upper()
            if l in d:
                val_list.append(d[l])
        master_val_list += val_list
    count_dict = {}
    for x in range(1, 10):
        count_dict.update({x: 0})
    for n in master_val_list:
        count_dict[n] += 1
    max_val_list = [key for (key, value) in count_dict.items() if value == max(count_dict.values())]
    karmic_list = [key for (key, value) in count_dict.items() if value == 0]

    def karmic_print():
        karma_str = ""
        count = 0
        for entry in karmic_list:
            karma_str += str(entry)
            count += 1
            if count != len(karmic_list):
                karma_str += ", "
        karma_count.clear()
        karma_count.append(count)
        helper_repo.update({"karmic_lessons" : karmic_list})
        return karma_str

    if len(max_val_list) == 1:
        print(f"Your Hidden Passion number is {max_val_list[0]}, with {count_dict[max_val_list][0]} occurrences.")
    else:
        string_list = [str(x) for x in max_val_list]
        print_str = ", ".join(string_list)
        print(f"Your Hidden Passion numbers are {print_str}, with {count_dict[max_val_list[0]]} occurrences each.")
    helper_repo.update({"passion" : max_val_list})
    print(f"Your Karmic Lesson numbers are {karmic_print()}.")
    return


def cornerstone(f_name):
    x = f_name[0].upper()
    helper_repo.update({"cornerstone" : x})
    print(f"Your Cornerstone is {x}")


def subconscious():
    x = 9 - karma_count[0]
    helper_repo.update({"subconscious": x})
    print(f"Your Subconscious Self number is {x}\n")


def planes_of_expression(f_name, l_name, m_name=""):
    planes_dict = {"Physical": 0, "Mental": 0, "Emotional": 0, "Intuitive": 0,
                   "Creative": 0, "Vacillating": 0, "Grounded": 0}
    planes_count = planes_dict.copy()
    full_name = "".join([f_name, l_name, m_name])
    letter_count = 0
    for x in full_name.upper():
        plane_name, mode_name = planes_matrix[x]
        planes_dict[plane_name] += full[x]
        planes_dict[mode_name] += full[x]
        # planes_count[plane_name] += 1   Thought I needed these, turns out I don't
        # planes_count[mode_name] += 1
        # letter_count += 1
    for k, v in planes_dict.items():
        planes_dict[k] = sum_digits(v)
    for x in ['Physical', 'Mental', 'Emotional', 'Intuitive']:
        helper_repo.update({f"{x.lower()}_plane" : planes_dict[x]})
        print(f"Your {x} Plane of Expression is {planes_dict[x]}.")

def get_age(start_date, end_date):
    difference_in_years = relativedelta(end_date, start_date).years
    return difference_in_years

def transits(age, f_name, l_name, m_name=""):

    f_name = f_name.upper()
    l_name = l_name.upper()
    m_name = m_name.upper() if m_name else ""

    def get_transit(name, target_age):
        total = 0
        while True:  # loop until we hit the target age
            for letter in name:
                total += full[letter]
                if total >= target_age:
                    return letter

    physical_letter = get_transit(f_name, age)
    spiritual_letter = get_transit(l_name, age)
    mental_letter = get_transit(m_name, age) if m_name else spiritual_letter

    print(f"\nYour Physical Transit for age {age} is {physical_letter}.")
    print(f"Your Spiritual Transit for age {age} is {spiritual_letter}.")
    print(f"Your Mental Transit for age {age} is {mental_letter}.\n")

    essence_transit = sum_digits(full[physical_letter] + full[mental_letter] + full[spiritual_letter])
    print(f"Your Essence Cycle for age {age} is {essence_transit}.\n")

    helper_repo.update({"p_transit" : physical_letter, "s_transit" : spiritual_letter, "m_transit" : mental_letter, "essence_cycle" : essence_transit})

    return physical_letter, spiritual_letter, mental_letter, essence_transit

def personals(d, m, y, essence_transit):
    y_sum = sum_digits(int(d) + int(m) + sum_digits(int(datetime.now().year), mode="ignore"), mode="ignore")
    print(f"Your Personal Year number for {datetime.now().year} is {y_sum}.")
    n_sum = sum_digits(y_sum + int(datetime.now().month), mode="ignore")
    print(f"Your Personal Month number for {datetime.now().strftime('%B')} {datetime.now().year} is {n_sum}.")
    d_sum = sum_digits(n_sum + int(datetime.now().day), mode="ignore")
    print(f"Your Personal Day number for today is {d_sum}.\n")
    print(f"Your Duality in {datetime.now().year} is {essence_transit} and {y_sum}.\n")
    helper_repo.update({"personal_y" : y_sum, "personal_m" : n_sum, "personal_d" : d_sum, "duality": [essence_transit, y_sum]})


def cmd_print(mode):

    if mode == "f_name":
        return "Enter your first name:"
    if mode == "m_name":
        return "Enter your middle name(s):"
    if mode == "l_name":
        return "Enter your last name:"
    if mode == "n_name":
        return "Enter your nickname, if you have one:"
    if mode == "d":
        return "Enter your day of birth:"
    if mode == "m":
        return "Enter your month of birth:"
    if mode == "y":
        return "Enter your year of birth:"
    if mode == "choice":
        return result_q_str
