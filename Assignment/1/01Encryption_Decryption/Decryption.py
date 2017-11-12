
#------------------------------------------------#

def decrypt():
    file_dir = input("Please enter the file name of the cipher text: ")
    #file_dir = "D:/Programing/Python/data2.txt"
    file_in = open(file_dir, "r")
    cipherText = ""
    for line in file_in:
        cipherText += line
    key = int(input("Key for decrypt : "))
    plainText = ""
    file_in.close()
    file_dir = input("Please enter the file name of the plain text: ")
    file_out = open(file_dir, "w")
    for i in range(len(cipherText)):
        if int(ord(cipherText[i])) >= 8211:
            plainText += chr((ord(cipherText[i]) - key*2) % 8482)
        else:
            plainText += chr((ord(cipherText[i]) - key) % 256)
    file_out.write(plainText)
    file_out.close()

#------------------------------------------------#
decrypt()