from Dices import Dice

class Traders:
 def __init__(self,price,resource,on_stock,merc_desc):
  #This part generates the price at random with price_generator if no price is chosen manualy
  if price is not None:
   self.price = price
  else:
   self.price_generator()
  #It asigns the resource asigned to the price if none is manualy asigned
  if resource is not None:
   self.resource = resource
  else:
   self.resource_asignator()
  if on_stock is not None:
    self.on_stock = on_stock
  else:
    self.merc_on_stock(None,None,None,None)
  #description for the selling merc
    self.merc_desc = merc_desc

         
 def price_generator(self): #It creates a price between 1 and 7
   self.price = Dice.dice(7)
   return self.price
 def resource_asignator(self): #Designed to asign the trading resource depending of the quantity asked (3 or less will be fuel, more than 3 food)
   if self.price <= 3:
    self.resource = 'fuel'
   elif self.price >= 4:
    self.resource = 'food'
 def merc_on_stock(self,ship,merc,trade,number = None):
  if merc is False:
    if self.resource == 'food' and (ship.food - self.price) > 0 or self.resource == 'fuel' and (ship.fuel - self.price) > 0:
      print('A good adquisition')
      if self.resource == 'food':
       ship.food_used(self.price)  
       return trade(number)
      elif self.resource == 'fuel':
       ship.fuel_used(self.price)  
       return trade(number)
    else:
     print('Can\'t afford it')
  elif merc is True:
   print('You have already enough of those')
        