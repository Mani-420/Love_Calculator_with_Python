welcome = 'Welcome to Love Calculator.'
print (welcome.center(75))

name1 = input("Enter your Name: ")
name2 = input("Enter your Crush Name: ")

your_name = name1.lower()
crush_name = name2.lower()

full_name = your_name + crush_name

t_inName = full_name.count("t")
r_inName = full_name.count("r")
u_inName = full_name.count("u")
e_inName = full_name.count("e")
l_inName = full_name.count("l")
o_inName = full_name.count("o")
v_inName = full_name.count("v")
e_inName = full_name.count("e")

true = int(t_inName + r_inName + u_inName + e_inName)
love = int(l_inName + o_inName + v_inName + e_inName)

score = str(true) + str(love)
love_percentage = int(score)

if (love_percentage <= 40):
    print(f"Your love score is: {love_percentage}%. You will be like Coke and Mentos.")
elif (love_percentage > 40 and love_percentage <= 70):
    print(f"Your love score is: {love_percentage}%. You will look Good together.")
else:
    print(f"Your love score is: {love_percentage}%. You will be like Love Birds.")
