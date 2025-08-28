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

karma = []
added_karma = []
karma_count = 0

def sum_digits(n, mode=""):
    s = 0

    if mode != "ignore":
        if n in MASTER_NUMBERS:
            return n
        if n in KARMIC_NUMBERS and n not in added_karma:
            karma.append(f"{n}/{sum(int(d) for d in str(n))}") #append karmic number to list as a nicely formatted string
            added_karma.append(n)
    while n:
        s += n % 10
        n //= 10

    if mode != "ignore":
        if s >= 10 and s not in MASTER_NUMBERS:
            return sum_digits(s) #recursive call in case s still has multiple digits
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
    res = sum_digits(n1, mode="ignore") - sum_digits(n2, mode="ignore")
    if res < 0:
        res *= -1
    return res

def bridge(n1, n2, mode=""):
    x = n1 - n2
    if x < 0:
        x *= -1
    if mode == "sp":
        print(f"Your Heart's Desire - Personality bridge is {x}")
    if mode == "le":
        print(f"Your Life's Path - Expression bridge is {x}")

def sum_digits_and_print(n, mode=""):
    if mode == "maturity":
        print(f"Your Maturity number is {sum_digits(n, mode='ignore')}")
    if mode == "rational":
        print(f"Your Rational Thought number is {sum_digits(n, mode='ignore')}")

def karma_print():

    karma_str = ""
    count = 0
    for entry in karma:
        karma_str += entry
        count += 1
        if count != len(karma):
            karma_str += ", "
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
    passion_number = max(max_val_list)

    def karmic_print():
        karma_str = ""
        count = 0
        for entry in karmic_list:
            karma_str += str(entry)
            count += 1
            if count != len(karmic_list):
                karma_str += ", "
        karma_count = count
        return karma_str

    print(f"Your Hidden Passion number is {passion_number}, with {count_dict[passion_number]} occurrences.")
    print(f"Your Karmic Lesson numbers are {karmic_print()}.")
    return

def cornerstone(f_name):
    print(f"Your Cornerstone is {f_name[0].upper()}")

def subconscious():
    print(f"Your Subconscious Self number is {9 - karma_count}")

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
      print(f"Your {x} Plane of Expression is {planes_dict[x]}.\n")


