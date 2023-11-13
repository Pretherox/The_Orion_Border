from act_1_events import ship
from Dices import Dice

#expedition graveyard
def graveyard():
        print('The expedition moves slowly through the wreckage of a ship graveyard.')
        print('While moving near the giant squeleton of a ship, a thin glimm can be seen at the other side.')
        print('It seems to be another ship that partialy intact, with some lights still on.')
        print('\n')
        print('A message is comming through:')
        print('\"Ha... hey guys... I need some help here... i\'m injuried, and that... thing broke my thrusters\"')
        print('\"There sould be some... ussefull things at the other side of the ship if we...\"')
        print('\n')
        print('The message is interrupted as the radar seems to have detected a huge signature aproaching our location.')
        print('\"Oh god! Is back! please hurry!\"')
        print('\n')
        print('There should be enough time to rescue the survivor, but not to take the resources.')
        print('\"Rescue\" = The civilian will be rescued but the possible resources will be lost')
        print('\"Loot\" = The resources will be retrieved, but the civilian will be left to his death')
        print('\"Leave\" = The ship leaves the graveyard as fast as it can.')
        while True:
            the_civilian_fate = input()
            if the_civilian_fate == 'Rescue' or the_civilian_fate == 'rescue':#the civilian is rescued, the loot is lost
                print('The expedition rapidly sends a rescue shuttle towards the damaged ship while')
                print('the ships of the graveyard are pushed away be a big creature with the resemblance of')
                print('a whale.')
                print('\n')
                print('The rescue team barely gets out on time as the giant space whale bites and swallos the other')
                print('ship.')
                print('The expedition hurrys to get away as it is still bussy chewing.')
                print('The survivor thanks us as joins our crew after his injuries are treated')
                ship.crew_new(1)
                break
            elif the_civilian_fate == 'Loot' or the_civilian_fate == 'loot':#the loot is saved, the civilian is not
                print('The expedition rapidly deploys an scavenger team towards the ship, getting all the loot')
                print('they can while the ships of the graveyard are pushed away be a big creature with the')
                print('resemblance of whale.')
                print('\n')
                print('Before leaving, the survivor of the other ship sends one last message, cursing the crew')
                print('for leaving him before the transmission is cuted off with a scream, as the giant space whale')
                print('bites and swallows his ship.')
                print('\n')
                inmoral_food = Dice.reward2(8,10)
                inmoral_fuel = Dice.reward2(1,2)
                print('We rescued ',inmoral_food,' units of food and ',inmoral_fuel,' units of fuel from the other ship.')
                ship.food_storage(inmoral_food)
                ship.fuel_storage(inmoral_fuel)
                break
            elif the_civilian_fate == 'Leave' or the_civilian_fate == 'leave':#literally, a "%!%# this, i'm out"
                print('Before the incomming mennace comes closer to the expedition, it is decided to leave')
                print('and not take unnecesary risks.')
                print('The man calling us before, sends another message, pleading the crew to come back, before')
                print('it\'s suddently cut off.')
                print('There are no more messages.')
                break
            else:
                print('Wrong input')

#black hole
def black_hole():
     print('The expedition is approaching a huge gravitational anomaly. Seems to be a black hole.')
     print('It is possible to avoid it, but the computer of the ship says that it is possible to use')
     print('the gravitational force of the black hole to impulse the ship without need of using fuel.')
     print('\n')
     print('It will be risky, since any error could make the ship go byond the event horizon.')
     print('¿Should we proceed?')
     print('\"Yes\" = If the ship sucess, fuel will not be expended.')
     print('\"Not\" = The ship will continue as normal with no risk.')
     while True:
          m2 = input()
          if m2 == 'Yes' or m2 == 'yes':
               roll_for_luck = Dice.dice(4)#this decides if the ship will have luck or not for they bravery
               if roll_for_luck == 1:
                    print('The ship moves towards the black hole, steping over its event horizon.')
                    print('\n')
                    print('The ship is gaining a lot of velocity, when suddently, something explodes')
                    print('making the whole ship to tremble violently and changing course towards the center')
                    print('of the black hole, sealing the fate of everyone on bord.')
                    ship.ship_game_over()#The dice wasn't mercifull enough
                    break
               elif roll_for_luck > 1:#the player got lucky, this time
                    print('The ship moves towards the black hole, steping over its event horizon.')
                    print('\n')
                    print('The ship is gaining a tremendous speed with no effort as the crew grabs them selfs')
                    print('to anithing nearby, as the whole ship trembles from the tension of the gravitational pull.')
                    print('\n')
                    print('After gaining enough momentum, the ship pulls out from the black hole edge towards')
                    print('their objective.')
                    ship.fuel_storage(1)#This will nullify the spended fuel for this event
                    break
          elif m2 == 'Not' or m2 == 'not':
               print('By moving at a safe distance from the black hole gravitational field, the expedition')
               print('rapidly leaves the system with no morre issues.')
               break
          else:
               print('Wrong input')

