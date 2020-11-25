a = ["Dammit, I'm mad!", 
    "Go hang a salami I'm a lasagna hog."] 

def is_palindrome(my_string): 
    new_string = ''.join([item for item in my_string if item.isalpha()])
    lower_letters = new_string.lower()
    return lower_letters == lower_letters[::-1]  
    

def main():
    my_list = ["Dammit, I'm mad!", 
    "Go hang a salami I'm a lasagna hog."] 
    for item in my_list:
        if not is_palindrome(item) :
            print("No luck this time...")
        else:
            print("It's a good day for science..")


if __name__  == "__main__":
    main()  

c = a[0] 
# f = 0
# e = len(c)-1 #e=15

# while not c[f].isalpha():
#     f += 1

# while not c[e].isalpha():
#     e -= 1 #e = 14

# while c[f].lower() == c[e].lower() and f < e:
#     f += 1 #f=1, f=2, f=3, f=4, f=5
#     e -= 1 #e=13, e=12, e=11, e=10, e=9, e=8, e=7, e=6, e=5
#     if f > e:
#         print("No luck this time...")
#     while not c[f].isalpha():
#         f += 1
#     while not c[e].isalpha():
#         e -= 1
# if f < e:
#     print("No luck this time...")
# else: 
#     print("It's a good day for science..") 

# c = a[1] 
# f = 0
# e = len(c)-1

# while not c[f].isalpha():
#     f += 1

# while not c[e].isalpha():
#     e -= 1

# while c[f].lower() == c[e].lower() and f < e:
#     f += 1
#     e -= 1
#     if f > e:
#             print("No luck this time...")
#     while not c[f].isalpha():
#         f += 1
#     while not c[e].isalpha():
#         e -= 1

# if f < e:
#     print("No luck this time...")
# else: 
#     print("It's a good day for science..") 
