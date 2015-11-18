# This is a game, where your character is fighting with monsters until he's level 3 or is dead.

__author__ = 'Simeon Petrov'
from random import randint

end_of_game = False
potions = 5


class Hero():
    def __init__(self):
        self.name = []
        self.atk = 10
        self.deff=5
        self.health = 50
        self.exp = 0
        self.lvl = 1


    def potion(self):
        global potions
        if potions == 0:
            print("You're out of potions!!!")
        else:
            self.health += 25
            potions -= 1
            print("You've have taken a potion. You restore 25pt health. You have left %s" % potions)


    def rase_lvl(self):
        self.atk+=1
        self.deff+=1
        self.health+=10
        self.exp-=10
        self.lvl +=1


class Enemy():
    def __init__(self):
        name = {0: "Goblin", 1: "Ork", 2: "Dark Elf", 3: "Boogie Man"}
        num = randint(0, 3)
        new = name[num]
        self.name = new
        if self.name == "Goblin":
            self.atk = 8
            self.deff=5
            self.health = 20
        elif self.name == "Ork":
            self.atk = 12
            self.deff=8
            self.health = 25
        elif self.name == "Dark Elf":
            self.atk = 10
            self.deff=6
            self.health = 30
        elif self.name == "Boogie Man":
            self.atk = 19
            self.deff=8
            self.health = 27


def fight(hero, enemy):
    print("     STARTING STATUS")
    print("         Hero:   Enemy:")
    print("Health:  %s       %s" % (hero.health, enemy.health))
    print("Atk:     %s       %s" % (hero.atk, enemy.atk))
    print("Def:     %s        %s" % (hero.deff, enemy.deff))
    print("Exp:     %s" % hero.exp)
    print("Lvl:     %s\n" % hero.lvl)
    
    while hero.health > 0 and enemy.health > 0:
        possibility = randint(0, 9)
        print("You attack the enemy!")
        if possibility <= 5:
            enemy.health -= (enemy.deff - hero.atk)*(-1)
            if enemy.health <0:
                enemy.health=0
        else:
            print("Oh No, you've missed!")
        possibility = randint(0, 9)
        print("The enemy hits you back.")
        if possibility <=5:
            hero.health -= (hero.deff - enemy.atk)*(-1)
            if hero.health <= 0:
                hero.health = 0
                print("\n\nOh... You're dead.")
                print("""You see the statue again, when it starts to speak..
                So you were not the chosen one...
                Welcome to your new home forever, mortal!""")
                global end_of_game
                end_of_game = True
        else:
            print("Good, the enemy missed you!")
        if hero.health != 0:
            print("     STATUS")
            print("         Hero:   Enemy:")
            print("Health:  %s       %s" % (hero.health, enemy.health))
            print("Atk:     %s       %s" % (hero.atk, enemy.atk))
            print("Def:     %s        %s" % (hero.deff, enemy.deff))
            print("Exp:     %s" % hero.exp)
            print("Lvl:     %s\n" % hero.lvl)
            decision = (input("Do you want a life potion? (y/n)")).lower()
            if decision == "y":
                hero.potion()
            print("\n")
    if hero.health > 0:
        hero.exp+=5
        print("You gained 5 experience. Total amount of experience: %s" % hero.exp)
    if hero.exp >=10:
        hero.rase_lvl()
        print("Woow, you just raised a level!")
    if end_of_game is False:
        print("You keep walking and after just a few steps...")


hero = Hero()
print("""Say hello to the underworld!
Here you can find many scary monsters.
And they're hungry!
But you can fight for your life!
So what do you choose...""")
print("You start walking through the darkness. After half an hour you see an old statue")
hero.name = input("What is your name, stranger... :")
print("%s, be aware that only the chosen one chan stay alive in the darkness!" % hero.name)
print("\nYou start walking away of the statue, when you see your first enemy\n")
while end_of_game == False:
    enemy=Enemy()
    print("A wild %s attacks you!" % enemy.name)
    fight(hero, enemy)
    if hero.lvl>=3:
        print("""You face the statue again, when it starts to speak..
        So you truly are the chosen one...
        And you seem to don't remember anything...
        Be gone from here, be gone Lord of the dark spirits...""")
        end_of_game = True
