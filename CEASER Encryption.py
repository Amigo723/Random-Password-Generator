Ptext = input("enter th message which you want to Encrypt : ")
char1 = "abcdefghijklmnopqrstuvwxyz"
char2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = int(input("Enter the key value : "))
Cipher = " "
if Ptext.isupper():
    for i in Ptext:
        position = char2.find(i)
        newPosition = (position + key) % 26
        Cipher += char2[newPosition]
elif Ptext.islower():
    for i in Ptext:
        position = char1.find(i)
        newPosition = (position + key) % 26
        Cipher += char1[newPosition]
else:
    print("You entered the wrong text : ")

print("your Encrypted message is : " + Cipher)
