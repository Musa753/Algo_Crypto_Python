import random
class basic_key():
  
  def __init__(self):
          self.__Cards=[]
 
  def get_basic_key(self):
   random.seed(42) # Graine fixe pour la génération de nombres aléatoires
   while len(self.__Cards) <52:
    num = random.randint(1,52)
    if num not in self.__Cards:
        self.__Cards.append(num)
   self.__Cards.append(53)
   self.__Cards.append(53)
   print(self.__Cards)
   return self.__Cards
 