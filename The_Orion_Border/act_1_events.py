from resources import Resources
from Dices import Dice
from Trading import Traders

ship = Resources(8,12,4,False,False,False,False,False,False)

def mission_traveler():
  
 print('A traveler is looking for a ship available to allow him travel to a nearby planet.')
 print('It says he\'s willing to pay for the trouble.')
 print('Accepting this request will use extra fuel.')
 print('\"yes\" = The expedition accepts the mission')
 print('\"not\" = The expedition ignores the mission')

 while True:
     m1 = input()
     print('\n')

     if m1 == 'yes':
      fuel_expenses = Dice.dice(2)
      food_reward = Dice.reward3(5,10,15)
      print('The job is done easely and without trouble. To do the trip the ship used ',fuel_expenses, 'units of fuel')
      print(food_reward, 'units of food has been given as a reward for the job.')
      print('\n')
      ship.fuel_used(fuel_expenses)
      ship.food_storage(food_reward)
      break
     elif m1 == 'not':
      print('The crew ignores the request and moves on.')
      print('\n')
      break
     else:
      print('Wrong imput, write \"yes\" or \"not\" to continue:')

def asteroid_impact():
 
 print('An asteroid is heading towards the ship!')
 
 asteroid_impact = Dice.dice(2) # this part decides the fate of the ship by rolling a d3
 if asteroid_impact == 0 and ship.hull_state is False: #The ship takes the shoot but the hull persist
  print('Luckily the hull was strong enough to endure the impact with no meaningfull damage.')
  print('\n')

 elif asteroid_impact == 0 and ship.hull_state is True: #The ship is too damaged to take the shoot, but the pilot manages to save the ship
  print('The pilot pulls out a quick move that alows the ship to avoid collision.')
  print('Sadly, such a maneuver cost 1 unit of fuel')
  ship.fuel_used(1)

 elif asteroid_impact >= 1 and ship.hull_state is True: #The ship takes the shoot and is too damaged to endure it
  asteroid_ship_save_roll = Dice.dice(2)
  if asteroid_ship_save_roll == 1: #Somehow the ship survives the impact, with a cost
     asteroid_crew_lost_impact = Dice.dice(2)
     print('The hull, even tough it\'s damaged, endured the hit, but')
     print('the incident took',asteroid_crew_lost_impact,' crew members lives.')
     ship.crew_remaining(asteroid_crew_lost_impact)
  elif asteroid_ship_save_roll == 2:
     #The impact was too much for the ship. "Game Over" baby
     ship.ship_game_over
     print('The asteroid goes through the ship like a bullet, causing catastrophic damage.')
  else:
    print('SHIP_ASTEROID_SAVE_THROW_ERROR') # Just in case I messed up something

 elif ship.hull_state is False:
    ship.hull_damage()
    print('The hull was able to withstand the impact, but it got severely damaged from it.')
 else:
    print('ASTEROID_HIT_HULL_STATE_ERROR') # Just in case I messed up something

# Electric storm
def electric_storm():

 print('The scaners show that the ship is aproaching an electrical anomaly.')
 print('Going through it would be the fastest way, but also the most dangerous.')
 print('Surrounding the anomaly would be the safest, but it will need more time and fuel')
 print('\"yes\" = The ship goes through the anomaly.')
 print('\"not\" = The ship surrounds the anomaly.')

 while True:
    m3 = input()
    print('\n')

    if m3 == 'yes':
     print('The ship advances, heading towards the electrical anomaly.')
     print('As the expedition ship aproaches arcs of electricity move around the star dust of the anomaly.')
     anomaly_safe_roll = Dice.dice(2)
     if anomaly_safe_roll == 1:
       print('Electrical arks form around the ship like an angry storm.')
       print('Some of the systems in the ship spark when an arc hits the ship, but furter damage is avoided.')
       print('The ship manages to get out of the storm with just minor scratches that are fixed soon enough.')
       break
     if anomaly_safe_roll >= 2:
      if ship.reactor_state is False:
       print('¡One of the arcs hit the ship! damaging the electrical systems and the reactor.')
       ship.reactor_damage()
       break
      if ship.reactor_state is True:
       print('¡One of the arcs hit the ship!')
       print('The already damaged reactor can not withstand the raw power of the storm, forcing a meltdown')
       ship.ship_game_over()
       break
      else:
        print('ELECTRIC_STORM_SAVE_ROLL_ERROR')

    elif m3 == 'not':
     electric_storm_safety = Dice.dice(2)
     print('The ship moves around the edge of the anomaly, avoiding the danger.')
     print('Nonetheless, safety has come with the extra cost of ',electric_storm_safety,' units of fuel.')
     ship.fuel_used(electric_storm_safety)
     break

    else:
     print('Wrong imput, write \"yes\" or \"not\" to continue:')
