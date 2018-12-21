from caesarcipher import CaesarCipher

class Caesar:
  """
  A class for bruteforcing a caeser cipher ciphertext 
  
  Parameters
  ----------
  ct : str
    ciphertext to be bruteforced
  """
  def __init__(self, ct, key: int=None):
    self.__ct = ct
    self.__key = key   
  """
  Getter for key
  """ 
  def get_key(self):
    return self.__key
  """
  Returns : string
  -------
  encrypted value of ciphertext
  """
  def encrypt(self) -> str:
    cipher = CaesarCipher(self.__ct, offset=self.__key)
    return cipher.encoded
  """
  Returns : string
  -------
  decrypted value of ciphertext
  """
  def decrypt(self) -> str:
    cipher = CaesarCipher(self.__ct, offset=self.__key)
    return cipher.decoded