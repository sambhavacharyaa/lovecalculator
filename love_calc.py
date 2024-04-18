print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") 
name2 = input("What is your partner's name?\n") 

com_nm = name1 + name2
lower_names = com_nm.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l+o+v+e

final_digit = str(first_digit) + str(second_digit)

if int(final_digit) <10 or int(final_digit) > 90:
  print(f"Your score is {final_digit}, you go together like coke and mentos.")
elif int(final_digit) >= 40 and int(final_digit) <=50:
  print(f"Your score is {final_digit}, you are alright together.")
else:
  print(f"Your score is {final_digit}.")