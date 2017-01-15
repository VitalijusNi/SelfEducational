
import random
import math
import time

class Warrior:
    def __init__(self, name="warrior", health=50, MAXdamage=20, MAXblock=10):
        self.name = name
        self.health = health
        self.MAXdamage = MAXdamage
        self.MAXblock = MAXblock

    def attack(self):

        damage = self.MAXdamage * (random.random() + .4)

        return damage

    def block(self):
        block = self.MAXblock * (random.random() + .5)

        return block


class Battle:
    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriordamage = warriorA.attack()

        warriorblock = warriorB.block()

        damage2WarriorB = math.ceil(warriordamage - warriorblock)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))
        time.sleep(1)
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))

            return "Game Over"
        else:
            return "Fight Again"




def main():
    name1 = str(input("Enter a name of first Warrior:"))
    name2 = str(input("Enter a name of second Warrior:"))
    war1 = Warrior(name1)
    war2 = Warrior(name2)

    battle = Battle()

    battle.startFight(war1, war2)



main()