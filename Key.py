 
import string
from basic_key import basic_key

class Key():

    def __init__(self,length):
      self.__lentgh=length 
      self.__SelectedCards=[]  
      self.__cards=basic_key().get_basic_key() 
      self.__key=[] 
      self.__Alphabet=list(string.ascii_lowercase)
      self.hist=""
    def get_hist(self):
       return self.hist
    def get_Cards(self):
        return self.__cards 

    def get_SelectedCards(self):
        return self.__SelectedCards 

    #premiere étape faire reculer les deux jokers 
    def JokersRecoil(self):      
            #mouvement JokerA   
             nouvel_index = (self.__cards.index(53)+1)%(len(self.__cards)-1)
             valeur = self.__cards.pop(self.__cards.index(53))  # retirer l'élément d'index 2 de la liste
             self.__cards = [valeur if x == nouvel_index else self.__cards[x] if x < nouvel_index else self.__cards[x-1] for x in range(len(self.__cards)+1)]
          #mouvement  jokerB
             nouvel_index1 = (self.__cards.index(53,nouvel_index+1)+2)%(len(self.__cards)-1)
             valeur = self.__cards.pop(self.__cards.index(53,nouvel_index+1))  # retirer l'élément d'index 2 de la liste
             self.__cards = [valeur if x == nouvel_index1 else self.__cards[x] if x < nouvel_index1 else self.__cards[x-1] for x in range(len(self.__cards)+1)]
    def max_Jokers_Index(self):
      if self.__cards.index(53) >self.__cards.index(53,self.__cards.index(53)+1):
        return self.__cards.index(53)
      else :
        return self.__cards.index(53,self.__cards.index(53)+1)

    def min_Jokers_Index(self):
      if self.__cards.index(53,self.__cards.index(53)+1)>self.__cards.index(53):
        return self.__cards.index(53)
      else:
        return  self.__cards.index(53,self.__cards.index(53)+1)

    #on extrapose les extremités de la liste contenant la liste contenu entre les deux jokers avec les jokers inclus 
    def doublecut_Over_Jokers(self):
       min=self.min_Jokers_Index()
       max=self.max_Jokers_Index()
       Right=[self.__cards[i]  for i in range(0,min) ]
       Left =[self.__cards[i]  for i in range(max+1,len(self.__cards)) ]
       body=[self.__cards[i]  for i in range(min,max+1)  ]
       self.__cards=[y for x in [Left,body,Right]  for y in x]
 
    def simple_Cut(self):
     n=self.__cards[len(self.__cards)-1]
     if n!=53 :
      firstPart=[self.__cards[i] for i in range(0,n)];  
      secondPart=[self.__cards[i] for i in range(n,len(self.__cards)-1)]
      self.__cards=[y for x in [secondPart,firstPart,[n]] for y in x]
      
       
    def reading_Aleatoir_value(self):
     i=0
     
     while(len(self.__SelectedCards)<self.__lentgh):
      self.hist+="********************************Melange"+str(i)+"\n"
      self.hist+=str(self.__cards)
      self.JokersRecoil()
      self.hist+="jokers_recoils"+"\n"
      self.hist+=str(self.__cards)+"\n"
      self.doublecut_Over_Jokers()
      self.hist+="double_cut"+"\n"
      self.hist+=str(self.__cards)+"\n"
      self.simple_Cut()
      self.hist+="simple cut"+"\n"
      self.hist+=str(self.__cards)
      self.__SelectedCards=[y for x in [self.__SelectedCards,[self.__cards[self.__cards[0]]%26]] for y in x]
      self.hist+="reading_aleatoire"+"\n"
      self.hist+=str(self.__SelectedCards)
      i=i+1
    def get_key(self):
      self.reading_Aleatoir_value()
      self.__key=''.join([self.__Alphabet[i] for i in  self.__SelectedCards])
      return self.__key 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        


 