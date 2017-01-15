


    #
   ###
  #####
 #######
#########
    #



tall= input("How tall tree gona be: ")

tall = int(tall)

spaces = tall - 1

hashes = 1

stump = tall - 1

while tall !=0:
    for i in range(spaces):
        print(" ",end="")

    for i in range(hashes):
        print("#", end="")

    print()

    spaces -= 1

    hashes += 2

    tall -= 1


for i in range(stump):
    print(" ", end="")
print("#")