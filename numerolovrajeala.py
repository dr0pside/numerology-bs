import helpers as h
from datetime import datetime
from calendar import isleap

#VAR INIT:
karma = h.karma
added_karma = h.added_karma
numbers_repo = {}


#MAIN FUNCS:

def birthday(d, m, y):
    res = ()

    for x in [d, m, y]:

        if x in h.MASTER_NUMBERS:
            res += (x,)
        else:
            res += (h.sum_digits(x),)

    life_path = sum(res)
    numbers_repo.update({"life_path" : life_path })

    if life_path not in h.MASTER_NUMBERS and life_path >= 10:
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
    
    print(f"Your Life Path - Birthday bridge is {h.bridge(life_path, d)}")
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
    
    name_str = "".join([f_name, l_name, m_name])
    
    if minor == True:
        name_str = n_name
        func_str = "Minor " + func_str
    
    name_numbers = []
    total = 0
    for l in name_str:
        l = l.upper()
        if l in name_dict:
            total += name_dict[l]
        if mode == "balance":
            break  # we only want the name initials for the balance number
    name_numbers.append(h.sum_digits(total))

    expr_number = h.sum_digits(sum(name_numbers))
    
    if minor == False:
        numbers_repo.update({mode : int(expr_number)})
    else:
        numbers_repo.update({"minor" + mode : int(expr_number)})
    

    if mode == "expression":
        if len(karma) == 0:
            print(f"Your {func_str} number is {expr_number}, with no karmic debt numbers.")
        else:
            print(f"Your {func_str} number is {expr_number}, with the karmic debt(s) {h.karma_print()}.")
    else:
        print(f"Your {func_str} number is {expr_number}.")

#RUNNER:

def number_generator(f_name, l_name, m_name, n_name, d, m, y,):

    h.karma.clear()
    h.added_karma.clear()
    birthday(d, m, y)
    for x in ["expression","soul", "personality"]:
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
    

#INPUT VALIDATION:

def str_validation(string):
    def has_numbers(word):
        checks = []
        for x in word:
            checks.append(x.isalpha())
        if False in checks:
            return True
    if has_numbers(string):
        print("Letters only allowed - try again.")
        interface()

def int_validation(integer, mode="", d=0, m=0):
    
    current_year = datetime.now().year

    def has_letters(number):
        return number.isalpha() or number.startswith("0")
    
    def month_check(month, d_input):
        if month in [4, 6, 9, 11] and d_input == 31:
            return True
        if month == 2 and d_input > 29:
            return True

    def year_check(year, d_input, m_input):
        if d_input == 29 and m_input == 2 and isleap(year):
            return True
    
    def out_of_bounds(number, mode, d=0, m=0):
        number = int(number)
        if mode == "day" and number > 31 or number < 1:
            print("Day cannot be lower than 1 or bigger than 31.")
            return True
        if mode == "month": 
            if number > 12 or number < 1:
                print(f"Month cannot be lower than 1 or bigger than 12.")
                return True
            if month_check(number, d):
                print(f"Month number {number} does not have that many days!")
                return True
        if mode == "year":
            if number > current_year:
                print(f"Year cannot be in the future.")
                return True
            if year_check(number, d, m):
                print(f"Year {number} is not a leap year!")
                return True
        
            return False
            
    if has_letters(integer):
        print("Invalid format - please try again. Do not use letters or start number with 0.")
            
    elif out_of_bounds(integer, mode, d, m):
        interface()

#CMD WINDOW:

def interface():

    f_name = input("Enter your first name:")
    str_validation(f_name)
    m_name = input("Enter your middle name (optional):")
    str_validation(m_name)
    l_name = input("Enter your last name:")
    str_validation(l_name)
    n_name = input("Enter your nickname, if you have one:")
    str_validation(n_name)
    if n_name == "":
        n_name = f_name
    
    d = input("Enter your day of birth:")
    int_validation(d, "day")
    stored_d = int(d)
    
    m = input("Enter your month of birth:")
    int_validation(m, "month", stored_d)
    stored_m = int(m)

    y = input("Enter your year of birth:")
    int_validation(y, "year", stored_d, stored_m)
    stored_y = int(y)
    
    number_generator(f_name, l_name, m_name, n_name, stored_d, stored_m, stored_y)
    
    x = input("Want to go again? Type 'YES' if so:   ")
    if x.upper() == "YES":
        interface()
    else:
        input("\nPress any button to exit...")
        quit()

if __name__ == "__main__":
    interface()



