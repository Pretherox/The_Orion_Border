import random
from act_1_events import ship
from act_1_events import mission_traveler,asteroid_impact,electric_storm,scrap_field,abandoned_ship,old_fuel_station,radiation_storm,pirate_ship
from act_2_events import graveyard, meateors, black_hole, moon_colission, fungus_growth
from novrobsk_trading_station import novrobsk
from jump_cost import ship_jump_cost
from score import score
from pause import pause

def main():
 #act 1 event selector
 act_one_event_list = (mission_traveler,asteroid_impact,electric_storm,scrap_field,abandoned_ship,old_fuel_station,radiation_storm,pirate_ship)
 a1_event_manager_event_numeration = range(4)
 a1_event_manager_tale_list = random.sample(a1_event_manager_event_numeration, 4)

 #act 2 event selector
 act_two_event_list = (graveyard, meateors, black_hole, moon_colission, fungus_growth)
 a2_event_manager_event_numeration = range(3)
 a2_event_manager_tale_list = random.sample(a2_event_manager_event_numeration, 3)
 #=================Intro=================

 print('Like many others, a new crew has formed to try reach the deepest parts of the Galaxy, The Orion Border.')
 print('It\'s a dangeroys travel, where many had died traying. Make sure to have enough fuel and food for it.')
 #act one display of events
 for x in range(4):
  ship.exp_supplye()
  master_game_over()
  act_one_event_list[a1_event_manager_tale_list[x]]()
  pause()
  ship_jump_cost()

 #small pause for the player at a trading station
 master_game_over()
 novrobsk()
 print('after reposting and expending some time at the station, the expedition continues it\'s way.')
 pause()

 #act two commences over here
 for x in range(3):
  ship.exp_supplye()
  master_game_over()
  act_two_event_list[a2_event_manager_tale_list[x]]()
  pause()
  ship_jump_cost()

  print('After many hardships, the crew managed to arrive at theyr goal, been the first on ones to survive such')
  print('an odyssey.')
  print('\n')
  print('YOU WON! CONGRATULATIONS!')
  score()

#I moved here the game_over mechanic so the restart can be done easely
def master_game_over():
 if ship.fuel <= 0 or ship.crew <= 0 or ship.game_over is True:
    print('Like many others before, the expedition never arrive to it\'s destination at the Orion Border')
    score()
    while True:
      try_again = input(str('¿Try again?(yes/not)'))
      if try_again == 'yes':
        ship.food = 12 #all this should reset the ship variables, other whise, it will be instant game over if resseting, since it will start with the parameters that make you lose
        ship.fuel = 8
        ship.crew = 4
        ship.hull_state = False
        ship.hull_parts = False
        ship.reactor_state = False
        ship.reactor_parts = False
        ship.weapon_system = False
        main()
      elif try_again == 'not':
        exit()
      else:
        print('Wrong input.')

main()


