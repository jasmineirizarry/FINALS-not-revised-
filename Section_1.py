#pre-battle/section 1 game
#input user and run to see what it gives you
#insert a start

import mc as main_character
def start(player):
    print("Welcome to the secret life of JajaLinks")
    print('the fate of the village is up to you')
    print('go to the shop to choose your weapons to fight the dark soul in an intense battle')
    
    choice=input('choose between a metal(a) or wooden sword(b)')
    if (choice == 'a'):
        print('metal sword')
        player.inventory.append('metal sword')
        
    choice= input('choose between a metal shield(x) or a wooden shield(y)')
    if (choice == 'x'):
        print('metal shield')
        player.inventory.append('metal shield')



#use == to check

##    print("choose your weapon and armor")
##    
##def choose(weapon)
##print("metal sword")
##def cost(40 marbles)
##
##if player does not want metal sword:
##    print("next")
##    
##def choose(next weapon)
##print("wooden sword")
##
##if player wants wooden sword:
##print("yes")
##def cost(20 marbles)
##
##def choose(sheild)
##print("metal sheild")
##
##if player wants metal shield:
##    print("Yes")
##
##if player does not want metal shield:
##    print("No")
##
##def choose(shield)
##print("wooden shield")
##
##if player does wants wooden shield
##    print("yes")
##    
