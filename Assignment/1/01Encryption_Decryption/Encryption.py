
# ----------------------------------------------------------

def encrypt(): #เข้ารหัส
    file_dir = input("Please enter the file name of the plain text: ")
    #file_dir = "D:/Programing/Python/data.txt"
    file_in = open(file_dir,"r")
    key = int(input("Enter key: "))
    #key = 2
    plainText = ""
    for line in file_in :
        plainText += line
    #print(plainText)
    cipherText = ""
    file_dir = input("Please enter the file name of the cipher text: ")
    file_out = open(file_dir,"w")
    for i in range(len(plainText)):
        if int(ord(plainText[i])) >= 8211: #Case that char over bound 256 ASCII => HTML
            cipherText += chr((ord(plainText[i]) + key*2) % 8482)
            #print((ord(plainText[i])), " = ", plainText[i], " => ", chr((ord(plainText[i]) + key) % 8482))
        else:
            cipherText += chr((ord(plainText[i]) + key ) % 256)
            #print((ord(plainText[i])), " = ", plainText[i], " => ", chr((ord(plainText[i]) + key) % 256))
    #print(cipherText)
    file_out.write(cipherText)
    file_in.close()
    file_out.close()

# -----------------------------------------------------------

encrypt()