def is_palindrome(my_string):  

    front_of_string = 0
    end_of_string = len(my_string)-1 

    while not my_string[front_of_string].isalpha():
        front_of_string += 1

    while not my_string[end_of_string].isalpha():
        end_of_string -= 1 

    while my_string[front_of_string].lower() == my_string[end_of_string].lower() and front_of_string < end_of_string:
        front_of_string += 1 
        end_of_string -= 1 
        if front_of_string > end_of_string:
            print("No luck this time...")
        while not my_string[front_of_string].isalpha():
            front_of_string += 1
        while not my_string[end_of_string].isalpha():
            end_of_string -= 1
   

def main():
    my_list = ["Dammit, I'm mad!", 
    "Go hang a salami I'm a lasagna hog."] 
    for item in my_list:
        if is_palindrome(item) :
            print("No luck this time...")
        else:
            print("It's a good day for science..")


if __name__  == "__main__":
    main()         