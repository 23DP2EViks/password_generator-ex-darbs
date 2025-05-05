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

    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
    ]

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


def save_passwords(passwords, filename="passwords.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    existing_passwords = {entry["password"] for entry in data}

    for pwd in passwords:
        if pwd not in existing_passwords:
            data.append({"password": pwd, "strength": check_password_strength(pwd)})

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Paroles tiek saglabātas {filename}")


def clear_password_file(filename="passwords.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4, ensure_ascii=False)
    print(f"{filename} ir notīrīts.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Nepareiza ievade. Lūdzu ievadiet 'y' vai 'n'.")


def main():
    passwords = []
    while True:
        print("\n1. Ģenerēt paroli")
        print("2. Pārbaudiet paroles sarežģītību")
        print("3. Saglabāt paroles failā")
        print("4. Iziet")

        choice = input("Atlasīt darbību: ")

        if choice == "1":
            try:
                length_input = input("Paroles garums (noklusējums 12): ")
                length = int(length_input) if length_input else 12
            except ValueError:
                print("Nepareiza ievade. Izmantots garums 12.")
                length = 12

            use_digits = ask_yes_no("Ieslēgt ciparus? (y/n): ")
            use_symbols = ask_yes_no("Vai iespējot īpašās rakstzīmes? (y/n): ")
            include_rare = ask_yes_no("Vai ieslēgt arī retas rakstzīmes (`:;~\\|[]{}'\")? (y/n): ")
            excluded = input("Ievadi simbolus, kurus izslēgt no paroles (atstāj tukšu, ja nav): ")

            try:
                password = generate_password(length, use_digits, use_symbols, include_rare, excluded)
                print("Ģenerētā parole:", password)
                print("Paroles stiprums:", check_password_strength(password))
                passwords.append(password)
            except ValueError as e:
                print("Kļūda:", str(e))

        elif choice == "2":
            password = input("Ievadiet paroli, lai pārbaudītu: ")
            strength = check_password_strength(password)
            print("Paroles stiprums:", strength)

        elif choice == "3":
            save_passwords(passwords)
            passwords = []

        elif choice == "4":
            if ask_yes_no("Vai notīrīt passwords.json failu? (y/n): "):
                clear_password_file()
            break

        else:
            print("Nepareiza ievade. Mēģiniet vēlreiz.")


if __name__ == "__main__":
    main()