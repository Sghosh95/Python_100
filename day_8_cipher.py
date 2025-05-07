import string
alphabet=[letter for letter in string.ascii_lowercase]
encrypted_list=[]
decrypted_list=[]

def encryption(word,cipher_value):
    for letter in word:
        if letter in alphabet:
            letter_index=alphabet.index(letter) 
            encryption_index=letter_index+cipher_value
            #with if else
            # if encryption_index>len(alphabet)-1:
            #     encryption_index=encryption_index-len(alphabet)
            #     encrypted_letter=alphabet[encryption_index]
            # else:
            #     encrypted_letter=alphabet[encryption_index]
            
            #with another approach
            encryption_index %= len(alphabet)
            encrypted_letter=alphabet[encryption_index]
            encrypted_list.append(encrypted_letter)

    encrypted_word=""
    for elements in encrypted_list:
        encrypted_word+=elements
    print("Encryption completed :",encrypted_word)

# word=input("Enter word to encrypt: ")
# cipher_value=int(input("Enter the cipher value: "))
# print("Your original word :",word)
# encryption(word,cipher_value)

def decryption(word,cipher_value):
    for letter in word:
        if letter in alphabet:
            letter_index=alphabet.index(letter) 
            decryption_index=letter_index-cipher_value
            #with if else
            # if encryption_index>len(alphabet)-1:
            #     encryption_index=encryption_index-len(alphabet)
            #     encrypted_letter=alphabet[encryption_index]
            # else:
            #     encrypted_letter=alphabet[encryption_index]
            
            #with another approach
            decryption_index %= len(alphabet)
            decrypted_letter=alphabet[decryption_index]
            decrypted_list.append(decrypted_letter)

    decrypted_word=""
    for elements in decrypted_list:
        decrypted_word+=elements
    print("Decryption completed :",decrypted_word)

# word=input("Enter word to decrypt: ")
# cipher_value=int(input("Enter the cipher value: "))
# print("Your original word :",word)
# decryption(word,cipher_value)


def cipher(word,cipher_value,encode_or_decode):
    operated_word=""
    decrypted_list=[]
    for letter in word:
        if encode_or_decode=="decode":
            cipher_value*=-1
        if letter in alphabet:
                letter_index=alphabet.index(letter) 
                decryption_index=letter_index+cipher_value
                #with if else
                # if encryption_index>len(alphabet)-1:
                #     encryption_index=encryption_index-len(alphabet)
                #     encrypted_letter=alphabet[encryption_index]
                # else:
                #     encrypted_letter=alphabet[encryption_index]
                
                #with another approach
                decryption_index %= len(alphabet)
                decrypted_letter=alphabet[decryption_index]
                decrypted_list.append(decrypted_letter)
                print("original letter :",letter)
                print("output :",decrypted_letter)

    for elements in decrypted_list:
        operated_word+=elements
    print(f"operation {encode_or_decode} completed for word {word}.Result : {operated_word}")

continue_operation=True

while continue_operation:

    encode_or_decode=input("Enter choice : 1. encode .. \n2.decode")
    word=input("Enter word :")
    cipher_value=int(input("Enter cipher value :"))

    cipher(word,cipher_value,encode_or_decode)

    print("Want to restart ? ")
    restart=input("1.Yes\n2.No").lower()
    if restart=="no":
        print("See you later. Good Bye!")
        continue_operation=False



                       


