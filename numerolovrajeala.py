MASTER_NUMBERS = [11, 22, 33]
KARMIC_NUMBERS = [13, 14, 16, 19]

full = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
             "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "O": 6, "P": 7, "Q": 8, "R": 9,
             "S": 1, "T": 2, "U": 3, "V": 4, "W": 5, "X": 6, "Y": 7, "Z": 8}

vowels = {"A": 1, "E": 5, "I": 9, "O": 6, "U": 3}

consonants = {"B": 2, "C": 3, "D": 4, "F": 6, "G": 7, "H": 8,
              "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "Q": 8, "R": 9,
              "S": 1, "T": 2, "V": 4, "W": 5, "X": 6, "Y": 7, "Z": 8}

karma = []
added_karma = []

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

def challenge_math(n1, n2):
    res = sum_digits(n1, mode="ignore") - sum_digits(n2, mode="ignore")
    if res < 0:
        res *= -1
    return res

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
        return karma_str

    print(f"Your Passion number is {passion_number}, with {count_dict[passion_number]} occurrences.")
    print(f"Your Karmic Lesson numbers are {karmic_print()}.")
    return
