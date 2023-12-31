import random

def encode_word(word):
    if len(word) > 3:
        return word[::2]

def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        decoded_word = word[3:-3]
        decoded_word = decoded_word[-1] + decoded_word[:-1]
        return decoded_word

def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    choice = input("Enter 'code' to encode or 'decode' to decode: ")
    message = input("Enter the message: ")

    if choice == 'encode':
        encoded_message = encode_message(message)
        print("Encoded message:", encoded_message)
    elif choice == 'decode':
        decoded_message = decode_message(message)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice. Please enter 'code' or 'decode'.")

if __name__ == '__main__':
    main()