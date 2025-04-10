import random
import string
import json


def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters 
    if use_digits:
        characters += string.digits 
    if use_symbols:
        characters += string.punctuation 

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    length_score = len(password) >= 12
    has_digits = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)
    
    strength = "Vāji"
    if length_score and has_digits and has_symbols:
        strength = "Spēcīgs"
    elif length_score and (has_digits or has_symbols):
        strength = "vidēji"

    return strength


def save_passwords(passwords, filename="passwords.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.extend(passwords)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Paroles tiek saglabātas {filename}")


def main():
    passwords = []
    while True:
        print("\n1. Ģenerēt paroli")
        print("2. Pārbaudiet paroles sarežģītību")
        print("3. Saglabāt paroles failā")
        print("4. Iziet")

        choice = input("Atlasīt darbību: ")

        if choice == "1":
            length = int(input("Paroles garums (noklusējums 12): ") or 12)
            use_digits = input("Ieslēgt ciparus? (y/n): ").lower() == 'y'
            use_symbols = input("Vai iespējot īpašās rakstzīmes? (y/n): ").lower() == 'y'

            password = generate_password(length, use_digits, use_symbols)
            print("Ģenerētā parole:", password)
            passwords.append(password)

        elif choice == "2":
            password = input("Ievadiet paroli, lai pārbaudītu: ")
            strength = check_password_strength(password)
            print("Paroles stiprums:", strength)

        elif choice == "3":
            save_passwords(passwords)
            passwords = []

        elif choice == "4":
            break

        else:
            print("Nepareiza ievade. Mēģiniet vēlreiz.")

if __name__ == "__main__":
    main()