#meateors
def meateors():
     print('The sensors are detecting something of organic origin aproaching the ship at great speed.')
     print('The crew has practically no time to react when some kind of meteor made of flesh enters')
     print('our range.')
     print('\n')
     if ship.weapon_system is True:
          print('Fortunately, our weapon system rapidly pinpoints the threat and shoots at it')
          print('blowing the "meateor" into several junks of flesh.')
          print('\n')
          print('To make things even weirder, the flesh of the meateor seems to be edible')
          print('so the crew managed to gater some of the junks.')
          strange_meat = Dice.reward2(4,6)
          ship.food_storage(strange_meat)
     elif ship.weapon_system is False and ship.hull_state is True:
          print('Knowing that with the hull of the ship in such bad state, the ship will not survive an impact like this')
          print('the ships pilot tries out an emergency manouver to avoid colision.')
          print('\n')
          if ship.reactor_state is False: #If the reactor is not damaged, now it is
               print('The pilot managed to avoid the impact, but such manouver put a lot of stress into the reactor')
               print('damaging it.')
               ship.reactor_damage()
          else: #if the reactor was damaged, now is destroid.
               print('Even tough the pilot tried his best to avoid colision, the reactor couldn\'t keep')
               print('with the power demand needed to do it, forcing a meltdown.')
               ship.ship_game_over()
     else:
          print('Everithing trembles when the chunk of flesh impacts against the hull of the ship')
          print('sticking out the hull as if the ship had grow some kind of tumor.')
          print('\n')
          print('To make things even weirder, the flesh of the meateor seems to be edible.')
          ship.hull_damage()
          strange_meat = Dice.reward2(6,8)
          ship.food_storage(strange_meat)

#moon colission (resting event)
def moon_colission():
     print('While moving through a planet system designed as KCX-1288, the expedition witnessed') #reference to WH40k
     print('of a cosmic event, where the moon of a planetoid, colisioned against the surface of the planet')
     print('it rotates around.')
     print('\n')
     print('The event showed a beautiful tough apocalyptical expectacle that humble the crews heart.')
     print('\n')
     print('After this, the expedition continues it\'s journey.')

#strange fungus
def fungus_growth():
     print('During routine maintenance check on the ships system, a strange groth of mushrooms had spoted')
     print('growing near the ships reactor.')
     print('They seem to be growing thanks to the radiation emanating from the reactor.')
     print('\n')
     print('Is not sure if they could be used as a food source, since there is no clear readings from')
     print('theyr chemical composition. Eating them could be risky')
     print('\"Yes\" = A crew member eats a mushroom.')
     print('\"Not\" = The crew disposes of the mushrooms.')
     while True:
          m3 = input()
          if m3 == 'Yes' or m3 == 'yes':
               print('One of the crew members of the ship decides to eat one of the mushrooms to see if they are safe to consume.')
               print('\n')
               mushroom_luck = Dice.dice(2)
               if mushroom_luck > 1:
                    print('The crew awaits to see if the consuming of the mushrooms is safe, but their fears become true as the volunteer')
                    print('falls ill and convulsing on the ground.')
                    print('Soon later, the ship has one less crew member and the remaining mushrooms are incinerated.')
                    ship.crew_remaining(1)
                    break
               else:
                    print('Some time passes, and the volunteer is seemingly all right.')
                    print('The rest of the mushrooms are collected and storaged for later consumption.')
                    ship.food_storage(4)
                    break
          elif m3 == 'Not' or m3 == 'not':
               print('As a safety mesure, the mushrooms are colected and incinerated.')
               break
          else:
               print('Wrong input')
