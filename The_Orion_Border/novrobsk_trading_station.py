from Trading import Traders
from act_1_events import ship

def novrobsk():
 novrobsk_stock1 = Traders(3,'food',None,'Fuel tank: a fuel tank filled to it\'s max capacity with ship fuel.')
 novrobsk_stock2 = Traders(3,'fuel',None,'Food crate: a food crate repleated with space preserved food, delicious.')
 novrobsk_stock3 = Traders(None,None,None,'Crew member: a potential, and seemingly desperate person wants to join the crew, for a price.')

 print('The expedition has arrived to Novrobsk trading station, the last man constructed')
 print('land mark on the explored galaxy.')
 print('The ship is permited to dock and trade on the space dock before continuing it\'s journy')

 while True:
  ship.exp_supplye()
  print('=========NOVROBSK TRADING PORT=========')
  print(novrobsk_stock1.merc_desc, 'only at', novrobsk_stock1.price, 'of', novrobsk_stock1.resource)
  print(novrobsk_stock2.merc_desc, 'only at', novrobsk_stock2.price, 'of', novrobsk_stock2.resource)
  print(novrobsk_stock3.merc_desc, 'only at', novrobsk_stock3.price, 'of', novrobsk_stock3.resource)
  print('Write \"exit\" if you are done trading.')
  trade_response = input()
  
  if trade_response == 'Fuel tank' or trade_response == 'fuel tank' or trade_response == 'Fuel' or trade_response == 'fuel':
   novrobsk_stock1.merc_on_stock(ship,False,ship.fuel_storage,3)
  elif trade_response == 'Food crate' or trade_response == 'food crate' or trade_response == 'Food' or trade_response == 'food':
   novrobsk_stock2.merc_on_stock(ship,False,ship.food_storage,3)
  elif trade_response == 'Crew member' or trade_response == 'crew member' or trade_response == 'Crew' or trade_response == 'crew':
   novrobsk_stock3.merc_on_stock(ship,False,ship.crew_new,1)
  elif trade_response == 'exit' or trade_response == 'Exit':
   print('A pleasure making business')
   break
  else:
   print('wrong input')
  
