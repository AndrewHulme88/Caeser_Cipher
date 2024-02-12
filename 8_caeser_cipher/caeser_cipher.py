alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

def caeser(direction_choice, input_text, shift_amount):
    new_text = ""
    for letter in input_text:
        if letter in alphabet:
            if direction_choice == "encode":
                position = (alphabet.index(letter) + shift_amount) % 26

            elif direction_choice == "decode":
                position = (alphabet.index(letter) - shift_amount) % 26
            else:
                return
            new_text += alphabet[position]
        else:
            new_text += letter
    print(f"The {direction_choice}d text is: {new_text}")


import art
print(art.logo)


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(direction_choice=direction, input_text=text, shift_amount=shift)        

    result = input("Type 'yes' if you would like to try again. Otherwise, type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Farewell")
