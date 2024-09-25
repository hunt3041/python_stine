def caesar_cipher(text, shift):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    text = list(text)
    for i in range(len(text)):
        letter = text[i]
        if letter == ' ':
            continue
        else:
            alphabet_index = alphabet.index(letter)
            new_index = alphabet_index + shift if alphabet_index + shift <= 25 else (alphabet_index + shift) % 25 - 1
            new_letter = alphabet[new_index]
            text[i] = new_letter
    text = ''.join(text)
    return text

print(caesar_cipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', -16))