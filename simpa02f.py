import random


def generate_long_password(password_lenght, my_list1, my_list2, my_list3):
    long_password = ""
    for item in range(0, password_lenght):
        long_password += str(random.choice(my_list1))
        long_password += str(random.choice(my_list2))
        long_password += str(random.choice(my_list3))
    return long_password


def generate_short_password(password_lenght, my_list):
    short_password = ""
    for item in range(0, password_lenght):
        short_password += str(random.choice(my_list))
    return short_password


def main():
    numbers = [0, 6, 3, 7, 4, 9, 1, 5, 2, 8]
    letters = ['h', 'r', 'b', 'u', 'd', 'q', 'o', 'l', 's', 'a', 'y', 'e', 'k', 'i', 'w', 'g', 'j', 'm', 'x', 'p', 'z', 'v', 'f', 't', 'b', 'n']
    symbols = ['%', '-', '&', '$', ')', '!', '*', '@', '_', '(', '+', '#', '=']
    short_password_letters = generate_short_password(10, letters)
    short_password_symbols = generate_short_password(10, symbols)
    long_password = generate_long_password(10, letters,numbers, symbols)


    print("Password with Letters, Numbers and Symbols: " + long_password)
    print("Password with Letters: " + short_password_letters)
    print("Password with Symbols: " + short_password_symbols)

if __name__ == "__main__":
    main()
