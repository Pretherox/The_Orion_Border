from act_1_events import ship

def score():
  food_score = ship.food * 100
  fuel_score = ship.fuel * 200
  crew_score = ship.crew * 500
  ship_state_score = 0
  ship_parts_score = 0

  if ship.hull_state is False:
    ship_state_score = ship_state_score + 2500
  if ship.hull_parts is True:
    ship_parts_score = ship_parts_score + 2000
  if ship.reactor_state is False:
    ship_state_score = ship_state_score + 2500
  if ship.reactor_parts is True:
    ship_parts_score = ship_parts_score + 2000
  if ship.weapon_system is True:
    ship_parts_score = ship_parts_score + 2500

  total_score = ship_parts_score + ship_state_score + food_score + fuel_score

  print('=======SCORE=======')
  print('Food score ',food_score)
  print('Fuel score ',fuel_score)
  print('Crew score ',crew_score)
  print('Ship state score ', ship_state_score)
  print('Ship parts score ', ship_parts_score)
  print('\n')
  print('Total score ',total_score)