from Key import Key
import string 

class Decodage():
   def __init__(self,message):
     self.__Alphabet=list(string.ascii_lowercase)
     self.__message=message
     self.__keyy=Key(len(message))
     self.__key=self.__keyy.get_key() 
     self._Decoded_message=[]
     self.__hist=[self.__keyy.get_hist()]
   def get_hist(self):
     return self.__hist
   
   def get_Decoded_message(self): 
    self.__message = self.__message.replace(" ", "")
    ind_1 = [ord(c.lower()) - 97 for c in self.__message]
    self.__hist.append("message"+"\n" )
    self.__hist.append(str(ind_1)+"\n")
    ind_2 = [ord(c.lower()) - 97 for c in self.__key]
    self.__hist.append("clé"+"\n") 
    self.__hist.append(str(ind_2)+"\n")
    ind = [(ind_1[i]-ind_2[i]) % 26 for i in range(len(ind_1))]
    self.__hist.append("result"+"\n") 
    self.__hist.append(str(ind)+"\n") 
    self._Decoded_message = ''.join([self.__Alphabet[i] for i in ind])
    self.__hist.append(self._Decoded_message)
    return self._Decoded_message