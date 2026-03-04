import random
password_list = []
password=""
Char = input ("Enter The Alphabets you want in your Password Generator: ")
Char_List = list(Char.lower())
DIG = int (input("Enter The Digits you want in your Password Generator : "))
DIG_List = list(str(DIG))
Special = input ("Enter a bunch of special symbols you want in your Password Generator : ")
Special_list = list(Special)
Str_no = int (input("Enter the number of alphabets you want in your password : "))
Dig_no = int (input ("Enter the number of digits you want in your password : "))
Spec_no = int (input ("Enter the number of special char you want in your password : "))
print (f"Your password size is {Str_no+Dig_no+Spec_no}")
for i in range (0,Str_no):
    password_list.append(random.choice(Char_List))
for i in range (0,Dig_no):
    password_list.append(random.choice(DIG_List))
for i in range (0,Spec_no):
    password_list.append(random.choice(Special_list))
random.shuffle(password_list)
for i in password_list:
    password += i
print(f"Your lovely password is : {password}")