import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","~"]

u_letters = int(input("how many letters would you like in your password: "))
u_numbers = int(input("how many numbers would you like in your password: "))
u_symbols = int(input("how many symbols would you like in your password: "))
password = ""
final_passwd = []
for char in range(1,u_letters + 1):
    final_passwd.append(random.choice(letters))
for num in range(1,u_numbers + 1):
    final_passwd.append(random.choice(numbers))
for sym in range(1,u_symbols + 1):
    final_passwd.append(random.choice(symbols))

random.shuffle(final_passwd)

for passwd in final_passwd:
    password += passwd
print(password)