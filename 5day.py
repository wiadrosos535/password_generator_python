import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
times_letters_loop_re = 0
while times_letters_loop_re < nr_letters:
    random.shuffle(letters)
    password += letters[1]
    times_letters_loop_re += 1

times_symbols_loop_re = 0
while times_symbols_loop_re < nr_symbols:
    random.shuffle(symbols)
    password += symbols[1]
    times_symbols_loop_re += 1

times_numbers_loop_re = 0
while times_numbers_loop_re < nr_numbers:
    random.shuffle(numbers)
    password += numbers[1]
    times_numbers_loop_re += 1
password_final = random.shuffle(password)
password_str = ''.join(password)



print(password_str)
