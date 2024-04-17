import socket
from Decodage import Decodage
 
class Receiver():
    
  def __init__(self) -> None:
      self.data=''
      self.key_=''
      self.client_socket=any
      self.__hist=[]
      #self.connexion()
  def get_Hist(self):
     return self.__hist
  def connexion(self):
    # créer une socket P2P
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # lier la socket à une adresse et un port
    self.client_socket.bind(('localhost', 58885))
    self.client_socket.listen(1)
    self.conn, self.addr = self.client_socket.accept()
  
  def RecvMessage(self):
    self.key=self.conn.recv(1024).decode()
    #encoder et envoyer la clé 
    self.data=Decodage(self.key).get_Decoded_message()
    self.__hist=self.__hist+Decodage(self.key).get_hist()
     

 