#scrap field event
def scrap_field():

#This roll will determinate if the scrap field has a scrap dealer or not
 scrap_field_version = Dice.dice(1) #Remember to fix this when event test is over
#This is the version where the scrap field is empty and the player will have to put it's ship at risk for the loot
 if scrap_field_version == 0: #Remember to fix this when event test is over 
   
  print('¡The ship has entered an area with a big scrap field!')
  print('The field can be explored with no need to use extra fuel since is close to the designated path of the ship.')
  print('Tough the debry seems very stable, going in with a faulty hull its greatly inadvisable.')
  print('\"yes\" = The ship goes into the scrap field to look for parts.')
  print('\"not\" = The ship keeps it\'s current course.')

  while True:
   m3 = input()
   print('\n')
    
   if m3 == 'yes':
       if ship.hull_state is True:
        print('Red lights and alarms go on around the ship as the damaged Hull tries to witsthand a storm of tiny pices of scrap.')
        print('Part of the ship despresurices as consecuence, forcing the crew to move out of the scrap field.')
        scrap_impact = Dice.dice(2)
        print('After the incident ',scrap_impact,' bodys where recovered.')
        ship.crew_remaining(scrap_impact)
        break
       elif ship.hull_state is False:
        print('Even with the constant noise of small pices of scrap hiting at the hull the structure of the ship')
        print('is able to endure it with no issues.')
        print('The ship whas able to salvage something from the scrap field:')
        scrap_field_reward = Dice.reward3(1,2,3)
        if scrap_field_reward == 1: #Electronic parts
          ship.reactor_parts_()
          print('Reactor parts: they can be used to fix a damaged reactor')
          break
        elif scrap_field_reward == 2: #Hull parts
          ship.hull_parts_()
          print('Hull parts: can be used to fix a ship\'s damaged hull')
          break
        elif scrap_field_reward == 3: #Weapon sistems online
          ship.weapons_online()
          print('Old artillery: can be instaled on a ships hull to provide protection')
          break
        else:
          print('SCRAP_FIELD_EVENT_REWARD: ERROR')
       else:
        print('SCRAP_FIELD_EVENT_ERROR')
   elif m3 == 'not':
      print('The ship continues the route passing nearby the scrap field')
   else:
      print('Wrong imput, write \"yes\" or \"not\" to continue:')

#In this version a recycling ship is alredy on the scrap field and will trade with the player
 elif scrap_field_version == 1: #Remember to fix this when event test is over

   #Price is 1 to 3 would be fuel as price, from 5 to 7 food
   scrap_parts_stock1 = Traders(None,None,None,'Hull parts: Keep that hull healty and strong: ')
   scrap_parts_stock2 = Traders(None,None,None,'Reactor parts: The engineer delight:')
   scrap_parts_stock3 = Traders(None,None,None,'Old artillery: Space is dangerous, buy this: ')

   print('¡The ship has entered an area with a big scrap field!')
   print('The radar indicates that there is a ship nearby, and is sending a signal with the')
   print('following message:')
   print('\"¡Hey!¡We arrive here first!¡If you want scrap, pay for it!\"')
   print('\n')
   while True:
    ship.exp_supplye()
    print('The recycling ship is offerinc the next items for sale.')
    print('Write the name of the item to buy it or \'exit\' if you want to finish buying.')
    print('=========SCRAP&PARTS=========')
    print(scrap_parts_stock1.merc_desc, 'only at', scrap_parts_stock1.price, 'of', scrap_parts_stock1.resource)
    print(scrap_parts_stock2.merc_desc, 'only at', scrap_parts_stock2.price, 'of', scrap_parts_stock2.resource)
    print(scrap_parts_stock3.merc_desc, 'only at', scrap_parts_stock3.price, 'of', scrap_parts_stock3.resource)
    trade_response = input()
    if trade_response == 'Hull parts' or trade_response == 'hull parts':
      scrap_parts_stock1.merc_on_stock(ship,ship.hull_parts,ship.hull_parts_)
    elif trade_response == 'Reactor parts' or trade_response == 'reactor parts':
      scrap_parts_stock2.merc_on_stock(ship,ship.reactor_parts,ship.reactor_parts_)
    elif trade_response == 'Old artillery' or trade_response == 'old artillery':
      scrap_parts_stock3.merc_on_stock(ship,ship.weapon_system,ship.weapons_online)
    elif trade_response == 'exit' or trade_response == 'Exit':
      print('A pleasure making business')
      break
    else:
      print('Wrong input')

 else:
   print('SCRAP_FIELD_VERSION_ROLL_ERROR')

