import random
import string
import json
import re

def generate_password(length=12, use_digits=True, use_symbols=True, include_rare_symbols=False, excluded_chars=""):
    if length < 4:
        raise ValueError("Parolei jābūt vismaz 4 simbolus garai.")
    if length > 128:
        raise ValueError("Parolei jābūt ne garākai par 128 simboliem.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    common_symbols = "!@#$%^&*()-_=+,.<>/?"
    rare_symbols = "`:;~\\|[]{}'\""
    all_symbols = common_symbols + (rare_symbols if include_rare_symbols else "")

    def remove_excluded(s):
        return ''.join(c for c in s if c not in excluded_chars and c != ' ')

    lowercase = remove_excluded(lowercase)
    uppercase = remove_excluded(uppercase)
    digits = remove_excluded(digits)
    all_symbols = remove_excluded(all_symbols)

    if not lowercase or not uppercase or (use_digits and not digits) or (use_symbols and not all_symbols):
        raise ValueError("Pēc izslēgto simbolu noņemšanas nav iespējams izveidot paroli ar dotajiem parametriem.")

    password_chars = [random.choice(lowercase), random.choice(uppercase)]
    if use_digits:
        password_chars.append(random.choice(digits))
    if use_symbols:
        password_chars.append(random.choice(all_symbols))

    pool = lowercase + uppercase
    if use_digits:
        pool += digits
    if use_symbols:
        pool += all_symbols

    remaining_length = length - len(password_chars)
    password_chars += random.choices(pool, k=remaining_length)
    random.shuffle(password_chars)

    return ''.join(password_chars)

def check_password_strength(password):
    length_score = len(password) >= 12
    has_lower = re.search(r'[a-z]', password) is not None
    has_upper = re.search(r'[A-Z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_symbol = re.search(r'[^\w\s]', password) is not None

    if length_score and has_lower and has_upper and has_digit and has_symbol:
        return "Spēcīgs"
    elif length_score and ((has_digit and has_symbol) or (has_upper and has_lower)):
        return "Vidējs"
    else:
        return "Vājš"

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("\033[92mNepareiza ievade. Lūdzu ievadiet 'y' vai 'n'.\033[0m")

def display_password_table(password_list):
    if not password_list:
        print("\033[92mNav par ko rādīt.\033[0m")
        return

    max_pwd_length = max(len(item["password"]) for item in password_list)
    max_pwd_length = max(max_pwd_length, len("Parole"))

    total_width = 4 + 2 + max_pwd_length + 2 + 10 + 2 + 4

    border = "\033[34m" + "=" * total_width + "\033[0m"
    row_separator = "\033[34m" + "-" * total_width + "\033[0m"
    header_format = f"\033[34m|\033[0m \033[96m{{:^4}}\033[0m \033[34m|\033[0m \033[96m{{:<{max_pwd_length}}}\033[0m \033[34m|\033[0m \033[96m{{:<10}}\033[0m \033[34m|\033[0m"
    row_format = f"\033[34m|\033[0m {{:^4}} \033[34m|\033[0m {{:<{max_pwd_length}}} \033[34m|\033[0m {{:<10}} \033[34m|\033[0m"

    print(border)
    print(header_format.format("Nr", "Parole", "Stiprums"))
    print(row_separator)

    for idx, item in enumerate(password_list, 1):
        print(row_format.format(idx, item['password'], item['strength']))
        print(row_separator)

    print(border)

class PasswordStats:
    def __init__(self, passwords):
        self.passwords = passwords
        self.weak = 0
        self.medium = 0
        self.strong = 0
        self.total = 0
        self._analyze()

    def _analyze(self):
        for entry in self.passwords:
            strength = entry.get("strength")
            if strength == "Vājš":
                self.weak += 1
            elif strength == "Vidējs":
                self.medium += 1
            elif strength == "Spēcīgs":
                self.strong += 1
        self.total = len(self.passwords)

    def display(self):
        print("\033[93mParoļu statistika:")
        print(f"Kopā: {self.total}")
        print(f" - Vājš: {self.weak}")
        print(f" - Vidējs: {self.medium}")
        print(f" - Spēcīgs: {self.strong}\033[0m")

class PasswordManager:
    def __init__(self):
        self.passwords = []

    def generate(self, length, use_digits, use_symbols, include_rare, excluded_chars):
        password = generate_password(length, use_digits, use_symbols, include_rare, excluded_chars)
        self.passwords.append(password)
        return password

    def check_strength(self, password):
        return check_password_strength(password)

    def save(self, filename="passwords.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        existing_passwords = {entry["password"] for entry in data}
        for pwd in self.passwords:
            if pwd not in existing_passwords:
                data.append({"password": pwd, "strength": check_password_strength(pwd)})

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        self.passwords = []
        print(f"\033[92mParoles saglabātas failā: {filename}\033[0m")

    def clear_file(self, filename="passwords.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        print(f"\033[92m{filename} ir notīrīts.\033[0m")

    def filter_by_strength(self, level):
        try:
            with open("passwords.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        return [entry["password"] for entry in data if entry.get("strength") == level]

    def search(self, substring):
        try:
            with open("passwords.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        return [entry["password"] for entry in data if substring in entry.get("password", "")]

    def sort_passwords(self, by="length"):
        try:
            with open("passwords.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        if by == "length":
            sorted_data = sorted(data, key=lambda x: len(x["password"]))
        elif by == "alphabet":
            sorted_data = sorted(data, key=lambda x: x["password"])
        elif by == "strength":
            order = {"Vājš": 0, "Vidējs": 1, "Spēcīgs": 2}
            sorted_data = sorted(data, key=lambda x: order.get(x["strength"], -1))
        else:
            print("\033[92mNepareizs kārtošanas veids.\033[0m")
            return []

        return sorted_data

    def show_stats(self):
        try:
            with open("passwords.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        stats = PasswordStats(data)
        stats.display()

def main():
    manager = PasswordManager()

    while True:
        print("\n\033[92m1. Ģenerēt paroli")
        print("2. Pārbaudīt paroles stiprumu")
        print("3. Saglabāt ģenerētās paroles failā")
        print("4. Notīrīt parole failu")
        print("5. Meklēt paroles pēc fragmenta")
        print("6. Filtrēt paroles pēc stipruma")
        print("7. Iziet")
        print("8. Kārtot paroles un parādīt tabulā")
        print("9. Rādīt statistiku parolēm\033[0m")

        choice = input("Atlasīt darbību: ")

        if choice == "1":
            try:
                length = int(input("Paroles garums (noklusējums 12): ") or 12)
            except ValueError:
                print("\033[92mNepareiza ievade. Izmantots garums 12.\033[0m")
                length = 12

            use_digits = ask_yes_no("Ieslēgt ciparus? (y/n): ")
            use_symbols = ask_yes_no("Ieslēgt īpašās rakstzīmes? (y/n): ")
            include_rare = ask_yes_no("Iekļaut arī retās rakstzīmes (`:;~\\|[]{}'\")? (y/n): ")
            excluded = input("Simboli, ko izslēgt (atstāj tukšu, ja nav): ")

            try:
                pwd = manager.generate(length, use_digits, use_symbols, include_rare, excluded)
                strength = manager.check_strength(pwd)
                print(f"\033[92mĢenerētā parole: {pwd}")
                print(f"Stiprums: {strength}\033[0m")
            except ValueError as e:
                print(f"\033[92mKļūda: {str(e)}\033[0m")

        elif choice == "2":
            pwd = input("Ievadi paroli pārbaudei: ")
            if len(pwd) > 128:
                print("\033[92mParole nedrīkst pārsniegt 128 simbolus.\033[0m")
                continue
            strength = manager.check_strength(pwd)
            print(f"\033[92mParoles stiprums: {strength}\033[0m")
            manager.passwords.append(pwd)
            if ask_yes_no("Ne vēlaties saglabāt šo paroli failā? (y/n): "):
                manager.save()

        elif choice == "3":
            manager.save()

        elif choice == "4":
            if ask_yes_no("Vai tiešām dzēst paroles no faila? (y/n): "):
                manager.clear_file()

        elif choice == "5":
            sub = input("Ievadi fragmentu meklēšanai: ")
            found = manager.search(sub)
            if found:
                print("\033[92mRezultāti:\033[0m [", end="")
                for i, pwd in enumerate(found):
                    print(f"\033[96m{pwd}\033[0m", end="")
                    if i != len(found) - 1:
                        print(", ", end="")
                print("]")
            else:
                print("\033[92mRezultāti: Nav sakritību.\033[0m")

        elif choice == "6":
            level_map = {"1": "Vājš", "2": "Vidējs", "3": "Spēcīgs"}
            while True:
                level_input = input("Ievadi vajadzīgā līmeņa numuru (1 - Vājš, 2 - Vidējs, 3 - Spēcīgs): ").strip()
                if level_input in level_map:
                    level = level_map[level_input]
                    break
                else:
                    print("\033[92mNepareiza izvēle. Mēģini vēlreiz (1, 2 vai 3).\033[0m")

            filtered = manager.filter_by_strength(level)
            if filtered:
                print("\033[92mRezultāti:\033[0m [", end="")
                for i, pwd in enumerate(filtered):
                    print(f"\033[96m{pwd}\033[0m", end="")
                    if i != len(filtered) - 1:
                        print(", ", end="")
                print("]")
            else:
                print("\033[92mRezultāti: Nav sakritību.\033[0m")

        elif choice == "7":
            print("\033[92mProgramma tiek aizvērta.\033[0m")
            break

        elif choice == "8":
            print("\n\033[92mKārtošanas veidi:")
            print("1 - Garums")
            print("2 - Alfabēts")
            print("3 - Stiprums\033[0m")
            sort_choice = input("Izvēlies kārtošanas veidu (1/2/3): ").strip()
            sort_map = {"1": "length", "2": "alphabet", "3": "strength"}
            sort_by = sort_map.get(sort_choice)

            if not sort_by:
                print("\033[92mNepareiza izvēle.\033[0m")
                continue

            sorted_pwds = manager.sort_passwords(by=sort_by)
            display_password_table(sorted_pwds)

        elif choice == "9":
            manager.show_stats()

        else:
            print("\033[92mNepareiza izvēle. Mēģini vēlreiz.\033[0m")

if __name__ == "__main__":
    main()
