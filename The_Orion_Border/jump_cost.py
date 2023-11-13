from act_1_events import ship

def ship_jump_cost():

 if ship.food - ship.crew < 0: #In case the expedition gets out of food but there whas still some for part of the crew
    ship.food_used(ship.crew)
    ship.crew_new(ship.food) #Had to use crew new since food_used will give a negative result
    ship.food = 0
    print ('\n')
    print('The lack of food has caused the loss of crew')
    print ('\n')
 else:
    ship.food_used(ship.crew)
 if ship.reactor_damage is True:
    ship.fuel_used(2)
    print ('\n')
    print('Because of the ship reactor damage, the ship wasted more fuel')
    print ('\n')
 else:
    ship.fuel_used(1)