# Abandoned ship
def abandoned_ship():

 print('The ship radar has caught a strange lecture nearby.')
 print('It\'s origin seems to come from another ship.')
 print('It has it\'s lights off and doesn\'t respond to radio calls.')
 print('Seems like it\'s possible to send a team of 2 crew members to board it.')
 print('\n')
 print('Sending a team can be risky, but profitable.')
 print('\"yes\" = A team is send into the ship.')
 print('\"not\" = The expedition ignores the ship and moves on.')

 def abandoned_ship_scenario_1():
   food_reward_m4 = Dice.reward2(5, 12)
   fuel_reward_m4 = Dice.reward2(2, 4)
   print('The team searchs the ship, but nobody is found on board.')
   print('After an a few hours, the team returns with ',food_reward_m4,' units of food and ',fuel_reward_m4,' of fuel.')
   print('The team refuses to steep foot on that ship again as they say they feelt been watch during the mission.')
   ship.food_storage(food_reward_m4)
   ship.fuel_storage(fuel_reward_m4)

 def abandoned_ship_scenario_2():
   print('The team goes into the ship with no issues. They report seen a room with the lights on')
   print('but when they aproach it, the communications are cut off.')

   print('After traying for a few hours to restablish communication unsuccessfully')
   print('the search team it\'s declared lost and the remaining crew decides to stay away from the ship')
   print('and continue theyr journey.')
   ship.crew_remaining(2)

 while True:
    m4 = input()
    print('\n')
    if m4 == 'yes':
     abandoned_ship_exploration_fates = Dice.reward2(abandoned_ship_scenario_1, abandoned_ship_scenario_2)
     abandoned_ship_exploration_fates()
     break

    elif m4 == 'not':
     print('It has been decided that it will be whiser to not board the ship.')
     break

    else:
     print('Wrong imput, write \"yes\" or \"not\" to continue:')

#Old fuel station
def old_fuel_station():

  print('The expedition has entered a new system.')
  print('There is a fuel supply station nearby, but seems like it has been undermaintinance for a long time.')
  print('The hulk of the supply station floats silently around a gas giant.')
  print('Seems like it has been abandoned as the docks have signs saying \"Out of order\" and \"Condemned\".')
  print('There could still be fuel left inside of the station.')
  print('\n')
  print('Send a team to look for fuel?')
  print('\"yes\" = A team will be sent into the station to look for fuel.')
  print('\"not\" = The expedition will continue theyr journey with out stop.')

  while True:
   m5 = input()
   print('\n')
   if m5 == 'yes':
     fuel_station_exploration = Dice.dice(2)
     print('The expedition boards the fuel suply station.')
     print('They where able to find ', fuel_station_exploration,' of fuel.')
     print('\n')
     print('While exploring the station, the team noticed that the machinery is not damaged')
     print('and only need power.')
     ship.fuel_storage(fuel_station_exploration)
     if ship.reactor_parts is False:
       print('Sadly, the reactor is missing some parts')
       print('and can not be fixed without them.')
       break
     elif ship.reactor_parts is True: #If the player has reactor parts, it can fix the station to get more fuel
       print('The reactor seems to be missing some parts.')
       print('The team could use the reactor parts stored at the ship to fix it.')
       print('\"yes\" = To use the reactor parts on fixtin the station reactor.')
       print('\"not\" = Leave the station with what the team alredy found.')
       while True:
         m5 = input()
         print('\n')
         if m5 == 'yes':
           ship.reactor_parts_use()
           print('A humming noise can be heard as the reactor, along with the rest of the station')
           print('comes back to life.')
           print('It only works for a few seconds before the screens all around the station alert')
           print('than a critical error has ocurred.')
           fuel_production = Dice.reward2(3,6)
           print('Yet, ',fuel_production,' units of fuel where produced by the industrial machinery in')
           print('that short time lapse.')
           ship.fuel_storage(fuel_production)
           break
         elif m5 == 'not':
           print('Reactor parts are a valuable resource. The crew decides')
           print('that is not worth use them to fix the station reactor.')
           print('The team lefts the station with that they already found.')
           break
         else:
           print('Wrong imput, write \"yes\" or \"not\" to continue:')
   elif m5 == 'not':
     print('The ship lefts behind the station, becoming just a tiny point in contrast of the')
     print('of the gas giant surface.')
     print('The expedition continues its journey.')
     break
   else:
       print('Wrong imput, write \"yes\" or \"not\" to continue:')

