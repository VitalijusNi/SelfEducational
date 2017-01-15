
get_message = str(input("Enter your message to encrypt: "))
key = int(input("How many charatcets should we shift(1 - 25): "))

words_encrypt = ""

for i in get_message:

    if i.isalpha():

        for convert in i:

            if convert.isupper():
                numb = int(ord(convert) + key)
                if numb > ord("Z"):
                    words_encrypt += str(chr(numb - 26))

                elif numb < ord("A"):
                    words_encrypt += str(chr(numb + 26))

                else:
                    words_encrypt += str(chr(numb))

            if convert.islower():

                numb = int(ord(convert) + key)

                if numb > ord("z"):

                    words_encrypt += str(chr(numb - 26))
                elif numb < ord("a"):
                    words_encrypt += str(chr(numb + 26))

                else:

                    words_encrypt += str(chr(numb))

    else:
        words_encrypt += i



print(words_encrypt)

decrypt = str(input("Enter your encrypted message: "))

key2 = int(input("Enter your key for encryption: "))

key = -key2

original_msg = ""

for i in decrypt:

    if i.isalpha():

        for convert in i:


            if convert.isupper():
                numb = int(ord(convert) + key)
                if numb > ord("Z"):
                    original_msg += str(chr(numb - 26))

                elif numb < ord("A"):
                    original_msg += str(chr(numb + 26))

                else:
                    original_msg += str(chr(numb))

            if convert.islower():

                numb = int(ord(convert) + key)

                if numb > ord("z"):

                    original_msg += str(chr(numb - 26))
                elif numb < ord("a"):
                    original_msg += str(chr(numb + 26))

                else:

                    original_msg += str(chr(numb))

    else:
        original_msg += i



print(original_msg)



