import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(message, s, dir):
    if dir == 'encode':
        new_message = []
        ind = 0
        for i in message:
            if i == ' ':
                new_message.append(" ")
            elif i not in alphabet:
                new_message.append(i)
            else:
                if s <= 26:
                    ind = alphabet.index(i)
                    new_message.append(alphabet[ind + s])
                else:
                    ind = alphabet.index(i)
                    new_message.append(alphabet[ind + s % 26])
        new_message = ''.join(new_message)
        print(new_message)
    if dir == 'decode':
        new_message = []
        ind = 0
        for i in message:
            if i == ' ':
                new_message.append(' ')
            elif i not in alphabet:
                new_message.append(i)
            else:
                ind = alphabet.index(i)
                new_message.append(alphabet[ind - s % 26])
        new_message = ''.join(new_message)
        print(new_message)
print(art.logo)
decision = "yes"
while decision.lower() == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    decision = input("would you like to try again? enter yes or no:\n")



