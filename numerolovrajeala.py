import helpers as h

karma = h.karma

def birthday(d, m, y):
    res = ()

    global karma

    for x in [d, m, y]:

        if x in h.master_numbers:
            res += (x,)
        else:
            res += (h.sum_digits(x),)

    life_path = sum(res)

    if life_path not in h.master_numbers and life_path >= 10:
        life_path = h.sum_digits(life_path)

    life_karma = karma.copy()

    period_print = (f"  Your First Period Cycle is {h.sum_digits(m)}.\n"
                    f"  Your Second Period Cycle is {h.sum_digits(d)}.\n"
                    f"  Your Third Period Cycle is {h.sum_digits(y)}.\n")

    pinnacle1 = h.sum_digits(h.sum_digits(m) + h.sum_digits(d))
    pinnacle2 = h.sum_digits(h.sum_digits(d) + h.sum_digits(y))
    pinnacle3 = h.sum_digits(pinnacle1 + pinnacle2)
    pinnacle4 = h.sum_digits(h.sum_digits(m) + h.sum_digits(y))

    pinnacle_print = (f"  Your First Pinnacle Cycle is {pinnacle1}.\n"
                      f"  Your Second Pinnacle Cycle is {pinnacle2}.\n"
                      f"  Your Third Pinnacle Cycle is {pinnacle3}.\n"
                      f"  Your Fourth Pinnacle Cycle is {pinnacle4}.\n")

    challenge1 = h.challenge_math(d, m)
    challenge2 = h.challenge_math(y, d)
    challenge3 = h.challenge_math(challenge1, challenge2)
    challenge4 = h.challenge_math(y, m)

    challenge_print = (f"  Your First Challenge number is {challenge1}.\n"
                       f"  Your Second Challenge number is {challenge2}.\n"
                       f"  Your Third Challenge number is {challenge3}.\n"
                       f"  Your Fourth Challenge number is {challenge4}.\n")

    sun_number = h.sum_digits(d + m, mode="ignore")

    if len(life_karma) == 0:
        print(
            f"\nYour Life Path is {life_path}, with no karmic debt numbers.\n{period_print}\n{pinnacle_print}\n{challenge_print}")
    else:
        print(
            f"\nYour Life Path is {life_path}, with the karmic debt(s) {h.karma_print()}.\n{period_print}\n{pinnacle_print}\n{challenge_print}")

    print(f"Your Sun number is {sun_number}.")

    h.karma.clear()
    h.added_karma.clear()


def name_analysis(f_name: str, l_name: str, m_name="", mode=""):
    name_dict = h.full

    func_str = "Expression"

    if mode == "soul":
        name_dict = h.vowels
        func_str = "Soul"

    if mode == "personality":
        name_dict = h.consonants
        func_str = "Personality"

    if mode == "passion":
        h.passion_karma(f_name, l_name, name_dict, m_name)
        return

    if mode == "balance":
        func_str = "Balance"

    name_numbers = []
    for name in [f_name, l_name, m_name]:
        total = 0
        for l in name:
            l = l.upper()
            if l in name_dict:
                total += name_dict[l]
            if mode == "balance":
                break  # we only want the name initials for the balance number
        name_numbers.append(h.sum_digits(total))

    expr_number = sum(name_numbers)

    if mode == "":
        if len(h.karma) == 0:
            print(f"Your {func_str} number is {h.sum_digits(expr_number)}, with no karmic debt numbers.")
        else:
            print(f"Your {func_str} number is {h.sum_digits(expr_number)}, with the karmic debt(s) {h.karma_print()}.")
    else:
        print(f"Your {func_str} number is {h.sum_digits(expr_number)}.")

    h.karma.clear()
    h.added_karma.clear()

#RUNNER:

def number_generator(f_name, l_name, d, m, y):

    birthday(d, m, y)
    name_analysis(f_name, l_name)
    for x in ["soul", "personality", "passion", "balance"]:
        name_analysis(f_name, l_name, mode=x)


#INPUT HANDLING:

def str_validation(string):
    def has_numbers(word):
        return any(char.isdigit() for char in word)
    if has_numbers(string):
        print("Letters only allowed - try again.")
        interface()

def int_validation(integer):
    def has_letters(number):
        return number.isalpha() or number.startswith("0")
    if has_letters(integer):
        print("Invalid format - please try again. Do not use letters or start number with 0.")
        interface()
    else:
        return int(integer)

def interface():
    f_name = input("Enter your first name:")
    str_validation(f_name)
    l_name = input("Enter your last name:")
    str_validation(l_name)
    d = input("Enter your day of birth:")
    d = int_validation(d)
    m = input("Enter your month of birth:")
    m = int_validation(m)
    y = input("Enter your year of birth:")
    y = int_validation(y)
    number_generator(f_name, l_name, d, m, y)

if __name__ == "__main__":
    interface()
    input("\nPress any button to exit...")


