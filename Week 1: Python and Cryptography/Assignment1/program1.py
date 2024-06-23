def encrypt(text,key):
    ans=""
    for char in text:
        if(char != ' '):
           new_char= chr((ord(char)-ord('a') + key)%26 + ord('a'))
           ans=ans+new_char

def decrypt(text,key):
    ans=""
    for char in text:
        if ord(char)-key<ord('a'):
            new_char=ord('z')-(key-(ord(char)-ord('a')))+1
            ans=ans+new_char

        else:
            new_char = chr(ord(char)-key)
            ans=ans+new_char

    return ans
        


task = int(input("Enter 1 for Encryption and 2 for Decryption"))
text = input("Enter the string")
key =input("Enter the key")

if task==1:
   encrypted_text=encrypt(text,key)
   print("The enctryped string is ",encrypted_text)

elif task==2:
   decrypted_text=decrypt(text,key)
   print("The decrypted string is ",decrypted_text)