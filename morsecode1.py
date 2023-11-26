# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'}   
 #This dictionary maps each character (both uppercase and numbers) to its Morse code representation.

def encrypt_morse_code(text):             #text is the input phrase that will be encrypted 
    encrypted_result = ""
                                            #It converts the character to uppercase
    for char in text:
        char_upper = char.upper()
        if char_upper in morse_code_dict:
            encrypted_result += morse_code_dict[char_upper] + ' '

    return encrypted_result.rstrip()              #it removes the trailing space using rstrip() and returns the encrypted result.


def decrypt_morse_code(code):
    decrypted_result = ""
    morse_to_char = {value: key for key, value in morse_code_dict.items()}
    for word in code.split():
        if word in morse_to_char:
            decrypted_result += morse_to_char[word]

    return decrypted_result


    
