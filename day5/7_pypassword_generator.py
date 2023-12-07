#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters_sample =  random.sample(letters, nr_letters)
# print(nr_letters_sample)
nr_letters_sample_join = ''.join(nr_letters_sample)
# print(nr_letters_sample_join)

nr_symbols_sample_join = ''.join(random.sample(symbols, nr_symbols))
# print(nr_symbols_sample_join)

nr_numbers_sample_join = ''.join(random.sample(numbers, nr_numbers))
easy_level_password = nr_letters_sample_join+nr_symbols_sample_join+nr_numbers_sample_join
print(f'Your easy level password is : {easy_level_password}')
# print(type(easy_level_password))

easy_level_password_list = list(easy_level_password)
# print(easy_level_password_list)
hard_level_password = ''.join(random.sample(easy_level_password_list, len(easy_level_password_list)))
print(f'You hard level password is : {hard_level_password}')
# print(type(hard_level_password))