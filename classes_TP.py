import random

class Personnage:
    hp = 100
    pa = 20
    def getHp(self):
        return self.hp
    def setHp(self, newHp):
        self.hp = newHp


class Sorcier(Personnage):
    pa = 10
    potion = 5
    def getPotion(self):
        return self.potion()
    def setPotion(self, restePotion):
        self.potion = restePotion
    def attack(self, target):
            coefAttack = 0
            coefAttack = random.uniform(0.1, 1)
            totalAttack = self.pa*coefAttack
            prendPotion  = random.randint(1,2)

            if (prendPotion ==2):
                    self.setHp(self.getHp()+15)
                    print("le Sorcier prend une Potion :"+str(15)+"pv")
                    print("hp restant:"+ str(self.getHp()))

            target.setHp(target.getHp()-totalAttack)
            print("le Sorcier inflige "+str(totalAttack)+"de degat a l'enemie")
            print("hp restant:"+ str(target.getHp()))


class Guerrier(Personnage):
    hp=120
    def attack(self, target):
        coefAttack = 0
        coefAttack = random.uniform(0.1, 1)
        totalAttack = self.pa*coefAttack
        autoAttaque  = random.randint(1,5)

        if (autoAttaque ==5):
                self.setHp(self.getHp()-totalAttack)
                print("le Guerrier s'ataque lui meme :"+str(totalAttack)+"de degat")
                print("hp restant:"+ str(self.getHp()))
        else :
            target.setHp(target.getHp()-totalAttack)
            print("le Guerrier inflige "+str(totalAttack)+"de degat a l'enemie")
            print("hp restant:"+ str(target.getHp()))
