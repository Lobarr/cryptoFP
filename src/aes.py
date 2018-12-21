import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from src.helpers import strToBytes, encodeBytes, decodeBytes

class AES:
  """
  A class for encrypting and decrypting string data using AES symmetric encryption algorithm

  Parameters
  ----------
  data : str
    data to be encrypted 
  """
  def __init__(self, data: str=None) -> None:
    self.__key = os.urandom(32)
    self.__iv = os.urandom(16)
    self.__data = data
    self.__cipher = Cipher(algorithms.AES(self.__key), modes.CBC(self.__iv), backend=default_backend())
  """
  Getter for key, iv, data, and cipher 
  """
  def get_key(self):
    return encodeBytes(self.__key).decode('utf-8')
  def get_iv(self):
    return encodeBytes(self.__iv).decode('utf-8')
  def get_data(self):
    return self.__data
  def get_cipher(self):
    return self.__cipher
  def setData(self, data):
    self.__data = data
  """
  Encrypts provided data

  Returns : bytes
  -------
  ciphertext of encrypted data

  """
  def encrypt(self) -> str:  
    encryptor = self.__cipher.encryptor()
    return encodeBytes(encryptor.update(self.__padData()) + encryptor.finalize()).decode('utf-8')
  """
  Decrypts provded ciphertext

  Parameters
  ----------
  ct : bytes
    ciphertext of encrypted data
  
  Returns : str
  -------
  decrypted data
  """
  def decrypt(self, ct) -> str:
    decryptor = self.__cipher.decryptor()
    dt = decryptor.update(decodeBytes(ct.encode('utf-8'))) + decryptor.finalize()
    return self.__unpadData(dt).decode("utf-8")
  """
  appends padding to the provided data
  """
  def __padData(self):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(strToBytes(self.__data))
    padded_data += padder.finalize()  
    return padded_data
  """
  removes appended padding from the data
  """
  def __unpadData(self, dt):
    unpadder = padding.PKCS7(128).unpadder() #message is now decrypted... but now need to unpad
    data = unpadder.update(dt)
    unpadded = data + unpadder.finalize()
    return unpadded