def radiation_storm():

  print('All screens on bord proyect a red alert with the next message:')
  print('DANGER: RADIATION WAVE IN COMMING, LOOK FOR SHELTER INMEDIATLY')
  print('\n')
  print('There is only 2 pods avaliable on bord that can shelter the crew from the wave.')
  print('Only 1 crew member can fit on a pod at the same time.')
  print('None the less, the ship could deploy a shield around the hulk to protect the crew')
  print('but to do it, the reactor will need 1 extra unit of fuel.')
  print('\n')
  print('¿Deploy shield?')
  print('\"yes\"= The shield will be deployed to protect the whole ship from the radiation wave.')
  print('\"not\"= The shield will not be deployed, and only 2 crew members will be safe from the radiation.')
  while True:
   m6 = input()
   if m6 == 'yes':
     print('\n')
     print('The reactor glows as it supplys the ship with the extra power needed to deploy the shield.')
     print('\n')
     print('The radiation lectures skyrocket out of the ships hull, going further byond safety limits.')
     print('Yet the shield reflects almost all of the radiation, leting through only a small')
     print('amount, within the range of non-hazardous')
     ship.fuel_used(1)
     break
   elif m6 == 'not':
     print('The smell of iron fills the ship, followed by a strange warm that engolfs anybody that')
     print('didn\'t find shelter on time.')
     print('\n')
     print('After a few hours, the ship automatic descontamination procedures are over and it\'t safe to go out of the pods again.')
     if ship.crew > 2:
       radiation_fatalitys = 2 - ship.crew
       positive_radiation_fatalitys = radiation_fatalitys * -1 #This part of the code is to turn the result of "radiation_fatalitys" into a possitive number
       print('There where',positive_radiation_fatalitys,' crew members that died from severe radiation poisoning')
       ship.crew_remaining(positive_radiation_fatalitys)
       break
     elif ship.crew <= 2:
       print('Luckily, there where enough pods for the crew.')
       break
   else:
       print('Wrong imput, write \"yes\" or \"not\" to continue:')

def pirate_ship():

 print('A ship is aproaching the expedition with an incomming message:')
 print('\"Shut down your thrusters and surrender your booty! Do it and we will be mercifull!\"')
 print('The pirates weapon system is pointing at us.')
 print('\n')
 print('The crew is awaiting orders')
 print('\"Surrender\" = shut down the thrusters and lets the pirates come abord in hopes for them be less cruel')
 print('\"Evade\" = try to gain distance and scape from the pirate ship reach. It will be risky.')
 if ship.weapon_system is True:
   print('\"Attack\" = shoot our artillery against them. This will have unpredictable results.')
 while True:
   m7 = input()
   if m7 == 'Surrender' or m7 == 'surrender':
     print('The thrusters of the ship become quiet as they loose power. The pirates hurry up on aproaching as they send a shuttle to get onboard.')
     print('\"That was the correct call! Common boys! let\'s help them lose some weight!\"')
     ship.food = round(ship.food / 2)#round is to make sure there is no decimals on the output
     ship.fuel = round(ship.fuel / 2)
     break
   elif m7 == 'Evade' or m7 == 'evade':
     print('The ship thrusters increase theyr potency on an attempt to gain as much distance as possible from the pirates')
     print('but their weapon system responds rapidly at the rebellious answear.')
     print('\n')
     exp_scape_attempt = Dice.dice(2)
     if exp_scape_attempt == 1:
       print('Various shoots impact against the hull of the ship')
       if ship.hull_state is False:
         print('damagin it greatly.')
         print('Yet, the ship manages to scape from the pirates.')
         print('\n')
         ship.hull_damage()
         break
       else:
         print('turning to scrap the already damaged hull, producing catastrophic damages')
         print('and destroying the ship.')
         print('\n')
         ship.ship_game_over()
         break
     else:
       print('The rapid reflexes of the pilot allow him to evade the inccoming shoots with')
       print('some complicated manouvers. This effort none the less, put a lot of stress on the')
       print('thrusters and consumed some extra fuel.')
       ship.fuel_used(1)
       break
   elif m7 == 'Shoot' and ship.weapon_system is True or m7 == 'shoot' and ship.weapon_system is True:
     print('The artillery system rapidly targets the pirate ship and shoots')
     pirate_battle = Dice.dice(2)
     if pirate_battle == 1:
       print('with such precision that it explodes inmediatly, leaving mostly scrap.')
       print('\n')
       ship.food_storage(4)
       ship.fuel_storage(2)
       print('After searching the remains, 4 units of food and 2 of fuel where recovered.')
       print('\n')
       break
     else:
       print('at them, seemingly leaving them confuse, as they rapidly turn back and scape')
       print('not expecting theyr prey to fight back.')
       print('\n')
       break
   else:
     print('Wrong input')