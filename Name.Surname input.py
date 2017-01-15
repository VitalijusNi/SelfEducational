
customers = []

while True:

    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].upper()

    if createEntry == "N":
        break

    elif createEntry == "Y":
        fName, lName = input("Enter customer Name :").split()

        customers.append({"fName": fName, "lName": lName})





# print data

for cust in customers:
    print(cust["fName"], cust["lName"])