import codecs
################################################################
def open_words():
    file_dir = "words.txt"
    file_in = open(file_dir, "r")
    words = set()
    for line in file_in :
        words.add(line.strip().lower())
    #print(words)
    file_in.close()
    return words

def crypta():
    file_dir = "testdata.dat"

    with codecs.open(file_dir, "rb",encoding='cp1252') as f:
        cipherText = f.read()

    print(cipherText)

    #for line in cipherText:
    #    print(line, "=>", ord(line), " covert > ",chr((ord(line) - 179)%256), " => ", ((ord(line)-179+256)%256))
        #print(chr(line), " => ", ord(chr(line)), " => ",(ord(chr(line))-179+256)%256," => ", chr((ord(chr(line))-179+256)%256) )

    words = open_words() #Read string in function open_words

    count = [0 for i in range(0,256)]
    text =  ["" for i in range(0,256)]

    plainText = ""
    for i in range(256):
        for j in range(len(cipherText)):
            plainText += chr((ord(cipherText[j]) - int(i) + 256) % 256)
        #print("Key => ",i, plainText)
        check_txt = plainText.split()
        for c in range(len(check_txt)):
            if check_txt[c].lower() in words:
                count[i] += 1
        text[i] += plainText
        plainText = ""

    #Write to file text
    for n in range(len(count)):
        if count[n] == max(count):
            print(text[n])
            file_out = codecs.open("original_text.txt", "w",encoding='ISO-8859-1')
            file_out.write(text[n])
            file_out.close()
            file_out = open("key.txt", "w")
            file_out.write(str(n))
            file_out.close()
            break;


crypta()