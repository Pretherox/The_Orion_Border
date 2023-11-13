class Resources:
    def __init__(self, fuel, food, crew, hull_state, hull_parts, reactor_state, reactor_parts, weapon_system, game_over):
        self.fuel = fuel
        self.food = food
        self.crew = crew
        self.hull_state = hull_state
        self.hull_parts = hull_parts
        self.reactor_state = reactor_state
        self.reactor_parts = reactor_parts
        self.weapon_system = weapon_system
        self.game_over = game_over

    def fuel_storage(self,fuel_reward):
        self.fuel = self.fuel + fuel_reward
        return self.fuel
    def fuel_used(self,fuel_expenses):
        self.fuel = self.fuel - fuel_expenses
        return self.fuel
    def food_storage(self,food_reward):
        self.food = self.food + food_reward
        return self.food
    def food_used(self,food_expenses):
       self.food = self.food - food_expenses
       return self.food
    def crew_remaining(self,crew_lost):
        self.crew = self.crew - crew_lost
    def crew_new(self,crew_gain):
        self.crew = self.crew + crew_gain
    def hull_damage(self):
        self.hull_state = True
    def hull_parts_(self, number = None):
        self.hull_parts = True
    def reactor_damage(self):
        self.reactor_state = True
    def reactor_parts_(self, number = None):
        self.reactor_parts = True
    def reactor_parts_use(self):
        self.reactor_parts = False
    def weapons_online(self, number = None):
        self.weapon_system = True    
    def fix_hull(self):
        if self.hull_state is True and self.hull_parts is True:
            self.hull_state = False
            self.hull_parts = False
    def fix_reactor(self):
        if self.reactor_state is True and self.reactor_parts is True:
            self.reactor_state = False
            self.reactor_parts = False
    def ship_game_over(self):
     self.game_over = True

    def exp_supplye(self):
     print('\n')
     print('=====SUPPLIES=====')
     print('⛽ Fuel=',self.fuel,' '+'🥫 Food=',self.food,' '+'👤 Crew=',self.crew)
     if self.hull_state or self.reactor_state is True:
        print('=====🚨ALERTS🚨=====')
     if self.hull_state is True:
      print('⚠ ALERT ⚠: Structural integrity compromised. The ships hull needs urgent repair.')
     if self.reactor_state is True:
      print('☢ ALERT ☢: Reactors fluctiations are unstable. Emergency repairs are encouraged.')
     if self.weapon_system is True:
       print('=====WEAPON SYSTEM=====')
       print('⚠ ON-LINE ⚠')
     if self.hull_parts is True or self.reactor_parts is True:
        print('=====STORAGE=====')
     if self.hull_parts is True:
      print('Hull parts avaliable')
     if self.reactor_parts is True:
      print('Reactor parts avaliable')
     print('\n')
