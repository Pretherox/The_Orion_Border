
'''
I decided to put to each condition theyr own answears instead a common one so i don't need to writhe a condition in case
the player trys to fix the ship with no damage on it.
'''

def pause():
  from act_1_events import ship
  while True:
    if ship.hull_state is True and ship.hull_parts is True or ship.reactor_state is True and ship.reactor_parts is True:
      print('\n')
      print('While the ship continues its journey, it is possible to fix the ship.')
      print('Write \"Hull\" or \"Reactor\" depending on what you want to fix, if you have the parts.')
      pause_ip = input('To continue with out repairs just write \"continue\": ')
      if pause_ip == 'continue' or pause_ip == 'Continue':
       break
      elif pause_ip == 'hull' or pause_ip == 'Hull':
       if ship.hull_state is True and ship.hull_parts is True:
        print('The hull of the ship has been fixed')
        print('\n')
        ship.hull_state = False
        ship.hull_parts = False
        break
       else:
        print('can\'t do')
      elif pause_ip == 'reactor' or pause_ip == 'Reactor':
       if ship.reactor_state is True and ship.reactor_parts is True:
        print('The reactor of the ship has been fixed')
        print('\n')
        ship.reactor_state = False
        ship.reactor_parts = False
        break
       else:
        print('can\'t do')
      else:
       print('Wrong imput')
    else:
     print('\n')
     pause_ip = input('Please, write \"continue\" to continue your adventure: ')
     if pause_ip == 'continue' or pause_ip == 'Continue':
      break
     else:
      print('Wrong imput')