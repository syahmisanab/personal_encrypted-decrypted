import base64
import string

list = "aGlraWtvbW9yaQ=="

de_list = base64.b64decode(list).decode('utf-8')

symbol_map = {
    'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '!', 'H': '^', 'I': '(', 'J': ')',
    'K': '_', 'L': '+', 'M': '=', 'N': '[', 'O': ']', 'P': '{', 'Q': '}', 'R': '|', 'S': ';', 'T': ':',
    'U': '<', 'V': '>', 'W': '?', 'X': '/', 'Y': ',', 'Z': '.',
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0',
    'k': '-', 'l': '=', 'm': '~', 'n': '`', 'o': '¬', 'p': '£', 'q': '€', 'r': '¥', 's': '¢', 't': '¤',
    'u': '§', 'v': '¶', 'w': '•', 'x': '†', 'y': '‡', 'z': '°'
}

prime_shifts = [2, 3, 5, 7]


def encrypt_message(text, theme):
    encrypted = ""
    prime_index = 0

    if theme != de_list:
        prime_shifts.reverse()

    for char in text:
        if char.isalpha():
            shift = prime_shifts[prime_index]
            prime_index = (prime_index + 1) % len(prime_shifts)

            if char.islower():
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)

            encrypted += symbol_map.get(shifted_char, char)
        else:
            encrypted += char

    return encrypted


def decrypt_message(encrypted_text, theme):
    reverse_symbol_map = {v: k for k, v in symbol_map.items()}
    decrypted = ""
    prime_index = 0

    if theme != de_list:
        prime_shifts.reverse()

    for char in encrypted_text:
        if char in reverse_symbol_map:
            original_char = reverse_symbol_map[char]
            shift = prime_shifts[prime_index]
            prime_index = (prime_index + 1) % len(prime_shifts)

            if original_char.islower():
                shifted_back_char = chr((ord(original_char) - 97 - shift) % 26 + 97)
            else:
                shifted_back_char = chr((ord(original_char) - 65 - shift) % 26 + 65)

            decrypted += shifted_back_char
        else:
            decrypted += char

    return decrypted


def main():
    action = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()
    text = input("Enter your message: ")

    if action in ['e', 'd']:
        theme = input("Enter the theme: ")
        if action == 'e':
            result = encrypt_message(text, theme)
            print(f"Encrypted Message: {result}")
        elif action == 'd':
            result = decrypt_message(text, theme)
            print(f"Decrypted Message: {result}")
    else:
        print("Invalid input! Please choose 'e' to encrypt or 'd' to decrypt.")


if __name__ == "__main__":
    main()
