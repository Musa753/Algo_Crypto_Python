from Encodage import  Encodage
import socket

class sender():
    
  def __init__(self,data) -> None:
      self.data=data
      self.key=any
      self.__hist=[]
      #self.connexion()
      
  def get_Hist(self):
     return self.__hist
  def connexion(self):
    # créer une socket P2P
    self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #self.sender_socket.setblocking(False)
    self.sender_socket.bind(('localhost', 58884))
    # se connecter à l'adresse et au port de la socket de réception
    self.sender_socket.connect(('localhost', 58885))
    
  def sendMessage(self):
    # encoder et envoyer la clé 
   if(self.key):
    self.sender_socket.sendall(self.key)
    self.sender_socket.close()
   else :
        self.key=Encodage(self.data).get_encoded_message()
        self.sender_socket.sendall(self.key.encode())
        self.sender_socket.close()

  def encodage_message(self):
     self.key=Encodage(self.data).get_encoded_message().encode()
     self.__hist=self.__hist+Encodage(self.key).get_hist()

 