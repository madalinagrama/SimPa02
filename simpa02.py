import random

numbers = [0, 6, 3, 7, 4, 9, 1, 5, 2, 8]
letters = ['h', 'r', 'b', 'u', 'd', 'q', 'o', 'l', 's', 'a', 'y', 'e', 'k', 'i', 'w', 'g', 'j', 'm', 'x', 'p', 'z', 'v', 'f', 't', 'b', 'n']
symbols = ['%', '-', '&', '$', ')', '!', '*', '@', '_', '(', '+', '#', '=']

def generate_long_password(pass_lenght, my_list1, my_list2, my_list3):
    long_password = ""
    for item in range(0, pass_lenght):
        position = random.randint(0, len(my_list1)-1)
        long_password += str(my_list1[position])
        position = random.randint(0, len(my_list2)-1)
        long_password += str(my_list2[position])
        position = random.randint(0, len(my_list3)-1)
        long_password += str(my_list3[position])
    return long_password

print(generate_long_password(10, numbers, letters, symbols))

def generate_short_password(pass_lenght, my_list):
    short_password = ""
    for item in range (0, pass_lenght):
        position = random.randint(0, len(my_list)-1)
        short_password += str(my_list[position])
    return short_password

print(generate_short_password(10, symbols))
print(generate_short_password(10, letters))
