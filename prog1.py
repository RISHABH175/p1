pt = input("Enter the plain Text").lower()
pt = [ord(a)-97 for a in pt]
key = int(input("Enter the key"))
print("Encrypted text is")
cip = []
for i in pt:
    cip.append((i+key)%26)
    print(chr((i+key)%26+97),end="")
print()
print("Decrypted text is")
for i in cip:
    print(chr((i-key)%26+97),end="")