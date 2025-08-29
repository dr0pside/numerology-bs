import helpers as h
from datetime import datetime, date
from calendar import isleap

# VAR INIT:
karma = h.karma
added_karma = h.added_karma
numbers_repo = {}
bday = []


# MAIN FUNCS:

def birthday(d, m, y, mode=""):

    if mode == "date":
        reversed_bday = [y, m, d]
        bday_date = date(*reversed_bday)
        return bday_date

    res = ()

    for x in [d, m, y]:

        if x in h.MASTER_NUMBERS:
            res += (x,)
        else:
            res += (h.sum_digits(x),)

    life_path = sum(res)


    if life_path not in h.MASTER_NUMBERS and life_path >= 10:
        life_path = h.sum_digits(life_path)

    numbers_repo.update({"life_path": life_path})

    life_karma = karma.copy()

    period_print = ""
    for pos, n in [("First", h.sum_digits(m)), ("Second", h.sum_digits(d)), ("Third", h.sum_digits(y))]:
        period_print += f"  Your {pos} Period Cycle is {n}.\n"

    pinnacle1 = h.sum_digits(h.sum_digits(m) + h.sum_digits(d))
    pinnacle2 = h.sum_digits(h.sum_digits(d) + h.sum_digits(y))
    pinnacle3 = h.sum_digits(pinnacle1 + pinnacle2)
    pinnacle4 = h.sum_digits(h.sum_digits(m) + h.sum_digits(y))

    pinnacle_print = ""
    for pos, n in [("First", pinnacle1), ("Second", pinnacle2), ("Third", pinnacle3), ("Fourth", pinnacle4)]:
        pinnacle_print += f"  Your {pos} Pinnacle Cycle is {n}.\n"

    challenge1 = h.challenge_math(h.sum_digits(d, mode="ignore"), h.sum_digits(m, mode="ignore"))
    challenge2 = h.challenge_math(h.sum_digits(y, mode="ignore"), h.sum_digits(d, mode="ignore"))
    challenge3 = h.challenge_math(challenge1, challenge2)
    challenge4 = h.challenge_math(h.sum_digits(y, mode="ignore"), h.sum_digits(m, mode="ignore"))

    challenge_print = ""
    for pos, n in [("First", challenge1), ("Second", challenge2), ("Third", challenge3), ("Fourth", challenge4)]:
        challenge_print += f"  Your {pos} Challenge number is {n}.\n"

    sun_number = h.sum_digits(d + m, mode="ignore")

    if len(life_karma) == 0:
        print(
            f"\nYour Life Path is {life_path}, with no karmic debt numbers.\n{period_print}\n{pinnacle_print}\n{challenge_print}")
    else:
        print(
            f"\nYour Life Path is {life_path}, with the karmic debt(s) {h.karma_print()}.\n{period_print}\n{pinnacle_print}\n{challenge_print}")

    print(f"Your Life Path - Birth Day bridge is {h.bridge(life_path, d)}")
    print(f"Your Sun number is {sun_number}.")


def name_analysis(f_name: str, l_name: str, m_name="", n_name="", mode="", minor=False):
    name_dict = h.full

    if mode == "expression":
        func_str = "Expression"

    if mode == "soul":
        name_dict = h.vowels
        func_str = "Heart's Desire/Soul Urge"

    if mode == "personality":
        name_dict = h.consonants
        func_str = "Personality"

    if mode == "passion":
        h.passion_karma(f_name, l_name, name_dict, m_name)
        return

    if mode == "balance":
        func_str = "Balance"

    name_list = [f_name, l_name, m_name]

    if minor == True:
        name_list = n_name
        func_str = "Minor " + func_str

    name_numbers = []
    total = 0
    for x in name_list:
        for l in x:
            l = l.upper()
            if l in name_dict:
                total += name_dict[l]
            if mode == "balance":
                break  # we only want the name initials for the balance number
    name_numbers.append(h.sum_digits(total))

    expr_number = h.sum_digits(sum(name_numbers))

    if minor == False:
        numbers_repo.update({mode: int(expr_number)})
    else:
        numbers_repo.update({"minor" + mode: int(expr_number)})

    if mode == "expression" and minor == False:
        if len(karma) == 0:
            print(f"Your {func_str} number is {expr_number}, with no karmic debt numbers.")
        else:
            print(f"Your {func_str} number is {expr_number}, with the karmic debt(s) {h.karma_print()}.")
    else:
        print(f"Your {func_str} number is {expr_number}.")


