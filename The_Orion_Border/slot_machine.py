import random
symbols = '7️⃣','🍒','🍇','🍉'

def play():
 results = random.choices(symbols,k=3) #selects 3 items from the symbol list at random

 print(f'{results[0]} | {results[1]} | {results[2]}') #prints the choosen symbols by printing theyr corresponding places
 if symbols[0] is results[0] and symbols[0] is results[1] and symbols[0] is results[2]: #makes sure it the 3 symbols are 7️⃣ to give the jakpot
    print('jakpot!!! 💰') #Lucky you

answer = '' #With out this variable "while answear != 'N'" wouldn't work ant the game wouldn't start
while answer != 'N':
 play()
 answer = input(str('Play another round? (Y/N):'))
 while answer != 'Y':
  if answer == 'N':
    print('Thank you for playing.') #is good to be polite
    break
  else:
    answer = input(str('Play another round? (Y/N):'))
