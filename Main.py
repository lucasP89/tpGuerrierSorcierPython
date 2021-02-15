from classes_TP import *
import time


player1 = Guerrier()
player2 = Sorcier()


while player1.hp > 0 or player2.hp > 0:
    player1.attack(player2)
    time.sleep(2)
    player2.attack(player1)
    time.sleep(2)
