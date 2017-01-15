
string = str(input("Enter a message to be encrypted: "))
secret = ""
for i in string:

    secret += str(ord(i)+100)


print("Your secret unicode:", secret)

uni_code = str(input("Write your UNICODE message: "))

message = ""

for i in range(0, len(uni_code)-1, 3):

    message += chr(int((uni_code[i] + uni_code[i+1] + uni_code[i+2]))-100)

print("Your original message: ", message)


