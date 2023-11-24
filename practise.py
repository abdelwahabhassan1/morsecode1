# Morse code dictionary
# morse_code_dict = {'A': '.-', 'B': '-...',
#                    'C': '-.-.', 'D': '-..', 'E': '.',
#                    'F': '..-.', 'G': '--.', 'H': '....',
#                    'I': '..', 'J': '.---', 'K': '-.-',
#                    'L': '.-..', 'M': '--', 'N': '-.',
#                    'O': '---', 'P': '.--.', 'Q': '--.-',
#                    'R': '.-.', 'S': '...', 'T': '-',
#                    'U': '..-', 'V': '...-', 'W': '.--',
#                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
#                    '1': '.----', '2': '..---', '3': '...--',
#                    '4': '....-', '5': '.....', '6': '-....',
#                    '7': '--...', '8': '---..', '9': '----.',
#                    '0': '-----', ' ': ' '}


# class MorseCodeConverter:
#     def __init__(self):
#         pass

#     def encrypt(self, text):
#         encrypted_text = ''
#         for char in text:
#             char = char.upper()
#             if char in morse_code_dict:
#                 encrypted_text += morse_code_dict[char] + ' '
#             elif char.isalpha() or char.isdigit():
#                 encrypted_text += 'UNKNOWN '
#             else:
#                 encrypted_text += ' '
#         return encrypted_text.rstrip()

#     def decrypt(self, morse_code):
#         morse_code_list = morse_code.split(' ')
#         decrypted_text = ''
#         for code in morse_code_list:
#             found = False
#             for key, value in morse_code_dict.items():
#                 if code == value:
#                     decrypted_text += key
#                     found = True
#             if not found:
#                 decrypted_text += 'UNKNOWN'
#         return decrypted_text


# # Main program
# morse_converter = MorseCodeConverter()

# # User input
# phrase_to_encrypt = input("Enter a phrase to encrypt: ")
# encrypted_phrase = morse_converter.encrypt(phrase_to_encrypt)
# decrypted_phrase = morse_converter.decrypt(encrypted_phrase)

# # Output
# print(f"Original phrase: {phrase_to_encrypt}")
# print(f"Encrypted phrase: {encrypted_phrase}")
# print(f"Decrypted phrase: {decrypted_phrase}")
# ##################################################################################
# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def encrypt_morse_code(text):
    encrypted_result = ""
    
    for char in text:
        char_upper = char.upper()
        if char_upper in morse_code_dict:
            encrypted_result += morse_code_dict[char_upper] + ' '

    return encrypted_result.rstrip()

def decrypt_morse_code(code):
    decrypted_result = ""
    morse_to_char = {value: key for key, value in morse_code_dict.items()}

    for word in code.split():
        if word in morse_to_char:
            decrypted_result += morse_to_char[word]

    return decrypted_result

# Example Usage:
user_input = input("Enter a phrase to encrypt: ")
encrypted_result = encrypt_morse_code(user_input)
print("Encrypted Morse Code:", encrypted_result)

user_input_decrypt = input("Enter Morse code to decrypt: ")
decrypted_result = decrypt_morse_code(user_input_decrypt)
print("Decrypted Phrase:", decrypted_result)