# RUNNER:

def number_generator(f_name, l_name, m_name, n_name, d, m, y, ):
    h.karma.clear()
    h.added_karma.clear()
    birthday(d, m, y)
    bday.append(birthday(d, m, y, mode = "date"))
    h.get_age(bday[0], datetime.now())
    for x in ["expression", "soul", "personality"]:
        name_analysis(f_name, l_name, m_name, mode=x)
        name_analysis(f_name, l_name, m_name, n_name, mode=x, minor=True)
    h.bridge(numbers_repo["soul"], numbers_repo["personality"], mode="sp")
    h.bridge(numbers_repo["life_path"], numbers_repo["expression"], mode="le")
    h.sum_digits_and_print(numbers_repo["life_path"] + numbers_repo["expression"], mode="maturity")
    h.sum_digits_and_print(h.pure_sum_letters(f_name, l_name, m_name) + d, mode="rational")
    for x in ["passion", "balance"]:
        name_analysis(f_name, l_name, m_name, mode=x)
    h.cornerstone(f_name)
    h.subconscious()
    h.planes_of_expression(f_name, l_name, m_name)
    age = h.get_age(birthday(d, m, y, mode="date"), datetime.now())
    physical, spiritual, mental, essence = h.transits(age, f_name, l_name, m_name)
    h.personals(d, m, y, essence)

# INPUT VALIDATION:

def str_validation(string, var):
    def has_numbers(word):
        checks = []
        for x in word:
            checks.append(x.isalpha())
        if False in checks:
            return True
        return False

    while True:
        if has_numbers(string):
            print("Letters only allowed - try again.")
        else:
            return string

        string = input(h.cmd_print(var))

def int_validation(integer, var, mode="", d=0, m=0):
    current_year = datetime.now().year

    def month_check(month, d_input):
        if month in [4, 6, 9, 11] and d_input == 31:
            return True
        if month == 2 and d_input > 29:
            return True

    def year_check(year, d_input, m_input):
        if d_input == 29 and m_input == 2 and not isleap(year):
            return True

    while True:
        try:
            number = int(integer)
        except ValueError:
            print("Invalid format - please try again. Do not use letters, symbols, or start the number with 0.")
        else:
            if mode == "d":
                if not (1 <= number <= 31):
                    print("Day cannot be lower than 1 or bigger than 31.")
                else:
                    return number
            elif mode == "m":
                if not (1 <= number <= 12):
                    print("Month cannot be lower than 1 or bigger than 12.")
                elif month_check(number, d):
                    print(f"Month number {number} does not have that many days!")
                else:
                    return number
            elif mode == "y":
                if number > current_year:
                    print(f"Year cannot be in the future.")
                elif year_check(number, d, m):
                    print(f"Year {number} is not a leap year!")
                else:
                    return number
            else:
                print("Something went very wrong")

        integer = input(h.cmd_print(var))


# CMD WINDOW:

def interface(counter):

    args = []

    for x in ["f_name", "m_name", "l_name", "n_name"]:
        var = x
        x = input(h.cmd_print(f"{x}"))
        args.append(str_validation(x, var))
    args[1], args[2] = args[2], args[1]  #switching m_name and l_name positions in list to match arg order
    for n in ["d", "m", "y"]:
        var = n
        n = input(h.cmd_print(f"{n}"))
        n = int_validation(n, var, mode=var)
        args.append(int(n))

    number_generator(*args)

    x = input("Want to go again? Type 'YES' if so:   ")
    if x.upper() == "YES":
        counter += 1
        print(f"You owe me {50 * counter} RON now.")
        interface(counter)
    else:
        input("\nPress any button to exit...")
        quit()


if __name__ == "__main__":
    print("Welcome to the Number Wizard! 50 RON per use.\n")
    interface(counter=1)


