################################################################
def open_words():
    #file_dir = "D:/Programing/Python/words.txt"
    file_dir = input("Enter path of file word list : ")
    file_in = open(file_dir, "r")
    words = set()
    for line in file_in :
        words.add(line.strip().lower())
    file_in.close()
    return words

#################################################################
def crypta():
    #file_dir = "D:/Programing/Python/data2.txt"
    file_dir = input("Enter path of file cipher text : ")
    file_in = open(file_dir,"r")
    cipherText = ""
    for line in file_in:
        cipherText += line.strip()
    file_in.close()

    words = open_words() #Read string in function open_words

    count = [0 for i in range(0,256)]
    text =  ["" for i in range(0,256)]
    plainText = ""
    for i in range(10):
        for j in range(len(cipherText)):

            if int(ord(cipherText[j])) >= 8211:
                plainText += chr((ord(cipherText[j]) - i * 2) % 8482)
            else:
                plainText += chr((ord(cipherText[j])-i)%256)

        check_txt = plainText.split()
        for c in range(len(check_txt)):
            if check_txt[c].lower() in words:
                count[i] += 1
        text[i] += plainText
        #print("i = ",i, text[i])
        plainText = ""

    #Write to file text
    for n in range(len(count)):
        if count[n] == max(count):
            file_out = open(input("Enter path of file plaintext to write : "), "w")
            file_out.write(text[n])
            file_out.close()
            file_out = open(input("Enter path of file key to write : "), "w")
            file_out.write(str(n))
            file_out.close()
            break;
###############################################################

crypta()







