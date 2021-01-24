Cipher = input("Enter the text you want to decrypt : ")
key = int(input("Enter the key : "))
char1 = "abcdefghijklmnopqrstuvwxyz"
char2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Ptext = ""

if Cipher.isupper():
    for i in Cipher:
        position = char2.find(i)
        newposition = (position - key) % 26
        Ptext += char2[newposition]
elif Cipher.islower():
    for i in Cipher:
        position = char1.find(i)
        newposition = (position - key) % 26
        Ptext += char1[newposition]
else:
    print("Entered text is wrong")

print("Decrypted message : " + Ptext)
