#main game
import Battle
import mc
import enemy
import Section_1
import random

#initializing main character
player = mc.main_character()
Section_1.start(player)
enemy = enemy.enemy()
def fight(player):
    print("A Dark souls spirit has spotted you and will attack")
    print ("Begin the battle")
    print("Use your sword and shield to attack the enemy")


#enemies.append(enemy.enemy(4))
#(syntax error says: tuple index out of range)
print("enemy atk ", enemy.attack)
Battle.attack(player,enemy)
while(player.hp>0):
    print("enemy atk ",enemy.attack)
while (player.hp==0) or (enemy.hp==0):
    print("battle over.")


#first attack

#print(player.hp)
##
##for turn in range (3):
##    print("turn ", turn)
##    Battle.attack(player,enemies[0])
##    
##battle.heal(player)
##print(player.hp)
