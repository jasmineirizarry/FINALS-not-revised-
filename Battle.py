#battle functionality
import mc
import random

def attack(player,enemy):
    print("before attack hp: ", player.hp)

    player.hp -= enemy.attack
    print("after battle hp", player.hp)
    
