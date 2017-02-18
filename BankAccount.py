
import threading
import random
import time


class BankAccount(threading.Thread):
    acctBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name,
                                                        customer.moneyRequest,
                                                        time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance is : ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in the account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

        time.sleep(3)


threadLock = threading.Lock()

mom = BankAccount("Mom", 1)
dad = BankAccount("Dad", 100)
sister = BankAccount("Sister", 50)

mom.start()
dad.start()
sister.start()

mom.join()
dad.join()
sister.join()

print("Execution Ends")
