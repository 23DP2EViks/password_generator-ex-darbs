import random
import string
import json
import re


def generate_password(length=12, use_digits=True, use_symbols=True, include_rare_symbols=False, excluded_chars=""):
    if length < 4:
        raise ValueError("Parolei jābūt vismaz 4 simbolus garai.")

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


def filter_passwords_by_strength(passwords, level):
    return [p for p in passwords if check_password_strength(p) == level]


def search_passwords(passwords, substring):
    return [p for p in passwords if substring in p]


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Nepareiza ievade. Lūdzu ievadiet 'y' vai 'n'.")


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
        print(f"Paroles saglabātas failā: {filename}")

    def clear_file(self, filename="passwords.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        print(f"{filename} ir notīrīts.")

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


def main():
    manager = PasswordManager()

    while True:
        print("\n1. Ģenerēt paroli")
        print("2. Pārbaudīt paroles stiprumu")
        print("3. Saglabāt ģenerētās paroles failā")
        print("4. Notīrīt parole failu")
        print("5. Meklēt paroles pēc fragmenta")
        print("6. Filtrēt paroles pēc stipruma")
        print("7. Iziet")

        choice = input("Atlasīt darbību: ")

        if choice == "1":
            try:
                length = int(input("Paroles garums (noklusējums 12): ") or 12)
            except ValueError:
                print("Nepareiza ievade. Izmantots garums 12.")
                length = 12

            use_digits = ask_yes_no("Ieslēgt ciparus? (y/n): ")
            use_symbols = ask_yes_no("Ieslēgt īpašās rakstzīmes? (y/n): ")
            include_rare = ask_yes_no("Iekļaut arī retās rakstzīmes (`:;~\\|[]{}'\")? (y/n): ")
            excluded = input("Simboli, ko izslēgt (atstāj tukšu, ja nav): ")

            try:
                pwd = manager.generate(length, use_digits, use_symbols, include_rare, excluded)
                print("Ģenerētā parole:", pwd)
                print("Stiprums:", manager.check_strength(pwd))
            except ValueError as e:
                print("Kļūda:", str(e))

        elif choice == "2":
            pwd = input("Ievadi paroli pārbaudei: ")
            print("Paroles stiprums:", manager.check_strength(pwd))
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
            print("Rezultāti:", found if found else "Nav sakritību.")

        elif choice == "6":
            level_map = {"1": "Vājš", "2": "Vidējs", "3": "Spēcīgs"}
            while True:
                level_input = input("Ievadi vajadzīgā līmeņa numuru (1 - Vājš, 2 - Vidējs, 3 - Spēcīgs): ").strip()
                if level_input in level_map:
                    level = level_map[level_input]
                    break
                else:
                    print("Nepareiza izvēle. Mēģini vēlreiz (1, 2 vai 3).")

            filtered = manager.filter_by_strength(level)
            print("Rezultāti:", filtered if filtered else "Nav sakritību.")

        elif choice == "7":
            print("Programma tiek aizvērta.")
            break

        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")


if __name__ == "__main__":
    main()